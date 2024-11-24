from models.alert import Alert
from models.detection import Detection
from app import db

class AnalyticsService:
    def get_stats(self):
        try:
            alert_count= db.session.query(Alert).count()
            detection_count= db.session.query(Detection).count()
            return {
                'alert_count': alert_count,
                'detection_count': detection_count
            }
            
            
        except Exception as e:
            raise Exception(f"Error fetching stats: {str(e)}")

    def get_history(self, start_date, end_date):
        try:
            alerts= Alert.query.filter(Alert.timestamp.between(start_date, end_date)).all()
            detections= Detection.query.filter(Detection.timestamp.between(start_date, end_date)).all()
            return {
                'alerts': [alert.to_dict() for alert in alerts],
                'detections': [detection.to_dict() for detection in detections]
            }
        except Exception as e:
            raise Exception(f"Error fetching history: {str(e)}")
