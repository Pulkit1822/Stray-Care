import time
import RPi.GPIO as GPIO
from mqtt_client import MQTTClient
from sensor_config import SensorConfig

class SensorModule:
    def __init__(self):
        self.config = SensorConfig()
        self.mqtt_client = MQTTClient()
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config.TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(self.config.ECHO_PIN, GPIO.IN)

    def measure_distance(self):
        # Send trigger pulse
        GPIO.output(self.config.TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.config.TRIGGER_PIN, GPIO.LOW)

        # Wait for echo
        while GPIO.input(self.config.ECHO_PIN) == GPIO.LOW:
            pulse_start = time.time()

        while GPIO.input(self.config.ECHO_PIN) == GPIO.HIGH:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Speed of sound/2
        return round(distance, 2)

    def run(self):
        try:
            while True:
                distance = self.measure_distance()
                if distance < self.config.ALERT_THRESHOLD:
                    self.mqtt_client.publish_alert({
                        'type': 'proximity',
                        'distance': distance,
                        'timestamp': time.time()
                    })
                time.sleep(1 / self.config.SAMPLING_RATE)
        except Exception as e:
            print(f"Error in sensor loop: {str(e)}")
        finally:
            GPIO.cleanup()

