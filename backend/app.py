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
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/mypal_db')
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
    print("Starting Flask app...")
    with app.app_context():
        try:
            db.create_all()
            print("✓ Database tables created successfully!")
        except Exception as e:
            print(f"ERROR creating tables: {e}")
    
    app.run(debug=True, host='0.0.0.0', port=5000)