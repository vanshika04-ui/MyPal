from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.mood import Mood

bp = Blueprint('moods', __name__, url_prefix='/api/moods')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_moods():
    try:
        user_id = get_jwt_identity()
        moods = Mood.query.filter_by(user_id=user_id).order_by(Mood.created_at.desc()).all()
        return jsonify([m.to_dict() for m in moods]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
@jwt_required()
def create_mood():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('mood_level'):
            return jsonify({"error": "Mood level is required"}), 400
        
        mood = Mood(
            user_id=user_id,
            mood_level=data['mood_level'],
            notes=data.get('notes', '')
        )
        
        db.session.add(mood)
        db.session.commit()
        
        return jsonify(mood.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500