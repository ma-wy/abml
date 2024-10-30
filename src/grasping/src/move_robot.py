#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class move_robot():
  def __init__(self):
#input==============================================================================================  
    self.grasping_target_sub = rospy.Subscriber("/ee_target_in_base", PoseStamped, self.callback_grasping_target)
#output=======================================================================================      
    self.magnet_pub = rospy.Publisher("/control_magnet", Int32, queue_size=1)
    self.bellow_pub = rospy.Publisher("/control_pump", Float64, queue_size=1)
    self.rob_trigger_pub = rospy.Publisher("/if_move_stop", Bool, queue_size=1)
#member===========================================================================================      
    self.target_pose = []

    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    self.magnet_trigger = Int32()
    self.bellow_trigger = Float64()
    self.rob_trigger = Bool()
    #os.system("rosrun franka_basic_motion grasping_init.py grasping")
    self.spare_p = array([0.1, 0.5, -0.07])
    self.spare_q = array([0.707, 0.707, 0.0, 0.0])
    self.frame = 'panda_link0'
    self.spare_place = give_PoseStamped(self.frame, self.spare_q, self.spare_p)
    self.count = 0
    self.spare_bias = array([-0.1, 0, 0])
    
    self.gripper = MoveGroupCommander('panda_hand')
    
    
    
  def callback_grasping_target(self, data):
    self.target_pose = data
    print('recieved target')
    print(self.target_pose)
    print('press enter to move robot to the target')
    #input()
    #self.rob.go(self.target_pose)

def main(args):
  rospy.init_node("move_robot", anonymous=True)
  mr = move_robot()
  
  #while not rospy.is_shutdown():
    #print('press enter to move robot to the target')
    #input()
    #mr.rob.go(mr.target_pose)
  '''
  mr.magnet_trigger.data = 1
  mr.magnet_pub.publish(mr.magnet_trigger)
  
  mr.bellow_trigger.data = 3.8
  mr.bellow_pub.publish(mr.bellow_trigger)
  print('connect the pump')
  time.sleep(2)
  os.system("rosrun franka_basic_motion gripper_width.py 0.0")
  # pick up
  os.system("rosrun franka_basic_motion trans_axis.py z 0.1")
  # move to the target spare place
  mr.spare_p += mr.spare_bias * mr.count
  mr.spare_place = give_PoseStamped(mr.frame, mr.spare_q, mr.spare_p)
  mr.rob.go(mr.spare_place)
  # open the gripper
  os.system("rosrun franka_basic_motion gripper_width.py 0.05")
  os.system("rosrun franka_basic_motion grasping_init.py grasping")
  
  mr.rob_trigger.data = True
  mr.rob_trigger_pub.publish(mr.rob_trigger)
  mr.count += 1
  '''
  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

