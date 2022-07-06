from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

# GPIO 13 is used for Generating Software PWM
# GPIO 5 & GPIO 6 are used for Motor control pins as per schematic 

PWM_PIN_MOT_LEFT = 13
IN1_PIN_MOT_LEFT = 5
IN2_PIN_MOT_LEFT = 6

# PWMOutputDevice takes  BCM_PIN number
# Active High 
# Intial value
# PWM Frequency
# and Pin_factory which can be ignored

pwm_pin_mot_left = PWMOutputDevice (PWM_PIN_MOT_LEFT, True, 0, 1200)

PWM_PIN_MOT2 = 12
IN1_PIN_MOT2 = 23
IN2_PIN_MOT2 = 24

# PWMOutputDevice takes  BCM_PIN number
# Active High 
# Intial value
# PWM Frequency
# and Pin_factory which can be ignored

pwm_pin_mot_left = PWMOutputDevice (PWM_PIN_MOT_LEFT, True, 0, 1200)
pwm_pin_mot_right = PWMOutputDevice (PWM_PIN_MOT2,True, 0, 1200)

# DigitalOutputDevice take 
# Pin Nuumber
# Active High
# Initial Value

cw_pin_mot_left = DigitalOutputDevice (IN1_PIN_MOT_LEFT, True, 0)
ccw_pin_mot_left = DigitalOutputDevice (IN2_PIN_MOT_LEFT, True, 0)

cw_pin_mot_right = DigitalOutputDevice (IN1_PIN_MOT2, True, 0)
ccw_pin_mot_right = DigitalOutputDevice (IN2_PIN_MOT2, True, 0)


def RotateMotorCW(pwm_percnt):
        """
        Switch motor in CW direction with given pwn percentage
        """
        pwm_percnt = pwm_percnt/100.0
        pwm_pin_mot_left.value = pwm_percnt
        cw_pin_mot_left.value = 1
        ccw_pin_mot_left.value = 0


def RotateMotorCCW(pwm_percnt):
        """
        Switch motor in CCW direction with given pwn percentage
        """
        pwm_percnt = pwm_percnt/100.0
        pwm_pin_mot_left.value = pwm_percnt
        cw_pin_mot_left.value = 0
        ccw_pin_mot_left.value = 1


def StopMotor():
        """
        Stop motor
        """
        cw_pin_mot_left.value = 0
        ccw_pin_mot_left.value = 0
        pwm_pin_mot_left.value = 0

def main():

        try:
            while True:
                RotateMotorCW()
                sleep(4)
                RotateMotorCCW()
        except KeyboardInterrupt:
                print ('Interrupted')
        StopMotor()

if __name__ == "__main__":
        main()