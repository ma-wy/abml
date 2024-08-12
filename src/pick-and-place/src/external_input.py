#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

# pose=[px3, rax3]
rospy.init_node('external_input')
d_pose = zeros(6)
d_p = 0.001 # mm
d_ra = 0.001 # rad
d_pose_pub = rospy.Publisher('/external_input', Float64MultiArray, queue_size=10)
d_pose_Float64MultiArray = Float64MultiArray()
d_pose_Float64MultiArray.data = list(d_pose)
print('===usage===') 
print('step 1:')
print('press x/y/z/r/a/p to choose an arribution of pose to control')
print('step 2:')
print('press -/+ to control direction')

degree = ['x', 'y', 'z', 'p', 'a', 'r']
direction = ['+','-']


# https://www.volcengine.com/theme/6619726-R-7-1

while(True):
  kk = getch.getch()
  if kk in degree:
  # p: x y z
    if kk=='x':
      print('control p_x')
      dd = getch.getch()
      if kk=='+':
        d_pose = d_pose + array([1, 0, 0, 0, 0, 0]) * d_p 
      elif input()=='-':
        d_pose = d_pose - array([1, 0, 0, 0, 0, 0]) * d_p 
    elif input()=='y':     
      if input()=='+':
        d_pose = d_pose + array([0, 1, 0, 0, 0, 0]) * d_p 
      elif input()=='-':
        d_pose = d_pose - array([0, 1, 0, 0, 0, 0]) * d_p  
    elif input()=='z':     
      if input()=='+':
        d_pose = d_pose + array([0, 0, 1, 0, 0, 0]) * d_p 
      elif input()=='-':
        d_pose = d_pose - array([0, 0, 1, 0, 0, 0]) * d_p 
    # ra: r y p    
    elif input()=='p':     
      if input()=='+':
        d_pose = d_pose + array([0, 0, 0, 1, 0, 0]) * d_ra 
      elif input()=='-':
        d_pose = d_pose - array([0, 0, 0, 1, 0, 0]) * d_ra 
    elif input()=='a':     
      if input()=='+':
        d_pose = d_pose + array([0, 0, 0, 0, 1, 0]) * d_ra 
      elif input()=='-':
        d_pose = d_pose - array([0, 0, 0, 0, 1, 0]) * d_ra 
    elif input()=='r':     
      if input()=='+':
        d_pose = d_pose + array([0, 0, 0, 0, 0, 1]) * d_ra 
      elif input()=='-':
        d_pose = d_pose - array([0, 0, 0, 0, 0, 1]) * d_ra 
  else:
    continue      
  kk = getch()
      
angle_axis_to_q(r)
#  d_pose_pub.publish(d_pose_Float64MultiArray)

