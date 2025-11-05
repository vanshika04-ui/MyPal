from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.journal import Journal
from utils.nlp_analysis import analyze_sentiment

bp = Blueprint('journals', __name__, url_prefix='/api/journals')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_journals():
    try:
        user_id = int(get_jwt_identity())
        journals = Journal.query.filter_by(user_id=user_id).order_by(Journal.created_at.desc()).all()
        return jsonify([j.to_dict() for j in journals]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
@jwt_required()
def create_journal():
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        
        if not data.get('content'):
            return jsonify({"error": "Content is required"}), 400
        
        score, label = analyze_sentiment(data['content'])
        
        journal = Journal(
            user_id=user_id,
            title=data.get('title', ''),
            content=data['content'],
            sentiment_score=score,
            sentiment_label=label
        )
        
        db.session.add(journal)
        db.session.commit()
        
        return jsonify(journal.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_journal(id):
    try:
        user_id = int(get_jwt_identity())
        journal = Journal.query.filter_by(id=id, user_id=user_id).first()
        
        if not journal:
            return jsonify({"error": "Journal not found"}), 404
        
        return jsonify(journal.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_journal(id):
    try:
        user_id = int(get_jwt_identity())
        journal = Journal.query.filter_by(id=id, user_id=user_id).first()
        
        if not journal:
            return jsonify({"error": "Journal not found"}), 404
        
        db.session.delete(journal)
        db.session.commit()
        
        return jsonify({"message": "Journal deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500