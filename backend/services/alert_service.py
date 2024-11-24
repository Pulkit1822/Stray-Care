from models.alert import Alert
from app import db


class AlertService:
    
    def create_alert(self, data):
        alert= Alert(
            type=data.get('type'),
            location=data.get('location'),
            severity=data.get('severity'),
            description=data.get('description'),
            image_url=data.get('image_url')
        )
        
        db.session.add(alert)
        db.session.commit()
        return alert.to_dict()



    def get_all_alerts(self):
        
        
        alerts= Alert.query.all()
        return [alert.to_dict() for alert in alerts]

    def get_alert_by_id(self, alert_id):
        alert= Alert.query.get(alert_id)
        if alert:
            
            return alert.to_dict()
        
        return None

    def update_alert(self, alert_id, data):
        
        alert= Alert.query.get(alert_id)
        if not alert:
            
            return None
        alert.type= data.get('type', alert.type)
        alert.location= data.get('location', alert.location)
        alert.severity= data.get('severity', alert.severity)
        alert.description= data.get('description', alert.description)
        alert.image_url= data.get('image_url', alert.image_url)
        alert.status= data.get('status', alert.status)
        db.session.commit()
        
        return alert.to_dict()
