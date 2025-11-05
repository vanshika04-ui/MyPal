from database import db
from datetime import datetime

class Mood(db.Model):
    __tablename__ = 'moods'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood_level = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # NO relationship defined here - it's defined in User model
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'mood_level': self.mood_level,
            'note': self.note,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }