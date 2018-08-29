"""
Project : Library with tools for line tracking robot
Author : Cedric Debetaz
Date : 2018 08 21
Version 1.0
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
    return speed #int((speed*1023)/100)
  
  def __init__ (self, io1=5, io2=4, io3=0, io4=2):
      # nodemcu pins from the motor shield """
    pin1 = Pin(io1, Pin.OUT)  # D1
    pin2 = Pin(io2, Pin.OUT)  # D2
    pin3 = Pin(io3, Pin.OUT)  # D3
    pin4 = Pin(io4, Pin.OUT)  # D4

    # named after the L9110 h-bridge pins """
    self.BIN1 = PWM(pin1, freq=750)
    self.BIN2 = PWM(pin3, freq=750)
    self.AIN1 = PWM(pin2, freq=750)
    self.AIN2 = PWM(pin4, freq=750)

  def stopAll(self):
    for each in (self.BIN1, self.BIN2, self.AIN1, self.AIN2):
      each.duty(0)

  def backward(self, speed):
    self.BIN1.duty(0)
    self.BIN2.duty(self._speedConvertion(speed))
    self.AIN1.duty(0)
    self.AIN2.duty(self._speedConvertion(speed))

  def forward(self, speed):
    self.BIN1.duty(self._speedConvertion(speed))
    self.BIN2.duty(0)
    self.AIN1.duty(self._speedConvertion(speed))
    self.AIN2.duty(0)

  def left(self, speed):
    self.BIN1.duty(self._speedConvertion(speed))
    self.BIN2.duty(0)
    self.AIN1.duty(0)
    self.AIN2.duty(self._speedConvertion(speed))

  def right(self, speed):
    self.BIN1.duty(0)
    self.BIN2.duty(self._speedConvertion(speed))
    self.AIN1.duty(self._speedConvertion(speed))
    self.AIN2.duty(0)






