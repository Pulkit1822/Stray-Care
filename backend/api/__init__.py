from flask import Blueprint
from .routes import alerts,analytics,detection


def create_api(app):
    # Register blueprints
    app.register_blueprint(alerts.bp,url_prefix='/api/alerts')
    app.register_blueprint(analytics.bp,url_prefix='/api/analytics')
    app.register_blueprint(detection.bp,url_prefix='/api/detection')
