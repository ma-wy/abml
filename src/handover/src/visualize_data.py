#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

# revise param
dataset_num = 1
member_num = 1
pose_num = 3

hand_key_points_name = ['wrist', 'thumb_tip', 'index_tip', 'middle_tip', 'ring_tip', 'pinky_tip', 'index_mcp', 'middle_mcp', 'ring_mcp', 'pinky_mcp', 'palm']
# init rosnode
rospy.init_node('visualize_data', anonymous=True)
hand_pc_pub = rospy.Publisher("/hand_pc_rob", PointCloud2, queue_size=1)
palm_pub = rospy.Publisher("/palm", PointStamped, queue_size=10)
handle_frame_pub = rospy.Publisher("/handle_frame", PoseStamped, queue_size=10)
hand_frame_pub = rospy.Publisher("/hand_frame", PoseStamped, queue_size=10)

# load data
dataset_path = load_str('/home/abml/zoe_ws/src/handover/data/path.txt')
hand_traj_path = dataset_path + 'dataset_' + str(dataset_num) + '/member_' + str(member_num) + '/pose_' + str(pose_num) + '/hand_traj.txt'
hand_traj = loadtxt(hand_traj_path)
handle_path = dataset_path + 'dataset_' + str(dataset_num) + '/member_' + str(member_num) + '/pose_' + str(pose_num) + '/handle_to_base.txt'
handle_pose = loadtxt(handle_path)
handle_p = handle_pose[0:3]
handle_q = handle_pose[3:7]

    
# loop
data_num = len(hand_traj)
for i in range(data_num):
  print(str(i+1) + '/' + str(data_num))
  hand_key_points = hand_traj[i][1:]
  input()
  # generate and pub hand pc
  r = 255
  g = 0
  b = 0
  a = 255
  rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
  hand_pc = []
  for j in range(11):
    pt = list(hand_key_points[j*3: (j+1)*3]) + [rgb] 
    hand_pc.append(pt)

  HEADER = Header()
  HEADER.frame_id = 'base'
  FIELDS = [
    PointField('x', 0, PointField.FLOAT32, 1),
    PointField('y', 4, PointField.FLOAT32, 1),
    PointField('z', 8, PointField.FLOAT32, 1),
    PointField('rgb', 12, PointField.UINT32, 1),
  ]
  POINTS = hand_pc#listhand_pc
  outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
  hand_pc_pub.publish(outputPoints)     
  
  # pub palm point
  palm = hand_pc[-1][0:3]
  palm_ps = give_PointStamped('base', palm)
  palm_pub.publish(palm_ps)
  
  # pub handle frame
  handle_frame = give_PoseStamped('base', handle_q, handle_p)
  handle_frame_pub.publish(handle_frame)
  
  # pub hand frame
  wrist = array(hand_pc[0][0:3])
  thumb_tip = array(hand_pc[1][0:3])
  index_mcp = array(hand_pc[6][0:3])
  pinky_mcp = array(hand_pc[9][0:3])
  
  v_1 = index_mcp - wrist
  v_2 = pinky_mcp - wrist
  v_3 = thumb_tip - wrist
  
  z_axis = cross(v_2, v_1)
  z_axis = z_axis/norm(z_axis)
  
  x_axis = (v_3 + v_1)/2
  x_axis = x_axis/norm(x_axis)
  
  y_axis = cross(z_axis, x_axis)
  x_axis = cross(y_axis, z_axis)
  
  q = xyz_axis_to_q(x_axis, y_axis, z_axis)
  p = palm
  
  hand_frame = give_PoseStamped('base', q, p)
  hand_frame_pub.publish(hand_frame)
















    
