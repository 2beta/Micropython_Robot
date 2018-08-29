"""
Project: Robot will follow a black line on floor
Author : Cedric Debetaz
Date : 2018 08 21
Version : 1.0
"""
#-----------------------------------------------------
from MyLibrary import Scheduler, LineSensors, Motors
import time

myScheduler=Scheduler(250) # main loop executed every 250ms
myLineSensors=LineSensors()
myMotors = Motors()
i=0 # number of main loop done
#-----------------------------------------------------
"""
Init
"""
print("Init started")
myMotors.stopAll()
time.sleep(1)
myMotors.forward(50)
time.sleep(1)
myMotors.backward(50)
time.sleep(1)
myMotors.stopAll()
time.sleep(1)
print("Init done")

"""
Main loop
"""
print("Main loop")
while True:
  tick = myScheduler.update()
  if tick:
    i+=1
    print ("It's time, #{}".format(i))
    #---------------------------------------
    position = myLineSensors.getPosition()
    print("Position = {}".format(position))
    if position == LineSensors.ON_LEFT:
      myMotors.right(50)
    elif position == LineSensors.ON_RIGHT:
      myMotors.left(50)      
    elif position == LineSensors.ON_MIDDLE:
      myMotors.forward(50)
    else:
      myMotors.stopAll()

