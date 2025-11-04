from database import db
from datetime import datetime

class Habit(db.Model):
    __tablename__ = 'habits'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    frequency = db.Column(db.String(20))
    streak = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'frequency': self.frequency,
            'streak': self.streak,
            'created_at': self.created_at.isoformat()
        }