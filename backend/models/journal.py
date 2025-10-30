from database import db
from datetime import datetime

class Journal(db.Model):
    __tablename__ = 'journals'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text, nullable=False)
    sentiment_score = db.Column(db.Float)
    sentiment_label = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'sentiment_score': self.sentiment_score,
            'sentiment_label': self.sentiment_label,
            'created_at': self.created_at.isoformat()
        }