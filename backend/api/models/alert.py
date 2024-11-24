from datetime import datetime
from app import db

class Alert(db.Model):
    
    id= db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String(50), nullable=False)
    location= db.Column(db.String(100), nullable=False)
    severity= db.Column(db.String(20), nullable=False)
    timestamp= db.Column(db.DateTime, default=datetime.utcnow)
    status= db.Column(db.String(20), default='active')
    description= db.Column(db.String(200))
    image_url= db.Column(db.String(200))
    
    
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'location': self.location,
            'severity': self.severity,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status,
            'description': self.description,
            'image_url': self.image_url
        }
