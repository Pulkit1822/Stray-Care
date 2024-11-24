from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.alert import Alert
from services.alert_service import AlertService

bp= Blueprint('alerts', __name__)
alert_service= AlertService()

@bp.route('/', methods=['GET'])
@jwt_required()
def get_alerts():
    try:
        alerts= alert_service.get_all_alerts()
        return jsonify({'alerts': alerts}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:alert_id>', methods=['GET'])
@jwt_required()
def get_alert(alert_id):
    try:
        alert= alert_service.get_alert_by_id(alert_id)
        if alert:
            return jsonify(alert), 200
        return jsonify({'message': 'Alert not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/', methods=['POST'])
@jwt_required()
def create_alert():
    try:
        data= request.get_json()
        alert= alert_service.create_alert(data)
        return jsonify(alert), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400