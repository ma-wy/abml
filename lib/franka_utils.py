#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#import sys 
#sys.path.append("/home/abml/zoe_ws/lib")
#from mwy_lib import *


'''
@author: mwy
'''
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *


def franka_open_gripper(client=actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction), width=0.025, speed=0.1):
  gripper_move_client = client
#  gripper_move_client.wait_for_server()  
  gripper_open = franka_gripper.msg.MoveGoal()
  gripper_open.width = width
  gripper_open.speed = speed
  gripper_move_client.send_goal(gripper_open)
  gripper_move_client.wait_for_result()
  return gripper_move_client.get_result().success

def franka_close_gripper(client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction), speed=0.1):
  gripper_grasp_client = client
#  gripper_grasp_client.wait_for_server()  
  gripper_close = franka_gripper.msg.GraspGoal()
  gripper_close.width = 0.055
  print(gripper_close.width)
  gripper_close.epsilon.inner = 0.01
  gripper_close.epsilon.outer = 0.01
  gripper_close.speed = 0.1
  gripper_close.force = 0
  gripper_grasp_client.send_goal(gripper_close)
  gripper_grasp_client.wait_for_result()
  return gripper_grasp_client.get_result().success

def franka_close_gripper_black(client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction), speed=0.1):
  gripper_grasp_client = client
#  gripper_grasp_client.wait_for_server()  
  gripper_close = franka_gripper.msg.GraspGoal()
  gripper_close.width = 0.01
  print(gripper_close.width)
  gripper_close.epsilon.inner = 0.1
  gripper_close.epsilon.outer = 0.1
  gripper_close.speed = 0.1
  gripper_close.force = 1
  gripper_grasp_client.send_goal(gripper_close)
  gripper_grasp_client.wait_for_result()
  return gripper_grasp_client.get_result().success

def franka_homing_gripper(client = actionlib.SimpleActionClient('/franka_gripper/homing', franka_gripper.msg.HomingAction)):
  gripper_homing_client = client
#  gripper_homing_client.wait_for_server()  
  gripper_homing = franka_gripper.msg.HomingGoal()
  gripper_homing_client.send_goal(gripper_homing)
  gripper_homing_client.wait_for_result()
  return gripper_homing_client.get_result().success  



