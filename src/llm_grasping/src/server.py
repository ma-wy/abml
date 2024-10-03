#!/usr/bin/env python3.8
import rospy
from math import pi
from llm_grasping.srv import RadianToAngle, RadianToAngleRequest, RadianToAngleResponse

class radian_to_angle_server:
  def __init__(self):
    self.radian_to_angle_server = rospy.Service('radian_to_angle', RadianToAngle, self.radian_to_angel_server_callback)
    print("Ready to convert radian to angle")
    
  def radian_to_angel_server_callback(self, req):
      res = RadianToAngleResponse()

      res.angle = 180.0 / pi * req.radian
      res.success = True

      print("request radian: %f, response angle: %f"%(req.radian, res.angle))

      return res


    
    

    

    

if __name__ == '__main__':
    rospy.init_node('radian_to_angle_server_node')
    s = radian_to_angle_server()
    rospy.spin()
