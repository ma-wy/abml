#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *
class external_input:
  def __init__(self):
#=======input==================================================================================
    self.time_origin_sub = rospy.Subscriber('/time_origin', Float32, self.callback_time_origin)
#    self.rob_state_sub = rospy.Subscriber('/joint_states', JointState, self.callback_rob_state)
    self.rob_ee_sub = rospy.Subscriber('/rob_ee', PoseStamped, self.callback_rob_ee)
#=======output==============================================================================
#    self.d_pose_pub = rospy.Publisher('/external_input', Float64MultiArray, queue_size=1)
#    self.target_pose_pub = rospy.Publisher('/target_pose', PoseArray, queue_size=1)
    self.target_pose_pub = rospy.Publisher('/target_pose', PoseStamped, queue_size=1)
    
# members
    self.base_frame = 'panda_link0'
    self.ee_p_old = []
    self.ee_q_old = []
    self.ee_p_new = []
    self.ee_q_new = []
#    self.ee_pose_new = []
    self.ee_pose = [0.0] * 7
    self.d_pose = zeros(6)
    
    self.target_pose_list = []
    self.target_pose = self.ee_pose
    '''
    cmd_len = 5
    for i in range(cmd_len):
      self.target_pose_list.append(self.ee_pose)
    '''
    
  def callback_time_origin(self, data):
#    tt = self.ee_p_new
#    self.ee_p_new = array(tt) + self.d_pose[0:3]
    print(self.d_pose)
    self.ee_p_new = array(self.ee_p_old) + self.d_pose[0:3]
    ee_q_rot = angle_axis_to_q(self.d_pose[3:6])
    self.ee_q_new = transformation_Q(self.ee_q_old, ee_q_rot) 
#    self.ee_pose_new = list(self.ee_p_new) + list(self.ee_q_new)
    '''
    del self.target_pose_list[0]
    self.target_pose_list.append(self.ee_pose_new)
    pose_list = []
    for pose in self.target_pose_list:
      p = pose[0:3]
      q = pose[3:7]
      pose_temp = give_Pose(p, q)
      pose_list.append(pose_temp)
    #print(pose_list)
    pose_list_temp = give_PoseArray(self.base_frame, pose_list)
    self.target_pose_pub.publish(give_PoseArray(self.base_frame, pose_list))
    '''
    pose_pub = give_PoseStamped(self.base_frame, self.ee_q_new, self.ee_p_new)   
    self.target_pose_pub.publish(pose_pub)
        
  def callback_rob_ee(self, data):
    pose = get_Pose(data)
    self.ee_p_old = pose[0:3]
    self.ee_q_old = pose[3:7]


  def get_target(self, d_pose):
    self.d_pose = d_pose    

def print_usage():
  print('===usage===') 
  print('step 1:')
  print('press buttons on to choose an arribution of pose to control')
  print('step 2:')
  print('rotate the rocker to control direction')

def output_init():
  degree = zeros(6)
  direction = 0
  return degree, direction
  
def main(args):
  rospy.init_node('external_input', anonymous=True)    
  # pose=[px3, rax3]
  ei = external_input()
  d_pose = zeros(6)
  d_p = 0.005 # m
  d_ra = 0.01 # rad

  print_usage()

  degree_button = [0,3,5,1,2,7]
  degree_list = ['x', 'y', 'z', 'p', 'a', 'r']
  degree_num = len(degree_list)
  button_state = list(zeros(degree_num))
  direction_list = ['+','-']
  axes_state = [0, 0]
  v = array([d_p, d_p, d_p, d_ra, d_ra, d_ra])

  pygame.init()
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  degree, direction = output_init()

  while not rospy.is_shutdown():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.JOYBUTTONDOWN:
        for i in range(degree_num):
          button_state[i] = joystick.get_button(degree_button[i])
        if any(button_state):
          d_pose = zeros(degree_num)
          input_button = degree_list[button_state.index(1)]
          print('degree')
          print(input_button)
          degree = get_control_degree(input_button)
          direction = 0
        else:
          print_usage()
          degree, direction = output_init()

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
    d_pose = direction * degree * v
    
    ei.get_target(d_pose)
    

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
  
  
  
  
  


