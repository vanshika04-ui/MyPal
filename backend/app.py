from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from database import db

# Load environment variables
load_dotenv()

# ========== NLTK Data Setup for TextBlob/Sentiment Analysis ==========
# Download required NLTK data on first run
# This ensures TextBlob and future AI/ML features work properly
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data quietly
try:
    nltk.data.find('corpora/brown')
    print("✓ NLTK data already downloaded")
except LookupError:
    print("📥 Downloading NLTK data for sentiment analysis...")
    nltk.download('brown', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('wordnet', quiet=True)
    print("✓ NLTK data downloaded successfully")
# ========== End NLTK Setup ==========

app = Flask(__name__)
CORS(app)

# Configuration
# Try to get DATABASE_URL from environment (Railway sets this via plugin)
# First try direct MYSQL_URL reference
DATABASE_URL = os.getenv('MYSQL_URL') or os.getenv('DATABASE_URL')

# If Railway provides mysql://, convert to mysql+pymysql://
if DATABASE_URL and DATABASE_URL.startswith('mysql://'):
    DATABASE_URL = DATABASE_URL.replace('mysql://', 'mysql+pymysql://', 1)
    print(f"✓ Converted Railway MySQL URL")

# If still no DATABASE_URL, try building from individual vars
if not DATABASE_URL:
    MYSQLUSER = os.getenv('MYSQLUSER')
    MYSQLPASSWORD = os.getenv('MYSQLPASSWORD')
    MYSQLHOST = os.getenv('MYSQLHOST')
    MYSQLPORT = os.getenv('MYSQLPORT')
    MYSQLDATABASE = os.getenv('MYSQLDATABASE')
    
    print(f"DEBUG - Variables: USER={MYSQLUSER}, HOST={MYSQLHOST}, PORT={MYSQLPORT}, DB={MYSQLDATABASE}")
    
    if all([MYSQLUSER, MYSQLPASSWORD, MYSQLHOST, MYSQLPORT, MYSQLDATABASE]):
        DATABASE_URL = f'mysql+pymysql://{MYSQLUSER}:{MYSQLPASSWORD}@{MYSQLHOST}:{MYSQLPORT}/{MYSQLDATABASE}'
        print(f"✓ Built DATABASE_URL from individual variables")
    else:
        # Fallback - but this shouldn't happen in production
        print("✗ WARNING: No MySQL config found!")
        DATABASE_URL = 'sqlite:///temp.db'  # Temporary SQLite as last resort

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
print(f"Final DATABASE_URL starts with: {DATABASE_URL[:20]}...")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key')

print(f"✓ Database URL loaded: {DATABASE_URL}")

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Import models (after app and db are created)
with app.app_context():
    from models.user import User
    from models.habit import Habit
    from models.mood import Mood
    from models.journal import Journal

# Import and register blueprints
from routes.auth import bp as auth_bp
from routes.habits import bp as habits_bp
from routes.moods import bp as moods_bp
from routes.journals import bp as journals_bp

app.register_blueprint(auth_bp)
app.register_blueprint(habits_bp)
app.register_blueprint(moods_bp)
app.register_blueprint(journals_bp)

# Home routes
@app.route('/')
def home():
    return jsonify({
        "message": "MyPal API is running!", 
        "status": "success",
        "endpoints": {
            "auth": "/api/auth/register, /api/auth/login",
            "journals": "/api/journals",
            "habits": "/api/habits",
            "moods": "/api/moods"
        }
    })

@app.route('/health')
def health():
    try:
        # Try to execute a simple query to check database connection
        db.session.execute(db.text('SELECT 1'))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"
    
    return {
        "status": "healthy",
        "database": db_status,
        "version": "1.0.0"
    }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Use environment variable for port (Railway sets this)
    port = int(os.environ.get('PORT', 5000))
    
    # Only enable debug in development
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)