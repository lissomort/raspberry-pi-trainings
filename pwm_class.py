from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

class PWMMotor:
        """
        PWM DC Motor control class
        """

        # gpio_pwm is used for Generating Software PWM
        # gpio_in_1  & gpio_in_2 are used for Motor control pins as per schematic 
        def __init__(self, gpio_pwm, gpio_in_1, gpio_in_2):
                self.pwm_pin = gpio_pwm
                self.in1_pin = gpio_in_1
                self.in2_pin = gpio_in_2

                # PWMOutputDevice takes  BCM_PIN number
                # Active High 
                # Intial value
                # PWM Frequency
                # and Pin_factory which can be ignored

                self.pwm_pin_motor = PWMOutputDevice(self.pwm_pin, True, 0, 1200)

                # DigitalOutputDevice take 
                # Pin Number
                # Active High
                # Initial Value

                self.cw_pin = DigitalOutputDevice(self.in1_pin, True, 0)
                self.ccw_pin = DigitalOutputDevice(self.in2_pin, True, 0)


        def rotate_motor_cw(self, pwm_percnt):
                """
                Switch motor in CW direction with given pwn percentage
                """
                pwm_percnt = pwm_percnt/100.0
                self.pwm_pin_motor.value = pwm_percnt
                self.cw_pin.value = 1
                self.ccw_pin.value = 0


        def rotate_motor_ccw(self, pwm_percnt):
                """
                Switch motor in CCW direction with given pwn percentage
                """
                pwm_percnt = pwm_percnt/100.0
                self.pwm_pin_motor.value = pwm_percnt
                self.cw_pin.value = 0
                self.ccw_pin.value = 1


        def stop_motor(self):
                """
                Stop motor
                """
                self.cw_pin.value = 0
                self.ccw_pin.value = 0
                self.pwm_pin_motor.value = 0

def main():
        try:
                motor_test = PWMMotor(
                        gpio_pwm=13,
                        gpio_in_1=5,
                        gpio_in_2=6
                )
                while True:
                        motor_test.rotate_motor_cw(40)
                        sleep(4)
                        motor_test.rotate_motor_cw(60)
        except KeyboardInterrupt:
                print ('Interrupted')
        motor_test.stop_motor()

if __name__ == "__main__":
        main()