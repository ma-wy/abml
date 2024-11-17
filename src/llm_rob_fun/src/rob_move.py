#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from llm_grasping.srv import SetRobFun, SetRobFunRequest, SetRobFunResponse

class rob_move:
  def __init__(self):
#=======input==================================================================================
    self.service = rospy.Service('/llm_rob_fun_server', SetRobFun, self.callback_response_rob_fun)
    self.target_sub = rospy.Subscriber("/ee_target_in_base", PoseStamped, self.callback_rob_target_pose)
#=======output==================================================================================
    self.magnet_pub = rospy.Publisher("/control_magnet", Int32, queue_size=1)
    self.bellow_pub = rospy.Publisher("/control_pump", Float64, queue_size=1)
    self.power_pub = rospy.Publisher("/control_power", Int32, queue_size=1)
    self.spare_place_pub = rospy.Publisher("/spare_place", PoseStamped, queue_size=1)
    self.raise_target_pub = rospy.Publisher("/raise_target", PoseStamped, queue_size=1)
#=================================================================================
# members
    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    self.gripper = MoveGroupCommander('panda_hand')
    self.gripper.set_goal_joint_tolerance(0.002)
    rob_fun = ['shelve', 'handover', 'idle']
    self.rob_fun = 'idle'

    self.init_joints = [1.575267887668587, -0.4352075831555483, 0.26885588875151517, -2.2980965634335013, 0.15372256857881975, 1.6601492852899764, 1.0014479012643849]
    self.target_pose = []

    self.power_trigger = Int32()
    self.magnet_trigger = Int32()
    self.bellow_trigger = Float64()
    self.spare_p = array([-0.45, 0.5, -0.06])
    self.spare_q = array([0.7213572259725731, 0.6925113348648213, 0.004594861464519345, 0.007119752033557192])
    
    self.frame = 'panda_link0'
    self.count = 0
    self.spare_place = give_PoseStamped(self.frame, self.spare_q, self.spare_p)
    #self.spare_bias = array([-0.1, 0, 0])
    self.if_recieved_target = False
    print('###################')
    print('ready to move robot')
    print('###################')
    
#===============================================================================================
  def callback_rob_target_pose(self, data):
    self.target_pose = data
    print('recieved target')
    print(self.target_pose)
    self.if_recieved_target = True
    
  def callback_response_rob_fun(self,request):
    res = SetRobFunResponse()
    res.success = False
    self.rob_fun = request.action
    print("rob_fun = " + str(self.rob_fun))
    
    if self.rob_fun == 'handover':
      print(self.rob_fun)
      if self.if_recieved_target == True:
        # robot motion
        print('This function is under development.')
        # return signal
        res.success = True
        # update target
        self.if_recieved_target = False
        
        
    elif self.rob_fun == 'shelve':
      print(self.rob_fun)
      if self.if_recieved_target == True:
        print(self.if_recieved_target)
        print(self.target_pose)
        ###############################
        # generate spare target
        #self.spare_place = deepcopy(self.target_pose)
        self.spare_place.pose.position.x += 0.1 # from the left edge
        self.spare_place_pub.publish(self.spare_place)
        # generate raise target
        raise_target = deepcopy(self.target_pose)
        raise_target.pose.position.z += 0.1 # 10cm
        self.raise_target_pub.publish(raise_target)
        #############################3        
        
        print('press enter')
        input()
        
        # robot motion
        # activate the magnet
        print('activate the magnet')
        self.magnet_trigger.data = 1
        self.magnet_pub.publish(self.magnet_trigger)
        # move robot to the target
        print('move robot to the target')
        self.rob.go(self.target_pose)

        print('press enter')
        input()
                
        # activate the bellow
        print('activate the bellow')
        self.bellow_trigger.data = 3.8
        self.bellow_pub.publish(self.bellow_trigger)
        self.power_trigger.data = 1
        self.power_pub.publish(self.power_trigger)
        
        time.sleep(8)
        # close the gripper
        print('close the gripper')
        close_width = 0.001
        self.gripper.go([close_width, close_width])
        self.gripper = MoveGroupCommander('panda_hand')
        self.gripper.set_start_state_to_current_state()
        self.gripper.set_goal_joint_tolerance(0.002)
        print('press enter')
        input()
        
        
        # raise up
        print('raise up')
        self.rob.go(raise_target)
        
        # move to the spare target
        print('move to the spare target')
        #print('press enter')
        #input()
        self.rob.go(self.spare_place)
        # switch off the magnet
        print('switch off the magnet')
        self.magnet_trigger.data = 0
        self.magnet_pub.publish(self.magnet_trigger)
        # open the gripper
        print('open the gripper')
        self.gripper.go([0.025, 0.025]) # width = 0.05 
        # switch off the bellow
        print('switch off the bellow')
        #self.bellow_trigger.data = 0
        #self.bellow_pub.publish(self.bellow_trigger)
        self.power_trigger.data = 0
        self.power_pub.publish(self.power_trigger)
        # reset the robot
        print('reset the robot')
        '''
        width = self.gripper.get_current_joint_values()
        print(width)
        if width[0] > 0.02:
          self.rob.go(self.init_joints)
        else:
          self.gripper.go([0.025, 0.025])
        '''
        self.gripper.go([0.025, 0.025])
        print('press enter')
        input()       
        #os.system('roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110')
        #os.system('roslaunch grasping launch_tf_subs.launch')
        self.rob.go(self.init_joints)
        # return signal
        res.success = True
        # update target
        self.if_recieved_target = False    
      
    else:
      print(self.rob_fun)
      print('please select a function: 1. handover; 2. shelve.')
      self.rob_fun = 'idle'
      res.success = False
    return res
    

def main(args):
  rospy.init_node('rob_move', anonymous=True)
  rate = rospy.Rate(20)
  rm = rob_move()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)

    
    
