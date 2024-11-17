#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class detect_voice_direction():
  def __init__(self):
#input==============================================================================================  
    self.mic_angle_sub = rospy.Subscriber("/voice_direction", Int32, self.callback_mic_angle)
#output=======================================================================================      
#    self.rob_trigger_pub = rospy.Publisher("/if_move_stop", Bool, queue_size=1)
#member===========================================================================================      
    self.mic_angle = None
    self.rob_joints_target = []
    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    print('ready to track voice')
    
    
  def callback_mic_angle(self, data):
    self.mic_angle = data.data
    print('recieved voice direction')
    print(self.mic_angle)
    
    '''
    ee_pose = get_PoseStamped(self.rob.get_current_pose())
    ee_x = ee_pose[0]
    ee_y = ee_pose[1]
    
    theta = xy_to_theta(ee_x, ee_y)
    
    alpha = deg_to_rad([-15 + self.mic_angle])[0]
    print(rad_to_deg([theta])[0])
    
    voice_dir_in_base = theta - alpha
    if voice_dir_in_base < -pi:
      voice_dir_in_base = voice_dir_in_base + 2*pi
    '''
    
    rob_joints_degree = self.rob.get_current_joint_values()
    print('current robot joint values')
    print(rad_to_deg([rob_joints_degree[0]])[0])
    
    theta = rob_joints_degree[0]
    alpha = deg_to_rad([-15 + self.mic_angle])[0]
    print(rad_to_deg([theta])[0])
    
    voice_dir_in_base = theta - alpha
    if voice_dir_in_base < -pi:
      voice_dir_in_base = voice_dir_in_base + 2*pi    
    
    
    
    self.rob_joints_target = deepcopy(rob_joints_degree)
    self.rob_joints_target[0] = voice_dir_in_base
    print('target robot joint values')
    print(rad_to_deg([voice_dir_in_base])[0])
    
    print('press enter to move robot to the target')
    self.rob.go(self.rob_joints_target)

def main(args):
  rospy.init_node("detect_voice_direction", anonymous=True)
  dvd = detect_voice_direction()
  
  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
    







