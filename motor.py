import time
import RPi.GPIO as GPIO

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
  direction = "none"
  if status == 1:
      directoin = "forward"
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
      directoin = "forward"
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



def move(speed, direction): 
  #speed = 100
  if direction == 'forward':
      print('moving forward')
      motor_A(1, speed)
      motor_B(1, speed)
  elif direction == 'backward':
      print('moving backward')
      motor_A(-1, speed)
      motor_B(-1, speed)
  elif direction == 'stop':
      print('stop')
      motor_A(0, speed)
      motor_B(0, speed)
  else:
    pass

def destroy():
  motorStop()
  GPIO.cleanup()             # Release resource


if __name__ == '__main__':
  try:
    while True:
      speed_set = 60
      setup()
      move(speed_set, 'forward')
      time.sleep(3)
      motorStop()
      time.sleep(1.5)
      move(speed_set, 'backward')
      time.sleep(3)
      motorStop()
      time.sleep(1.5)
  except KeyboardInterrupt:
    destroy()
