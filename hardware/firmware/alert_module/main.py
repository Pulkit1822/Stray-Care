import time
import RPi.GPIO as GPIO
from mqtt_client import MQTTClient
from alert_config import AlertConfig

class AlertModule:
    def __init__(self):
        self.config = AlertConfig()
        self.mqtt_client = MQTTClient()
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config.LED_PIN, GPIO.OUT)
        GPIO.setup(self.config.BUZZER_PIN, GPIO.OUT)
        self.led_pwm = GPIO.PWM(self.config.LED_PIN, 100)
        self.buzzer_pwm = GPIO.PWM(self.config.BUZZER_PIN, 440)

    def trigger_alert(self, alert_type='warning'):
        if alert_type == 'warning':
            self.led_pwm.start(50)  # 50% duty cycle
            self.buzzer_pwm.start(50)
            time.sleep(0.5)
            self.led_pwm.stop()
            self.buzzer_pwm.stop()
        elif alert_type == 'danger':
            self.led_pwm.start(100)  # 100% duty cycle
            self.buzzer_pwm.start(100)
            time.sleep(1)
            self.led_pwm.stop()
            self.buzzer_pwm.stop()

    def run(self):
        try:
            while True:
                # Listen for alert messages from MQTT
                alert = self.mqtt_client.get_alert()
                if alert:
                    self.trigger_alert(alert.get('type', 'warning'))
                time.sleep(0.1)
        except Exception as e:
            print(f"Error in alert loop: {str(e)}")
        finally:
            GPIO.cleanup()