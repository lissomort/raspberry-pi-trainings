import RPi.GPIO as GPIO
import time
from adafruit_motor.motor import DCMotor

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT), # A1
GPIO.setup(37, GPIO.OUT), # A2
GPIO.setup(16, GPIO.OUT), # B1
GPIO.setup(18, GPIO.OUT), # B2

motor = DCMotor(35, 37) # AMotor

for i in range(1,3):
    motor.throttle(0.5)
    time.sleep(1)
    motor.throttle(None)


 