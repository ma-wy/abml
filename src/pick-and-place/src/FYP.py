#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2013, SRI International
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of SRI International nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Acorn Pooley, Mike Lautman

## BEGIN_SUB_TUTORIAL imports
##
## To use the Python MoveIt interfaces, we will import the `moveit_commander`_ namespace.
## This namespace provides us with a `MoveGroupCommander`_ class, a `PlanningSceneInterface`_ class,
## and a `RobotCommander`_ class. More on these below. We also import `rospy`_ and some messages that we will use:
##

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

import numpy as np
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion
import yaml
import serial
from std_msgs.msg import Int64
from message.msg import Position, gripper
import time
from moveit_commander import MoveGroupCommander


try:
    from math import pi, tau, dist, fabs, cos, sin, acos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt, sin, acos

    tau = 2.0 * pi
    
    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

## END_SUB_TUTORIAL
#arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.2)
#ser_dat=''
# hand_eye_mat = np.array([[ 0.2566176,  0.8527198, -0.4549904,  0.9383670417113285],
#  [ 0.9633036, -0.2639844,  0.0485635,  0.10513935474444507],
#  [ -0.0786993, -0.4507561, -0.8891712,  0.5363258560366873],
#  [ 0.,          0.,          0.,          1.        ]])

hand_eye_mat = np.array([[ 0.1030738,  0.9359201, -0.3367926,  0.8019755923219894],
 [ 0.9864399, -0.0527058,  0.1554300,  -0.16134546108201062],
 [ 0.1277191, -0.3482465, -0.9286615,  0.9858482222513281],
 [ 0.,          0.,          0.,          1.        ]])




def all_close(goal, actual, tolerance):
    """
    Convenience method for testing if the values in two lists are within a tolerance of each other.
    For Pose and PoseStamped inputs, the angle between the two quaternions is compared (the angle
    between the identical orientations q and -q is calculated correctly).
    @param: goal       A list of floats, a Pose or a PoseStamped
    @param: actual     A list of floats, a Pose or a PoseStamped
    @param: tolerance  A float
    @returns: bool
    """
    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        x0, y0, z0, qx0, qy0, qz0, qw0 = pose_to_list(actual)
        x1, y1, z1, qx1, qy1, qz1, qw1 = pose_to_list(goal)
        # Euclidean distance
        d = dist((x1, y1, z1), (x0, y0, z0))
        # phi = angle between orientations
        cos_phi_half = fabs(qx0 * qx1 + qy0 * qy1 + qz0 * qz1 + qw0 * qw1)
        return d <= tolerance and cos_phi_half >= cos(tolerance / 2.0)

    return True

class MoveGroupPythonInterfaceTutorial(object):
    """MoveGroupPythonInterfaceTutorial"""

    def __init__(self):
        super(MoveGroupPythonInterfaceTutorial, self).__init__()
        rospy.init_node('FYP', anonymous=True)





        ## BEGIN_SUB_TUTORIAL setup
        ##
        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        group_name = "panda_arm"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )

        ## END_SUB_TUTORIAL

        ## BEGIN_SUB_TUTORIAL basic_info
        ##
        ## Getting Basic Information
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^
        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)

        # We can also print the name of the end-effector link for this group:
        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)

        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")
        ## END_SUB_TUTORIAL
        # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

    def init_pose(self):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        move_group = self.move_group

        ## BEGIN_SUB_TUTORIAL plan_to_pose
        ##
        ## Planning to a Pose Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## We can plan a motion for this group to a desired pose for the
        ## end-effector:
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 0.0005491024859655507
        pose_goal.orientation.x = -0.924000369012121
        pose_goal.orientation.y = 0.3823902179086942
        pose_goal.orientation.z = -0.0008589526561981145
        pose_goal.position.x = 0.30698300028512676
        pose_goal.position.y = 0.00019364303046238626
        pose_goal.position.z = 0.590763729842274
        waypoints = []
        waypoints.append(copy.deepcopy(pose_goal))
        (cartesian_plan, fraction) = move_group.compute_cartesian_path(
            waypoints, 0.01, 0.00  # waypoints to follow  # eef_step
        )
        cartesian_plan = move_group.retime_trajectory(moveit_commander.RobotCommander().get_current_state(), 
                                                 cartesian_plan, 
                                                 0.07)
        self.move_group.execute(cartesian_plan, wait=True)

    def plan_cartesian_path(self, x, y, z, theta, scale=1):
        axis = [sin(theta), cos(theta), 0.0]
        w = cos(pi / 2)
        x2 = axis[0] * sin(pi / 2.0)
        y2 = axis[1] * sin(pi / 2.0)
        z2 = axis[2] * sin(pi / 2.0)
        move_group = self.move_group
        waypoints = []          
        wpose = self.move_group.get_current_pose().pose
        wpose.orientation.w = w
        wpose.orientation.x = x2
        wpose.orientation.y = y2
        wpose.orientation.z = z2
        wpose.position.z = scale * z  # First move up (z)
        wpose.position.y = scale * y  # and sideways (y)
        wpose.position.x = scale * x  # and forward (x)

        
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (cartesian_plan, fraction) = move_group.compute_cartesian_path(
            waypoints, 0.01, 0.00  # waypoints to follow  # eef_step
        )  # jump_threshold
        cartesian_plan = self.move_group.retime_trajectory(moveit_commander.RobotCommander().get_current_state(), 
                                                 cartesian_plan, 
                                                 0.07)
        # Note: We are just planning, not asking move_group to actually move the robot yet:
        return cartesian_plan

        ## END_SUB_TUTORIAL

    def display_trajectory(self, plan):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        robot = self.robot
        display_trajectory_publisher = self.display_trajectory_publisher

        ## BEGIN_SUB_TUTORIAL display_trajectory
        ##
        ## Displaying a Trajectory
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## You can ask RViz to visualize a plan (aka trajectory) for you. But the
        ## group.plan() method does this automatically so this is not that useful
        ## here (it just displays the same trajectory again):
        ##
        ## A `DisplayTrajectory`_ msg has two primary fields, trajectory_start and trajectory.
        ## We populate the trajectory_start with our current robot state to copy over
        ## any AttachedCollisionObjects and add our plan to the trajectory.
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        # Publish
        display_trajectory_publisher.publish(display_trajectory)

        ## END_SUB_TUTORIAL

    def execute_plan(self, plan):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        move_group = self.move_group
        self.display_trajectory(plan)
        move_group.execute(plan, wait=True)
    
    def move_to(self, x, y, z, theta):
        plan = plan_cartesian_path(x, y, z, theta)
        execute_plan(plan)
    def receive():
        data = arduino.read().decode('utf-8')
        return data

class Comm(object):
    def __init__(self):
        super(Comm, self).__init__()
        self.receiver=receiver()
        self.next_step=next_step()
        self.Gripper=Gripper()
        
    def receiver():
        while True:
            try:
                data = rospy.wait_for_message("pos", Quaternion, timeout = None)
                return data
            except KeyboardInterrupt:
                return None
    '''            
    def ard_receive():
        while True:
            try:
                data = arduino.read().decode('utf-8')
                if data == 'a':
                    return
            except KeyboardInterrupt:
                return None
    def Gripper():
        arduino.write(str(1).encode())
        rec = Comm.ard_receive()
    '''    
    	
    

def main():
    print("Press Enter to start")
    input()
    #Comm.Gripper()
    real_vec = np.zeros((1,4)).astype(float)
    try:
        robot = MoveGroupPythonInterfaceTutorial()
        #Publisher Yisen
        pub_gripper = rospy.Publisher('/value_topic', Int64, queue_size=10)

        commander_s = MoveGroupCommander("panda_arm")
        commander_s.set_max_velocity_scaling_factor(0.5)
        commander_s.set_max_acceleration_scaling_factor(0.5)

        while 1:
            print("Back to initial position...")
            commander_s.set_named_target('ready')
            commander_s.go()

            # robot.init_pose()
            print("Initialize Done")
            data = Comm.receiver()
            print(data)
            scale = 0.001
            tvec = np.array(((data.x)*scale, (data.y)*scale, (data.z)*scale, 1)).astype(float)
            real_vec = np.matmul(hand_eye_mat, tvec)
            print(real_vec)
            plan = robot.plan_cartesian_path(real_vec[0], real_vec[1], real_vec[2]+0.125, 1.96)
            robot.display_trajectory(plan)
            input()
            robot.execute_plan(plan)

            # gripper close
            pub_gripper.publish(1)
            time.sleep(3)

            # move to the surgeon

            joint_goal = [0.043272458575273814, 0.25180870409179146, 1.3511670450810485, -1.8739070427785114, -0.27406981148322423, 1.9320121403229271, 0.6597979882209727]
            commander_s.go(joint_goal, wait=True)

            # gripper open
            pub_gripper.publish(-1)
            time.sleep(3)



            #Comm.Gripper()
            # plan2 = robot.plan_cartesian_path(0.27709698223598644, -0.4657871897313535, 0.3949813943525625, 2.6)
            # robot.display_trajectory(plan2)
            # robot.execute_plan(plan2)
            #Comm.Gripper()
        
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        pass
        

## BEGIN_TUTORIAL
## .. _moveit_commander:
##    http://docs.ros.org/noetic/api/moveit_commander/html/namespacemoveit__commander.html
##
## .. _MoveGroupCommander:
##    http://docs.ros.org/noetic/api/moveit_commander/html/classmoveit__commander_1_1move__group_1_1MoveGroupCommander.html
##
## .. _RobotCommander:
##    http://docs.ros.org/noetic/api/moveit_commander/html/classmoveit__commander_1_1robot_1_1RobotCommander.html
##
## .. _PlanningSceneInterface:
##    http://docs.ros.org/noetic/api/moveit_commander/html/classmoveit__commander_1_1planning__scene__interface_1_1PlanningSceneInterface.html
##
## .. _DisplayTrajectory:
##    http://docs.ros.org/noetic/api/moveit_msgs/html/msg/DisplayTrajectory.html
##
## .. _RobotTrajectory:
##    http://docs.ros.org/noetic/api/moveit_msgs/html/msg/RobotTrajectory.html
##
## .. _rospy:
##    http://docs.ros.org/noetic/api/rospy/html/
## CALL_SUB_TUTORIAL imports
## CALL_SUB_TUTORIAL setup
## CALL_SUB_TUTORIAL basic_info
## CALL_SUB_TUTORIAL plan_to_joint_state
## CALL_SUB_TUTORIAL plan_to_pose
## CALL_SUB_TUTORIAL plan_cartesian_path
## CALL_SUB_TUTORIAL display_trajectory
## CALL_SUB_TUTORIAL execute_plan
## CALL_SUB_TUTORIAL add_box
## CALL_SUB_TUTORIAL wait_for_scene_update
## CALL_SUB_TUTORIAL attach_object
## CALL_SUB_TUTORIAL detach_object
## CALL_SUB_TUTORIAL remove_object
## END_TUTORIAL
