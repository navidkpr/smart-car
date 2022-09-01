import time
from tkinter import N
import RPi.GPIO as GPIO
from smart_car.keyboard import Key, getKey

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

pwn_A = 0
pwm_B = 0

def motorStop():#Motor stops
  GPIO.output(Motor_A_Pin1, GPIO.LOW)
  GPIO.output(Motor_A_Pin2, GPIO.LOW)
  GPIO.output(Motor_B_Pin1, GPIO.LOW)
  GPIO.output(Motor_B_Pin2, GPIO.LOW)
  GPIO.output(Motor_A_EN, GPIO.LOW)
  GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():#Motor initialization
  global pwm_A, pwm_B
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Motor_A_EN, GPIO.OUT)
  GPIO.setup(Motor_B_EN, GPIO.OUT)
  GPIO.setup(Motor_A_Pin1, GPIO.OUT)
  GPIO.setup(Motor_A_Pin2, GPIO.OUT)
  GPIO.setup(Motor_B_Pin1, GPIO.OUT)
  GPIO.setup(Motor_B_Pin2, GPIO.OUT)

  motorStop()
  try:
    pwm_A = GPIO.PWM(Motor_A_EN, 1000)
    pwm_B = GPIO.PWM(Motor_B_EN, 1000)
  except:
    pass


def motor_A(status, speed): # Motor A positive and negative rotation.
  direction: str = "none"
  if status == 1:
      direction = "forward"
  elif status == -1:
      direction = "backward"
  print('Moving motor A in direction {}'.format(direction))
  if status == 0: # stop
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)
  elif status == 1:                       # positive rotation.
      GPIO.output(Motor_B_Pin1, GPIO.HIGH)
      GPIO.output(Motor_B_Pin2, GPIO.LOW)
      pwm_B.start(100)
      pwm_B.ChangeDutyCycle(speed)
  elif status == -1:                      # negative rotation.
      GPIO.output(Motor_B_Pin1, GPIO.LOW)
      GPIO.output(Motor_B_Pin2, GPIO.HIGH)
      pwm_B.start(0)
      pwm_B.ChangeDutyCycle(speed)
      

def motor_B(status, speed):            # Motor B positive and negative rotation.
  direction = "none"
  if status == 1:
      direction = "forward"
  elif status == -1:
      direction = "backward"
  print('Moving motor B in direction {}'.format(direction))
  if status == 0: # stop
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
  elif status == 1:                       # positive rotation.
      GPIO.output(Motor_A_Pin1, GPIO.HIGH)
      GPIO.output(Motor_A_Pin2, GPIO.LOW)
      pwm_A.start(100)
      pwm_A.ChangeDutyCycle(speed)
  elif status == -1:                      # negative rotation.
      GPIO.output(Motor_A_Pin1, GPIO.LOW)
      GPIO.output(Motor_A_Pin2, GPIO.HIGH)
      pwm_A.start(0)
      pwm_A.ChangeDutyCycle(speed)



def move(): 
  while (1):
    key: Key = getKey()
    if key == Key.Up:
        print('moving forward')
        motor_A(1, 100)
        motor_B(1, 100)
    elif key == Key.Down:
        print('moving backward')
        motor_A(-1, 100)
        motor_B(-1, 100)
    else:
        print('stop')
        break
        # motor_A(0, speed)
        # motor_B(0, speed)
    # else:
    #   pass

def destroy():
  motorStop()
  GPIO.cleanup()             # Release resource


if __name__ == '__main__':
  try:
    while True:
      # speed_set = 60
      setup()
      move()
      # motorStop()
      # move(speed_set, 'forward')
      # motorStop()
      # move(speed_set, 'backward')
      # time.sleep(3)
      # motorStop()
      # time.sleep(1.5)
  except KeyboardInterrupt:
    destroy()
