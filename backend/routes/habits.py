from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.habit import Habit

bp = Blueprint('habits', __name__, url_prefix='/api/habits', strict_slashes=False)

@bp.route('', methods=['POST'])
@bp.route('/', methods=['POST'])
@jwt_required()
def create_habit():
    try:
        data = request.get_json()
        user_id = int(get_jwt_identity())
        
        if not data.get('name') or not data.get('frequency'):
            return jsonify({'error': 'Name and frequency are required'}), 400
        
        habit = Habit(
            user_id=user_id,
            name=data.get('name'),
            frequency=data.get('frequency'),
            streak=data.get('streak', 0)
        )
        
        db.session.add(habit)
        db.session.commit()
        
        return jsonify({
            'message': 'Habit created successfully',
            'habit': habit.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('', methods=['GET'])
@bp.route('/', methods=['GET'])
@jwt_required()
def get_habits():
    try:
        user_id = int(get_jwt_identity())
        habits = Habit.query.filter_by(user_id=user_id).all()
        return jsonify({
            'habits': [habit.to_dict() for habit in habits]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_habit(id):
    try:
        user_id = int(get_jwt_identity())
        habit = Habit.query.filter_by(id=id, user_id=user_id).first()
        
        if not habit:
            return jsonify({'error': 'Habit not found'}), 404
        
        db.session.delete(habit)
        db.session.commit()
        
        return jsonify({'message': 'Habit deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500