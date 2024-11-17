#!/usr/bin/env python3.8

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class hand_servoing:
  def __init__(self):
#=======input==================================================================================
    self.hand_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_hand_2d)
    self.if_hand_sub = rospy.Subscriber('/if_hand', Bool, self.callback_if_hand)
#=======output==================================================================================
    self.target_pub = rospy.Publisher("/target", PoseStamped, queue_size=1)
#===============================================================================================
# members
    self.lw_ratio = 0
    self.thumb_dir_pix = []
    self.if_hand = False
    
  def callback_if_hand(self, data):
    self.if_hand = data.data
    
  def callback_hand_2d(self, data):
    handedness = data.handedness.data
    wrist = [data.wrist.x, data.wrist.y, data.wrist.z]
    thumb_tip = [data.thumb_tip.x, data.thumb_tip.y, data.thumb_tip.z]
    index_tip = [data.index_tip.x, data.index_tip.y, data.index_tip.z]
    middle_tip = [data.middle_tip.x, data.middle_tip.y, data.middle_tip.z]
    ring_tip = [data.ring_tip.x, data.ring_tip.y, data.ring_tip.z]
    pinky_tip = [data.pinky_tip.x, data.pinky_tip.y, data.pinky_tip.z]
    index_mcp = [data.index_mcp.x, data.index_mcp.y, data.index_mcp.z]
    middle_mcp = [data.middle_mcp.x, data.middle_mcp.y, data.middle_mcp.z]
    ring_mcp = [data.ring_mcp.x, data.ring_mcp.y, data.ring_mcp.z]
    pinky_mcp = [data.pinky_mcp.x, data.pinky_mcp.y, data.pinky_mcp.z]
    palm = [wrist, index_mcp, middle_mcp, ring_mcp, pinky_mcp]
    hand_axy = mean(array(palm), axis=0)

    d = p3_to_line_p12(array(index_mcp), array(pinky_mcp), array(wrist))
    self.lw_ratio = d/norm(array(index_mcp)-array(pinky_mcp))
    v1 = array(thumb_tip) - array(wrist)
    v2 = array(index_mcp) - array(wrist)
    self.thumb_dir_pix = 1/2*(v1/norm(v1) + v2/norm(v2))
  
  
  
def main(args):
  rospy.init_node('hand_servoing', anonymous=True)
  hs = hand_servoing()
  
  rob = MoveGroupCommander('panda_arm')
  rob.set_end_effector_link("panda_hand")
  frame = "panda_link0"
  rob.set_max_velocity_scaling_factor(0.1)
  rob.set_max_acceleration_scaling_factor(0.1)
  
  init_ratio = hs.lw_ratio
  lw_ratio_pre = hs.lw_ratio
  
  while not rospy.is_shutdown():
    if hs.if_hand:
      pose_crr = get_PoseStamped(rob.get_current_pose()) 
      p = pose_crr[0:3]
      q_crr = pose_crr[3:7]
      print("lw ratio")
      print(hs.lw_ratio)
      # y axis in base, x axis in ee frame
      q_rot = angle_axis_to_q_complex(axis = "y", angle = hs.lw_ratio - lw_ratio_pre, angle_type = "rad")
      print(q_rot)
      print(q_crr)
      lw_ratio_pre = hs.lw_ratio
      
      q = transformation_Q(q_crr,q_rot)
      target = give_PoseStamped(frame, q, p)
      hs.target_pub.publish(target)
      #input()
      rob.go()
      time.sleep(1)
      
  
  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
if __name__ == '__main__':

    main(sys.argv)









####################################################################
rospy.init_node("test_moveit_orientation", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link("panda_hand")
frame = "panda_link0"
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)

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



    
    
    

