from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from database import db

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
# Build DATABASE_URL from individual MySQL environment variables
# This avoids issues with special characters in Railway
MYSQLUSER = os.getenv('MYSQLUSER')
MYSQLPASSWORD = os.getenv('MYSQLPASSWORD')
MYSQLHOST = os.getenv('MYSQLHOST')
MYSQLPORT = os.getenv('MYSQLPORT')
MYSQLDATABASE = os.getenv('MYSQLDATABASE')

# Build connection string for production, fallback to localhost for dev
if all([MYSQLUSER, MYSQLPASSWORD, MYSQLHOST, MYSQLPORT, MYSQLDATABASE]):
    DATABASE_URL = f'mysql+pymysql://{MYSQLUSER}:{MYSQLPASSWORD}@{MYSQLHOST}:{MYSQLPORT}/{MYSQLDATABASE}'
else:
    # Development fallback
    DATABASE_URL = 'mysql+pymysql://root:@localhost/mypal_db'
    
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
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
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Use environment variable for port (Railway sets this)
    port = int(os.environ.get('PORT', 5000))
    
    # Only enable debug in development
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)