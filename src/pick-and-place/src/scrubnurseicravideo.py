#!/usr/bin/env python3.8
import rospy
import time
from math import pi
from moveit_commander import MoveGroupCommander
from actionlib_msgs.msg import GoalStatusArray

from std_msgs.msg import Int64


rospy.init_node('moveit_move')
rospy.wait_for_message('move_group/status', GoalStatusArray)
pub_gripper = rospy.Publisher('/value_topic', Int64, queue_size=10)

commander = MoveGroupCommander('panda_arm')
commander.set_max_velocity_scaling_factor(0.5)
commander.set_max_acceleration_scaling_factor(0.5)



commander.set_named_target('ready')
commander.go()


commander = MoveGroupCommander('panda_arm')
joint_goal = [0.338380620839303, 0.5052951123337996, 0.04423710695170519, -2.536839071135732, -0.08056383111038141, 2.9986641362303863, 1.2747214452214537]
commander.go(joint_goal, wait=True)

pub_gripper.publish(1)

time.sleep(6)

commander = MoveGroupCommander('panda_arm')
joint_goal = [0.043272458575273814, 0.25180870409179146, 1.3511670450810485, -1.8739070427785114, -0.27406981148322423, 1.9320121403229271, 0.6597979882209727]
commander.go(joint_goal, wait=True)

pub_gripper.publish(-1)

time.sleep(6)


commander.set_named_target('ready')
commander.go()

time.sleep(8)



commander = MoveGroupCommander('panda_arm')
joint_goal = [0.04180559199264174, 0.4853570438811653, -0.03823348811768233, -2.642052335425308, -0.08576499274365584, 3.1131079056792785, 0.843532938122568]
commander.go(joint_goal, wait=True)

pub_gripper.publish(1)

time.sleep(6)

commander = MoveGroupCommander('panda_arm')
joint_goal = [0.043272458575273814, 0.25180870409179146, 1.3511670450810485, -1.8739070427785114, -0.27406981148322423, 1.9320121403229271, 0.6597979882209727]
commander.go(joint_goal, wait=True)

pub_gripper.publish(-1)

time.sleep(6)


commander.set_named_target('ready')
commander.go()
