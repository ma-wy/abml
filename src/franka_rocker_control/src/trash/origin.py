#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *


rospy.init_node('time_origin_pub', anonymous=True)
time_origin_pub = rospy.Publisher('/time_origin', Float32, queue_size=1)
t = Float32()
i = 0
while not rospy.is_shutdown():
  i += 1
  t.data = i
  time_origin_pub.publish(t)



