import time
import cv2
import numpy as np
from mqtt_client import MQTTClient
from camera_config import CameraConfig

class CameraModule:
    def __init__(self):
        self.config = CameraConfig()
        self.mqtt_client = MQTTClient()
        self.camera = None
        self.is_running = False

    def initialize(self):
        try:
            self.camera = cv2.VideoCapture(self.config.CAMERA_ID)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.FRAME_WIDTH)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.FRAME_HEIGHT)
            self.is_running = True
            print("Camera module initialized successfully")
        except Exception as e:
            print(f"Error initializing camera: {str(e)}")
            raise

    def process_frame(self, frame):
        # Apply preprocessing
        processed = cv2.resize(frame, (self.config.PROC_WIDTH, self.config.PROC_HEIGHT))
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
        return processed

    def run(self):
        while self.is_running:
            try:
                ret, frame = self.camera.read()
                if ret:
                    processed_frame = self.process_frame(frame)
                    self.mqtt_client.publish_frame(processed_frame)
                time.sleep(1 / self.config.FPS)
            except Exception as e:
                print(f"Error in camera loop: {str(e)}")
                time.sleep(1)

    def cleanup(self):
        self.is_running = False
        if self.camera:
            self.camera.release()