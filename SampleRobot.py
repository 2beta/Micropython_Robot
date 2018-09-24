"""
Project: Robot will follow a black line on floor
Author : Cedric Debetaz
Date : 2018 08 21
Version : 1.0
"""
#-----------------------------------------------------
from Robot import Scheduler, LineSensors, Motors
import time

myScheduler=Scheduler(250) # main loop executed every 250ms
myLineSensors=LineSensors()
myMotors = Motors()
i=0 # number of main loop done
#-----------------------------------------------------
"""
Init
"""
"""
print("Init started")
print("stop")
myMotors.stopAll()
time.sleep(2)

print("forward")
myMotors.forward(50)
time.sleep(2)

print("backward")
myMotors.backward(55)
time.sleep(2)

print("left")
myMotors.left(60)
time.sleep(2)

print("right")
myMotors.right(65)
time.sleep(2)

print("left_fast")
myMotors.left_fast(70)
time.sleep(2)

print("right_fast")
myMotors.right_fast(75)
time.sleep(2)

print("stop")
myMotors.stopAll()
time.sleep(1)
print("Init done")
"""

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
    """if position == LineSensors.ON_LEFT:
      myMotors.right(50)
    elif position == LineSensors.ON_RIGHT:
      myMotors.left(50)      
    elif position == LineSensors.ON_MIDDLE:
      myMotors.forward(50)
    else:
      myMotors.stopAll()"""

