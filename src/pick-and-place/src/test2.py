#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

'''
def get_joint_postions(ja, joint_names):
    joint_angles = r.joint_angles() # get current joint angles of the robot
    joint_positions = []
    for i in joint_names:
        joint_positions.append(joint_angles[i])
    return joint_positions
'''
if __name__ == '__main__':
    rospy.init_node("test_robot")
    r = ArmInterface() # 1420.5067157745361 ms
    joint_names = r.joint_names() # 0.0019073486328125 ms

    ratio = -1.0
    speed = 0.5
    
    r.move_to_neutral() #time: 4078.61590385437 ms
    
 #   joint_positions = r.get_joint_positions()
#    print(joint_positions)    
    
#    joint_positions = array(joint_positions) 
#    joint_positions[-1] = joint_positions[-1] - 0.5  *ratio 
#    joint_angles[joint_names[-1]] = joint_positions[-1]
    '''
    joint_angles = r.joint_angles()
    joint_angles[joint_names[-1]] = joint_angles[joint_names[-1]] - 0.5  *ratio 
    r.set_joint_position_speed(speed) 
    
    t1 = time.time() 
    r.move_to_joint_positions(joint_angles) 
    #speed = 0.2 time: 2982.105493545532 ms
    #speed = 0.3 time: 2160.2821350097656 ms
    #speed = 0.4 time: 1748.1935024261475 ms
    #speed = 0.5 time: 1503.8037300109863 ms 
    t2 = time.time()
    dt = d_time_ms(t1, t2)
#    print(r.endpoint_pose())
#    'position': array([0.30637234, 0.00694957, 0.48297631])
#    'orientation': quaternion(0.00303022918590906, -0.972014915648807, 0.23389726733686, 0.0216769416586322)
#    print(r.get_flange_pose())
#    array([0.31058317, 0.00528792, 0.58627606]),  
#    quaternion(-0.00549555892433902, -0.808512430161063, 0.58807187588126, 0.0211876828524569)
    pos = array([0.31058317, 0.00528792, 0.58627606])
    r.move_to_cartesian_pose(pos)
    pos = array([0.30637234, 0.00694957, 0.48297631])
#    r.move_to_cartesian_pose(pos)
    
    '''
    '''
    joint_angles = r.joint_angles()  
    # no move: 2 ms  
    while not rospy.is_shutdown():
        t1 = time.time()   
        r.set_joint_position_speed(speed)
        t2 = time.time()
        dt = d_time_ms(t1, t2)

     
    
    joint_angles = r.joint_angles() # get current joint angles of the robot
    joint_positions = []
    for i in joint_names:
        joint_positions.append(joint_angles[i])
    joint_positions = np.array(joint_positions) 
    joint_positions[-1] = joint_positions[-1] - 0.5   *ratio 
    joint_angles[joint_names[-1]] = joint_positions[-1]
    r.set_joint_position_speed(speed)
    r.move_to_joint_positions(joint_angles)
        
    joint_angles = r.joint_angles() # get current joint angles of the robot
    joint_positions = []
    for i in joint_names:
        joint_positions.append(joint_angles[i])
    joint_positions = np.array(joint_positions) 
    joint_positions[-1] = joint_positions[-1] - 0.5   *ratio 
    joint_angles[joint_names[-1]] = joint_positions[-1]
    r.set_joint_position_speed(speed)
    r.move_to_joint_positions(joint_angles)
    '''
    
    
    
    
