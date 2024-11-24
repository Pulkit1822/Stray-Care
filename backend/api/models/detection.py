from datetime import datetime
from app import db

class Detection(db.Model):
    
    id= db.Column(db.Integer, primary_key=True)
    animal_type= db.Column(db.String(50), nullable=False)
    confidence= db.Column(db.Float, nullable=False)
    
    location= db.Column(db.String(100), nullable=False)
    timestamp= db.Column(db.DateTime, default=datetime.utcnow)
    image_url= db.Column(db.String(200))
    metadata= db.Column(db.JSON)
    
    
    
    
    def to_dict(self):
        return {
            
            'id': self.id,
            'animal_type': self.animal_type,
            'confidence': self.confidence,
            'location': self.location,
            'timestamp': self.timestamp.isoformat(),
            'image_url': self.image_url,
            'metadata': self.metadata
        }
