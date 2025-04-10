#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *


def main(args):
  rospy.init_node('gripper_open', anonymous=True)

  gripper_move_client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)
  gripper_move_client.wait_for_server()  
  print('open the gripper')
  b = franka_open_gripper(client=gripper_move_client, width=0.008, speed=0.1)
  print(b)
  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)


    
    
    
    
