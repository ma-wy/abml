#!/usr/bin/env python3
from __future__ import print_function
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *


import threading

import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty

class PublishThread(threading.Thread):
    def __init__(self, rate):
        super(PublishThread, self).__init__()
        self.publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
        self.reset_pose_pub = rospy.Publisher('/if_reset', Int32, queue_size=1)
        self.if_gripper_close_pub = rospy.Publisher('/if_gripper_close', Int32, queue_size=1)
        self.if_gripper_open_pub = rospy.Publisher('/if_gripper_open', Int32, queue_size=1)
        self.gripper_pub = rospy.Publisher('/set_gripper', Float32, queue_size=1)
        self.speed = 0.0
        self.turn = 0.0
        self.condition = threading.Condition()
        self.done = False
        self.d_pose = zeros(6)
        self.if_reset = Int32()
        self.if_reset.data = 0
        self.set_gripper = Float32()
        self.set_gripper.data = None
        self.gripper_control = zeros(3)
        # Set timeout to None if rate is 0 (causes new_message to wait forever
        # for new data to publish)
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None

        self.start()
        
        pygame.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()




    def wait_for_subscribers(self):
        i = 0
        while not rospy.is_shutdown() and self.publisher.get_num_connections() == 0:
            if i == 4:
                print("Waiting for subscriber to connect to {}".format(self.publisher.name))
            rospy.sleep(0.5)
            i += 1
            i = i % 5
        if rospy.is_shutdown():
            raise Exception("Got shutdown request before subscribers connected")

    def update(self, d_pose, if_reset, gripper_control, speed, turn):
        self.condition.acquire()
        self.if_reset.data = if_reset
        self.gripper_control = gripper_control
        self.d_pose = d_pose
        self.speed = speed
        self.turn = turn
        # Notify publish thread that we have a new message.
        self.condition.notify()
        self.condition.release()
        settings = termios.tcgetattr(sys.stdin)

    def stop(self):
        self.done = True
        self.update(zeros(6), 0, zeros(3), 0, 0)
        self.join()

    def run(self):
        twist = Twist()
        if_gripper_open = Int32()
        if_gripper_close = Int32()
        set_gripper = Float32()
        while not self.done:
            self.condition.acquire()
            # Wait for a new message or timeout.
            self.condition.wait(self.timeout)

            # Copy state into twist message.
            twist.linear.x = self.d_pose[0]
            twist.linear.y = self.d_pose[1]
            twist.linear.z = self.d_pose[2]
            twist.angular.x = self.d_pose[3]
            twist.angular.y = self.d_pose[4]
            twist.angular.z = self.d_pose[5]

            self.condition.release()
            if_gripper_close.data = int(self.gripper_control[0])
            if_gripper_open.data = int(self.gripper_control[1])
            set_gripper.data = self.gripper_control[2]
            
            # Publish.
            
            self.publisher.publish(twist)
            self.reset_pose_pub.publish(self.if_reset)
            self.gripper_pub.publish(set_gripper)
            self.if_gripper_close_pub.publish(if_gripper_close)
            self.if_gripper_open_pub.publish(if_gripper_open)
            
        # Publish stop message when thread exits.
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        self.if_reset.data = 0
        if_gripper_close.data = self.gripper_control[0]
        if_gripper_open.data = self.gripper_control[1]
        set_gripper.data = self.gripper_control[2]
        self.publisher.publish(twist)
        self.reset_pose_pub.publish(self.if_reset)
        self.gripper_pub.publish(set_gripper)
        self.if_gripper_close_pub.publish(if_gripper_close)
        self.if_gripper_open_pub.publish(if_gripper_open)

    def getKey(self, key_timeout):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
        if rlist:
            key = sys.stdin.read(1)  
            print(sys.stdin)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key


def output_init():
    degree = zeros(6)
    direction = 0
    return degree, direction

def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('teleop_twist_keyboard')

    speed = rospy.get_param("~speed", 0.2)
    turn = rospy.get_param("~turn", 0.2)
    repeat = rospy.get_param("~repeat_rate", 0.0)
    key_timeout = rospy.get_param("~key_timeout", 0.0)
    
    
    
    
    if key_timeout == 0.0:
        key_timeout = None

    pub_thread = PublishThread(repeat)



    d_pose = zeros(6)
    d_p = 0.02 # m
    d_ra = 0.1 # rad
    degree, direction = output_init()
      
    reset_button = 13  
    if_reset = 0
    
    speed_button = [12, 10, 8, 9, 11]
    speed_list = ['home', 'p+', 'p-', 'r+', 'r-']
    speed_num = len(speed_button)
    speed_state = [0] * speed_num
    
    degree_button = [0,3,5,1,2,7]
    degree_list = ['x', 'y', 'z', 'p', 'a', 'r']
    degree_num = len(degree_list)
    degree_state = [0] * degree_num
    
    direction_list = ['+','-']
    axes_state = [0, 0]
    v = array([d_p, d_p, d_p, d_ra, d_ra, d_ra])
    
    gripper_button = [6,4]
    gripper_list = ['close', 'open']
    gripper_num = len(gripper_button)
    gripper_state = [0] * gripper_num
    gripper_control = zeros(3)
    set_gripper = 0
    
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    status = 0

    try:
        pub_thread.wait_for_subscribers()
        pub_thread.update(d_pose, if_reset, gripper_control, speed, turn)

        while not rospy.is_shutdown():   
            event_detect = pygame.event.get()
            if any(event_detect):
                for event in event_detect:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.JOYBUTTONDOWN:
                        if joystick.get_button(reset_button):
                            if_reset = 1    
                        else:
                            if_reset = 0
                        if joystick.get_button(gripper_button[0]):
                            set_gripper = 1.0
                            gripper_state[0] = 1
                        else:
                            gripper_state[0] = 0
                        if joystick.get_button(gripper_button[1]):
                            gripper_state[1] = 1
                            set_gripper = 0
                        else:
                            gripper_state[1] = 0
                        if all(gripper_state):    
                            gripper_state[0] = 0
                            gripper_state[1] = 0
                        for i in range(degree_num):
                            degree_state[i] = joystick.get_button(degree_button[i])
                        if any(degree_state):
                            d_pose = zeros(degree_num)
                            input_button = degree_list[degree_state.index(1)]
                            print('degree')
                            print(input_button)
                            degree = get_control_degree(input_button)
                            direction = 0
                            
                        for i in range(speed_num):
                            speed_state[i] = joystick.get_button(speed_button[i])
                        if any(speed_state):    
                            if speed_state[0]:
                                d_p = 0.01 # m
                                d_ra = 0.01          
                            elif speed_state[1]:
                                d_p *= 1.5
                            elif speed_state[2]:
                                d_p *= 0.8
                            elif speed_state[3]:    
                                d_ra *= 1.5
                            elif speed_state[4]:    
                                d_ra *= 0.8
                            v = array([d_p, d_p, d_p, d_ra, d_ra, d_ra])
                            speed_state = [0]*speed_num
                            
                            
                # detect axix state    
                if joystick.get_axis(0) < 0.1 and joystick.get_axis(0) > 0:
                   axes_state[0] = 0
                else:
                   axes_state[0] = 1
                if joystick.get_axis(1) < 0.1 and joystick.get_axis(1) > 0:
                   axes_state[1] = 0
                else:
                   axes_state[1] = 1            
                  
            #      print('set mode to LS')  
                if any(axes_state):   
                    if joystick.get_axis(1) < -0.9:
                        direction = 1.0
                    elif joystick.get_axis(1) > 0.9:
                        direction = -1.0
                else:     
                    direction = 0.0
                gripper_control[0] = gripper_state[0]
                gripper_control[1] = gripper_state[1]
                gripper_control[2] = set_gripper   
                d_pose = direction * degree * v       
                '''
                key = pub_thread.getKey(key_timeout)
                if key in speedBindings.keys():
                    speed = speed * speedBindings[key][0]
                    turn = turn * speedBindings[key][1]

                    print(vels(speed,turn))
                    if (status == 14):
                        print(msg)
                    status = (status + 1) % 15
                   
                else:
                    # Skip updating cmd_vel if key timeout and robot already
                    # stopped.
                    if key == '':# and x == 0 and y == 0 and z == 0 and p == 0 and a == 0 and r == 0:
                        continue
                    d_pose = zeros(6)    
                #    if (key == '\x03'):
                #        break
                '''
                pub_thread.update(d_pose, if_reset, gripper_control, speed, turn)

    except Exception as e:
        print(e)

    finally:
        pub_thread.stop()

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
