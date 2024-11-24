import cv2
import numpy as np
from datetime import datetime

def process_image(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def format_timestamp(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def calculate_risk_level(detection_data):
    # Risk calculation logic
    speed = detection_data.get('speed', 0)
    distance = detection_data.get('distance', 0)
    animal_count = detection_data.get('animal_count', 1)
    
    risk_score = (speed * 0.4) + (distance * 0.3) + (animal_count * 0.3)
    
    if risk_score > 0.7:
        return 'high'
    elif risk_score > 0.4:
        return 'medium'
    return 'low'
