from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.mood import Mood

bp = Blueprint('moods', __name__, url_prefix='/api/moods')

@bp.route('', methods=['POST'])
@bp.route('/', methods=['POST'])
@jwt_required()
def create_mood():
    try:
        data = request.get_json()
        user_id = int(get_jwt_identity())
        
        if not data.get('mood_level'):
            return jsonify({'error': 'Mood level is required'}), 400
        
        mood_level = int(data.get('mood_level'))
        if mood_level < 1 or mood_level > 5:
            return jsonify({'error': 'Mood level must be between 1 and 5'}), 400
        
        mood = Mood(
            user_id=user_id,
            mood_level=mood_level,
            notes=data.get('notes', '') 
        )
        
        db.session.add(mood)
        db.session.commit()
        
        return jsonify({
            'message': 'Mood logged successfully',
            'mood': mood.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('', methods=['GET'])
@bp.route('/', methods=['GET'])
@jwt_required()
def get_moods():
    try:
        user_id = int(get_jwt_identity())
        moods = Mood.query.filter_by(user_id=user_id).all()
        return jsonify({
            'moods': [mood.to_dict() for mood in moods]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500