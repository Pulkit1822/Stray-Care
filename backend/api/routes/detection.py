from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required
from services.detection_service import DetectionService


bp= Blueprint('detection',__name__)
detection_service= DetectionService()

@bp.route('/analyze',methods=['POST'])
@jwt_required()

def analyze_image():
    try:
        
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}),400
            
            
        image= request.files['image']
        results= detection_service.analyze_image(image)
        return jsonify(results),200
    
    except Exception as e:
        return jsonify({'error': str(e)}),400


@bp.route('/stream',methods=['POST'])
@jwt_required()
def process_stream():
    try:
        stream_data= request.get_json()
        results= detection_service.process_stream(stream_data)
        return jsonify(results),200
    except Exception as e:
        return jsonify({'error': str(e)}),400