#!/usr/bin/env python

import sys
import time
import os
import roslib
import rospy

from people_msgs.msg import PositionMeasurementArray
from geometry_msgs.msg import *

'''
Testing reliability of leg detector

Empty environment:
What % of messages received from leg detector have (correct) person?
1) Stand still 2m, 4m directly in front (facing robot, not facing)
2) Walk a across field of view slowly (start 2m away, walk towards robot, walk from one side to the other)

In regular room:
What % of messages received from leg detector have (correct) person?
1) Stand still 2m, 4m directly in front (facing robot, not facing)
2) Walk a across field of view slowly (start 2m away, walk towards robot, walk from one side to the other)

(Optional)
In regular room:
When does Human Follower code set wrong goal (if person is showing)?
1) Same
2) Same

use wait for message!

'''


def timer():
	running = True
	counting = False
	countedTime = 0.0
	startTime = time.time()
	endTime = time.time()
	lastStamp = time.time()

	while (running):
		input = str(raw_input(">"))
		if (input == "q"):
			endTime = time.time()
			if (counting):
				# stop time
				countedTime += (endTime - lastStamp)
			
			print "stopped, total at: " + str(countedTime) + " / " + str(endTime-startTime)
			running = False
		else:
			counting = not counting
			# update the time
			
			if (counting == False):
				# updating time
				countedTime += (time.time() - lastStamp)
				print "paused, total at: " + str(countedTime) + " / " + str(time.time()-startTime)
			else:
				print "continue from: " + str(countedTime) + " / " + str(time.time()-startTime)

				lastStamp = time.time()
	# outside of loop
	print "total: " + str(countedTime) + "/" + str(endTime - startTime)
	return (countedTime, endTime-startTime)

def generateFileName(ex_type, dist = 0):
	''' generates the file name for this experiment
	    based on the type and the time
	'''
	filename = str(ex_type) + "_" + str(dist) + "_" + str(int(time.time())) + ".txt"
	return filename
        

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		print "usage: " + sys.argv[0] + " [env type: -s/-c] [optional: dist]"

	else:
		if (sys.argv[1] == "-s"):
			print "running tests in a simple environment"
			print generateFileName("s")
		elif (sys.argv[1] == "-c"):
			print "running tests in a complex environment"
			print generateFileName("c")
		else:
			print "invalid environment parameter. Use either '-s' or '-c' "
	timer()
    
