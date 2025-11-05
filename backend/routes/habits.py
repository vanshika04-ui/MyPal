from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.habit import Habit

bp = Blueprint('habits', __name__, url_prefix='/api/habits')

@bp.route('/', methods=['GET'])
@bp.route('', methods=['GET'])
@jwt_required()
def get_habits():
    try:
        user_id = int(get_jwt_identity())
        habits = Habit.query.filter_by(user_id=user_id).all()
        return jsonify([h.to_dict() for h in habits]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
@bp.route('', methods=['POST'])
@jwt_required()
def create_habit():
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        
        if not data.get('name'):
            return jsonify({"error": "Habit name is required"}), 400
        
        habit = Habit(
            user_id=user_id,
            name=data['name'],
            description=data.get('description', ''),
            frequency=data.get('frequency', 'daily')
        )
        
        db.session.add(habit)
        db.session.commit()
        
        return jsonify(habit.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_habit(id):
    try:
        user_id = int(get_jwt_identity())
        habit = Habit.query.filter_by(id=id, user_id=user_id).first()
        
        if not habit:
            return jsonify({"error": "Habit not found"}), 404
        
        db.session.delete(habit)
        db.session.commit()
        
        return jsonify({"message": "Habit deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500