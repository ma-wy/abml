#!/usr/bin/env python
import rospy
from math import pi
from moveit_commander import MoveGroupCommander
from actionlib_msgs.msg import GoalStatusArray
from camera_opencv.msg import Command


def CommandCallback(data):  
    Command_voice = data.c;

    rospy.init_node('moveit_move')
    rospy.wait_for_message('move_group/status', GoalStatusArray)

    commander = MoveGroupCommander('panda_arm')
    commander.set_max_velocity_scaling_factor(0.7)
    commander.set_max_acceleration_scaling_factor(0.7)

    if Command_voice == 0:

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('open')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [0, 0, 0, -pi/2, 0, pi/2, pi/4]
        commander.go(joint_goal, wait=True)
        commander.go()

    if Command_voice == 1:

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.486, 0.811, 0.650, -1.923, -0.781, 2.476, 1.428]
        commander.go(joint_goal, wait=True)
        commander.go()

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('close')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.080, 0.749, 1.324, -1.622, -0.790, 1.708, 0.565]
        commander.go(joint_goal, wait=True)

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('open')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [0, 0, 0, -pi/2, 0, pi/2, pi/4]
        commander.go(joint_goal, wait=True)
        commander.go()


    if Command_voice == 2:

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.682, 0.807, 0.674, -1.954, -0.800, 2.487, 1.271]
        commander.go(joint_goal, wait=True)
        commander.go()

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('close')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.080, 0.749, 1.324, -1.622, -0.790, 1.708, 0.565]
        commander.go(joint_goal, wait=True)

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('open')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [0, 0, 0, -pi/2, 0, pi/2, pi/4]
        commander.go(joint_goal, wait=True)
        commander.go()

    if Command_voice == 3:

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.820, 0.816, 0.660, -1.925, -0.802, 2.477, 1.117]
        commander.go(joint_goal, wait=True)
        commander.go()

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('close')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [-0.080, 0.749, 1.324, -1.622, -0.790, 1.708, 0.565]
        commander.go(joint_goal, wait=True)

        commander = MoveGroupCommander('panda_hand')
        commander.set_named_target('open')
        commander.go()

        commander = MoveGroupCommander('panda_arm')
        joint_goal = [0, 0, 0, -pi/2, 0, pi/2, pi/4]
        commander.go(joint_goal, wait=True)
        commander.go()



if __name__ == '__main__':
    rospy.init_node('moveit_move')
    rospy.Subscriber("endo_camera/com", Command, CommandCallback)
    rospy.Rate(5)
    rospy.wait_for_message('move_group/status', GoalStatusArray)

    commander = MoveGroupCommander('panda_arm')
    commander.set_max_velocity_scaling_factor(0.7)
    commander.set_max_acceleration_scaling_factor(0.7)
    commander.set_named_target('ready')
    commander.go()
    commander = MoveGroupCommander('panda_hand')
    commander.set_named_target('open')
    commander.go()

    commander = MoveGroupCommander('panda_arm')
    joint_goal = [0, 0, 0, -pi/2, 0, pi/2, pi/4]
    commander.go(joint_goal, wait=True)
    # commander = MoveGroupCommander('panda_hand')
    # commander.set_named_target('close')
    commander.go()
    print('1111111')

    rospy.spin()
    print('22222222')


# commander = MoveGroupCommander('panda_arm')
# commander.set_pose_target([0.3,0,0.6,0.9,-0.38,1.3,3.2], end_effector_link="panda_link8")
## commander.set_position_target([0.5,0,0.5], end_effector_link="panda_link8")
# commander.go()

