#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

def line_intersect_circle(p, lsp, esp):
    # p is the circle parameter, lsp and lep is the two end of the line
    x0, y0, r0 = p
    x1, y1 = lsp
    x2, y2 = esp
    if r0 == 0:
        return [[x1, y1]]
    if x1 == x2:
        if abs(r0) >= abs(x1 - x0):
            p1 = x1, round(y0 - math.sqrt(r0 ** 2 - (x1 - x0) ** 2), 5)
            p2 = x1, round(y0 + math.sqrt(r0 ** 2 - (x1 - x0) ** 2), 5)
            inp = [p1, p2]
            # select the points lie on the line segment
            inp = [p for p in inp if p[0] >= min(x1, x2) and p[0] <= max(x1, x2)]
        else:
            inp = []
    else:
        k = (y1 - y2) / (x1 - x2)
        b0 = y1 - k * x1
        a = k ** 2 + 1
        b = 2 * k * (b0 - y0) - 2 * x0
        c = (b0 - y0) ** 2 + x0 ** 2 - r0 ** 2
        delta = b ** 2 - 4 * a * c
        if delta >= 0:
            p1x = round((-b - math.sqrt(delta)) / (2 * a), 5)
            p2x = round((-b + math.sqrt(delta)) / (2 * a), 5)
            p1y = round(k * x1 + b0, 5)
            p2y = round(k * x2 + b0, 5)
            inp = [[p1x, p1y], [p2x, p2y]]
            # select the points lie on the line segment
            inp = [p for p in inp if p[0] >= min(x1, x2) and p[0] <= max(x1, x2)]
        else:
            inp = []

    return inp if inp != [] else [[x1, y1]]

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
    







