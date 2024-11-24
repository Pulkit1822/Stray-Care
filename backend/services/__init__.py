from .detection_service import DetectionService
from .alert_service import AlertService
from .analytics_service import AnalyticsService
from .notification_service import NotificationService

def init_services(app):
    app.detection_service= DetectionService(app.config)
    app.alert_service= AlertService(app.config)
    app.analytics_service= AnalyticsService(app.config)
    app.notification_service= NotificationService(app.config)
