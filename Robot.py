"""
Project : Library with tools for line tracking robot
Author : Cedric Debetaz
Date : 2018 08 21
Version 2.0
"""


import time
from machine import Pin, PWM

#--------------------------------------------------
class Scheduler:
  """
  Raise a bit every x ms, during 1 cycle
  """
  timeActual=time.ticks_ms()
  
  def __init__ (self, tempo):
    self.tempo = tempo # value of the scheduler
    self.timeOld = 0
    
  def update (self):
    """
    Return true during 1 cycle each x ms,
    false the rest of the time
    """
    Scheduler.timeActual=time.ticks_ms()
    
    if Scheduler.timeActual >= self.timeOld + self.tempo:
      self.timeOld = Scheduler.timeActual
      return True
    else:
      return False
      
      

#-----------------------------------------
class LineSensors:
  """ 
  Line sensors
  """
  WHITE = True
  BLACK = False
  
  UNKNOWN = 0
  ON_LEFT = 1
  ON_MIDDLE = 2
  ON_RIGHT = 3

  def __init__ (self, pin1=14, pin2=12, pin3=13):
    self.leftSensor = Pin(pin1, Pin.IN, Pin.PULL_UP)  # D5 / GPIO14
    self.middleSensor = Pin(pin2, Pin.IN, Pin.PULL_UP)  # D6 / GPIO12
    self.rightSensor = Pin(pin3, Pin.IN, Pin.PULL_UP)  # D7 / GPIO13
  
  def getPosition(self):  
    if self.leftSensor.value()==LineSensors.WHITE and self.middleSensor.value()==LineSensors.BLACK and self.rightSensor.value()==LineSensors.WHITE :
      return LineSensors.ON_MIDDLE
    if self.leftSensor.value()==LineSensors.BLACK and self.rightSensor.value()==LineSensors.WHITE :
      return LineSensors.ON_LEFT
    elif self.leftSensor.value()==LineSensors.WHITE and self.rightSensor.value()==LineSensors.BLACK:
      return LineSensors.ON_RIGHT
    else:
      return LineSensors.UNKNOWN
 
#------------------------------------------------------
class Motors:
  """
  2 DC Motors management,
  speed 0-100
  """
  def _speedConvertion (self, speed):
    # speed minimum 55 (on my robot motors)
    return int((speed*1023.0)/100.0)
  
  def __init__ (self, io1=5, io2=4, io3=0, io4=2):
    # nodemcu pins from the motor shield """
    self.pwm_A = PWM(Pin(io1), freq=750) # D1 PWM A
    self.pwm_B = PWM(Pin(io2), freq=750) # D2 PWM B
    self.direction_A = Pin(io3, Pin.OUT) # D3 Direction A
    self.direction_B = Pin(io4, Pin.OUT) # D4 Direction B   

  def stopAll(self):
    self.pwm_A.duty(0)
    self.pwm_B.duty(0)
    self.direction_A.value(0)
    self.direction_B.value(0)

  def backward(self, speed):
    self.pwm_A.duty(self._speedConvertion(speed))
    self.pwm_B.duty(self._speedConvertion(speed))
    self.direction_A.value(0)
    self.direction_B.value(0)

  def forward(self, speed):
    self.pwm_A.duty(self._speedConvertion(speed))
    self.pwm_B.duty(self._speedConvertion(speed))
    self.direction_A.value(1)
    self.direction_B.value(1)
    
  def left(self, speed):
    self.pwm_A.duty(self._speedConvertion(speed))
    self.pwm_B.duty(0)
    self.direction_A.value(0)
    self.direction_B.value(0)

  def right(self, speed):
    self.pwm_A.duty(0)
    self.pwm_B.duty(self._speedConvertion(speed))
    self.direction_A.value(0)
    self.direction_B.value(0)
  
  def left_fast(self, speed):
    self.pwm_A.duty(self._speedConvertion(speed))
    self.pwm_B.duty(self._speedConvertion(speed))
    self.direction_A.value(0)
    self.direction_B.value(1)

  def right_fast(self, speed):
    self.pwm_A.duty(self._speedConvertion(speed))
    self.pwm_B.duty(self._speedConvertion(speed))
    self.direction_A.value(1)
    self.direction_B.value(0)




