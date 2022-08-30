import Adafruit_PCA9685  
import time
pwm = Adafruit_PCA9685.PCA9685()  
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal  
while 1: # Make the servo connected to the No. 3 servo port on the Robot HAT reciprocate
    pwm.set_pwm(0, 0, 600)
    time.sleep(4)
    