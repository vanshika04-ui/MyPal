from database import db
from datetime import datetime

class Mood(db.Model):
    __tablename__ = 'moods'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood_level = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text,nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='moods')
    
    def to_dict(self):
        return {
            'id': self.id,
            'mood_level': self.mood_level,
            'notes': self.notes,
            'created_at': self.created_at.isoformat()
        }