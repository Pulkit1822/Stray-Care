from flask_mail import Message
from app import mail

class NotificationService:
    def send_alert_notification(self, alert):
        try:
            msg= Message(
                subject="New Alert Notification",
                sender="noreply@example.com",
                recipients=["user@example.com"]
            )
            msg.body= f"Alert Type: {alert['type']}\nLocation: {alert['location']}\nSeverity: {alert['severity']}\nDescription: {alert['description']}"
            mail.send(msg)
        except Exception as e:
            raise Exception(f"Error sending alert notification: {str(e)}")

    def send_detection_notification(self, detection):
        try:
            msg= Message(
                subject="New Detection Notification",
                sender="noreply@example.com",
                recipients=["user@example.com"]
            )
            msg.body= f"Animal Type: {detection['animal_type']}\nConfidence: {detection['confidence']}\nLocation: {detection['location']}\nTimestamp: {detection['timestamp']}"
            mail.send(msg)
        except Exception as e:
            raise Exception(f"Error sending detection notification: {str(e)}")
