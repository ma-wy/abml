#!/usr/bin/env python3.8
'''
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
'''
import rospy
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import PoseStamped
from numpy import *
import tf

def get_PoseStamped(posestamped):
  pose = [posestamped.pose.position.x, 
    posestamped.pose.position.y, 
    posestamped.pose.position.z, 
    posestamped.pose.orientation.x,
    posestamped.pose.orientation.y,
    posestamped.pose.orientation.z,
    posestamped.pose.orientation.w]
  return pose
  
def get_tf(frame_p, frame_ch):
  listener = tf.TransformListener() 
  listener.waitForTransform(frame_p, frame_ch, rospy.Time(), rospy.Duration(4.0))
  (p,q) = listener.lookupTransform(frame_p, frame_ch, rospy.Time(0))
  return p, q
  
def give_PoseStamped(frame, q, p):
  pose = PoseStamped()
  pose.header.frame_id = frame
  pose.header.stamp = rospy.Time.now()
  pose.pose.orientation.x = q[0]
  pose.pose.orientation.y = q[1]
  pose.pose.orientation.z = q[2]
  pose.pose.orientation.w = q[3]
  pose.pose.position.x = p[0]
  pose.pose.position.y = p[1]
  pose.pose.position.z = p[2]
  return pose

def get_PoseStamped(posestamped):
  pose = [posestamped.pose.position.x, 
    posestamped.pose.position.y, 
    posestamped.pose.position.z, 
    posestamped.pose.orientation.x,
    posestamped.pose.orientation.y,
    posestamped.pose.orientation.z,
    posestamped.pose.orientation.w]
  return pose

def transformation_Q(q_orig,q_rot):
  q_new = tf.transformations.quaternion_multiply(q_rot,q_orig)
  return array(q_new)
  
def deg_to_rad(joints):
  if type(joints) is list or array:
    for i in range(len(joints)):
      joints[i] = float(joints[i])/180.0 * pi
    return joints   
  else:
    return float(joints)/180.0 * pi  

def angle_axis_to_q_complex(axis = "z", angle = 5, angle_type = "degree"):
  if axis == "x":
    r = [1,0,0]
  elif axis == "y":
    r = [0,1,0]
  elif axis == "z":
    r = [0,0,1]
  else:
    print("Please input x, y, z to select a rotation axis.")
    
  if angle_type == "degree":
    a = float(angle)/180.0 * pi
  elif not angle_type == "rad":
    print("Please set angle_type as degree or rad.")
    
  R = tf.transformations.rotation_matrix(a, r)      
  q = tf.transformations.quaternion_from_matrix(R) 
  return q

def rotation_between_2v(v1, v2):
  vec1 = v1
  vec2 = v2
  angle = arccos(dot(vec1,vec2)/(linalg.norm(vec1)*linalg.norm(vec2)))
  axis = cross(vec1,vec2)
  q = tf.transformations.quaternion_about_axis(angle, axis)
  return q

####################################################################
rospy.init_node("test_moveit_orientation", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link("panda_hand")
frame = "panda_link0"
rob.set_max_velocity_scaling_factor(0.3)
rob.set_max_acceleration_scaling_factor(0.3)

init_pose = get_PoseStamped(rob.get_current_pose())
print(init_pose)
# handover init pose #########################
p = [0.289, 0.000, 0.400]
q = [1.000, -0.002, -0.006, 0.002] 
joints = [0, -50, 0, -150, 0, 100, 45]
joints = deg_to_rad(joints)
#rob.go(joints)

# grasp init pose ###############################
p = [0.001, 0.288, 0.399]
q = [0.710, 0.705, -0.004, 0.007] 
joints = [90, -50, 0, -150, 0, 100, 45]
joints = deg_to_rad(joints)
rob.go(joints)

# ee z-vertical pose ######################
pose = rob.get_current_pose()
pose_crr = get_PoseStamped(pose)
p_crr = pose_crr[0:3]
q_crr = pose_crr[3:7]
R = tf.transformations.quaternion_matrix(q_crr)
current_z_vec = array(R[0:3, 2])
target_z_vec = array([0,0,-1])
q_rot = rotation_between_2v(current_z_vec, target_z_vec)
q_new = transformation_Q(q_crr,q_rot)
target = give_PoseStamped(frame, q_new, p_crr)
#rob.go(target)

# ee rot_z motion ###########################
pose = rob.get_current_pose()
pose_crr = get_PoseStamped(pose)
p_crr = pose_crr[0:3]
q_crr = pose_crr[3:7]
q_rot = angle_axis_to_q_complex(axis = "z", angle = -35, angle_type = "degree")
q_new = transformation_Q(q_crr,q_rot)
target = give_PoseStamped(frame, q_new, p_crr)
#rob.go(target)
#final_pose = get_PoseStamped(rob.get_current_pose())
#print(final_pose[3:7])
#print(q_new)
#print(linalg.norm(array(final_pose[3:7])-array(q_new)))
# orientation error = 0.0012722568794945137 0.0013044281767996774

# move position with consistant orientation ########################
d = -0.05
pose = rob.get_current_pose()
target = pose.pose
target.position.z += d
#rob.go(pose)
#final_pose = get_PoseStamped(rob.get_current_pose())
#print(abs(linalg.norm(array(final_pose[0:3])-array(init_pose[0:3]))-abs(d)))
# position error = 0.0011246125396957157 0.000892771064345925



    
    
    

