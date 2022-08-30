import time
import RPi.GPIO as GPIO

Motor_A_EN = 11

Motor_A_Pin1 = 13
Motor_A_Pin2 = 12

def motorStop():
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    GPIO.output(MOTOR_A_EN, GPIO.LOW)


def setup():#Motor initialization  
    global pwm_A
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)  
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    motorStop()  
    try:  
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)  
    except:  
        pass  
def destroy():  
    motorStop()
    GPIO.cleanup()

def move(speed, direction, turn, radius=0.6):   # 0 < radius <= 1    
    #speed = 100  
    if direction == 'forward':  
        if turn == 'right':  
            motor_left(0, left_backward, int(speed*radius))  
            motor_right(1, right_forward, speed)  
        elif turn == 'left':  
            motor_left(1, left_forward, speed)  
            motor_right(0, right_backward, int(speed*radius))  
        else:  
            motor_left(1, left_forward, speed)  
            motor_right(1, right_forward, speed)  
    else:  
        pass  

if __name__ == "__main__":
    try:
        speed_set = 60  
        setup()  
        move(speed_set, 'forward', 'no', 0.8)  
        time.sleep(1.3)  
        motorStop()  
        destroy()  
    except KeyboardInterrupt:  
        destroy()  