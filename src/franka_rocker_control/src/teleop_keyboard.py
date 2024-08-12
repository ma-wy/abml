#!/usr/bin/env python3
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

import rospy
import math
import numpy as np
import time
from geometry_msgs.msg import PoseStamped, Pose, Twist
from pynput.keyboard import Listener
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose
from panda import Panda



class TeleopKeyboard(Panda):
    """
    A class that allows a user to control the cartesian pose of the Franka Emika robots through 
    a key board, that builds on top of the funcionality provided by the `Panda` class,
    which provides an interface to the Franka Emika robots. This is done through the `teleop_twist_keyboard`
    package.
    """
    def __init__(self):
        # start up a ROS node
        rospy.init_node("teleop_node")
        super(TeleopKeyboard, self).__init__()

        # Set the node frequency - twice the frequency of the /key_vel topic
        self.r=rospy.Rate(20)
        
        # Variable to store the current key value.
        self.key_value = None
        self.if_reset = 0
        self.set_gripper = 0
        self.if_gripper_close = 0
        self.if_gripper_open = 0
        # Subscriber to keyboard from teleop_twist_keyboard package
        self.key_sub=rospy.Subscriber("/cmd_vel", Twist, self.keyboard_read_callback)
        self.if_reset_sub=rospy.Subscriber("/if_reset", Int32, self.if_reset_callback)
        self.gripper_sub=rospy.Subscriber("/set_gripper", Float32, self.gripper_callback)
        self.if_gripper_close_sub = rospy.Subscriber('/if_gripper_close', Int32, self.if_gripper_close_callback)
        self.if_gripper_open_sub = rospy.Subscriber('/if_gripper_open', Int32, self.if_gripper_open_callback)
        
        # Amount to move the robot 
        self.move_distance = 0.01 
        # This funciton is needed to keep the node running 
        rospy.spin()

    def if_gripper_close_callback(self, data):
        self.if_gripper_close = data.data
        
    def if_gripper_open_callback(self, data):
        self.if_gripper_open = data.data

    def gripper_callback(self, data):
        self.set_gripper = data.data

    def if_reset_callback(self, data):
        self.if_reset = data.data


    def keyboard_read_callback(self, key_input):
        """
        Callback function that changes the robots end effector cartesian pose when 
        one of the arrow keys are pressed. It changes the equilibrium pose by 1mm, given the key pressed
        and direction assigned to that key.
        """
        self.key_value = key_input
        print(self.key_value) 

        # X axis position
        
        if self.if_reset:
            goal = self.reset_ee_pose
            self.goal_pub.publish(goal)
            self.if_reset = 0
          
        if self.if_gripper_open:
            width = 0
            self.move_gripper(width)  
            self.if_gripper_open = 0
            
        if self.if_gripper_close:
            width = 1
            self.move_gripper(width)  
            self.if_gripper_close = 0
            
        if self.key_value.linear.x or self.key_value.linear.y or self.key_value.linear.z:
            # Set this to the current value as it needs some orientation value to publish to /equilibrium_pose
            d_p = np.array([self.key_value.linear.x, self.key_value.linear.y, self.key_value.linear.z])
            quat_goal = list_2_quaternion(self.curr_ori)
            posi_goal = self.curr_pos + d_p
            goal = array_quat_2_pose(posi_goal, quat_goal)
            self.goal_pub.publish(goal)
            self.key_value.linear.x = 0.0 
            self.key_value.linear.y = 0.0 
            self.key_value.linear.z = 0.0
        
        # X axis rotation
        elif self.key_value.angular.x or self.key_value.angular.y or self.key_value.angular.z:
            # Set this to the current value as it needs some orientation value to publish to /equilibrium_pose
            posi_goal = self.curr_pos
            d_ra = [self.key_value.angular.x, self.key_value.angular.y, self.key_value.angular.z]
            d_q = angle_axis_to_q(d_ra)
            q_curr = self.curr_q
            q_temp = transformation_Q(q_curr,d_q)
            quat_goal = list_2_quaternion([q_temp[3], q_temp[0], q_temp[1], q_temp[2]])
            goal = array_quat_2_pose(posi_goal, quat_goal)#
            self.goal_pub.publish(goal)
            self.key_value.angular.x = 0.0
            self.key_value.angular.y = 0.0
            self.key_value.angular.z = 0.0


def main(args):
    teleop_panda = TeleopKeyboard()
    
if __name__ == '__main__':

    main(sys.argv)
  























