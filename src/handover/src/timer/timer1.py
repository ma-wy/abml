#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

def main(args):
  rospy.init_node('timer1', anonymous=True)

  timer = rospy.Publisher("/timer1", Float32, queue_size=1)
  t = Float32()
  while not rospy.is_shutdown():
    t.data = time.time()
    timer.publish(t)
      
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
if __name__ == '__main__':

    main(sys.argv)
    
    
