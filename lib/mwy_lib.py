#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#import sys 
#sys.path.append("/home/abml/zoe_ws/lib")
#from mwy_lib import *


'''
@author: mwy
'''
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *

'''
# a
def angle_axis_to_q(r):
def angle_axis_to_q_complex(axis = "z", angle = 5, angle_type = "degree"):
# b
def bias_2d_to_3d(pt_2d, param_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/bias.txt'):
# c
def calculate_swept_area_with_end_circles(line, radius, resolution=32):
def cam_2_ee_pose(pose_cam):
def check_file(file_path, remove_file = False):
def check_make_clear_folder(path):
def clean_data(data):
def clear_folder(folder_path):
def closest(mylist, Number):
def create_circle(center, radius, resolution=32):
def create_ring(center, inner_radius, outer_radius, resolution=32):
# d
def d_time_ms(t1, t2):
def deg_to_rad(joints):
def detect_outliers(data, threshold=3):
def detect_qrcode(frame, h, w, intrinsics = [317.494, 246.239, 607.652, 607.507]):
# e
def ee_pose_link8_to_ee(pose):
# f
def file_num_in_dir(path):
def filter3(data, k):
def func(x,a,b):  
def franka_open_gripper():
def franka_close_gripper():
def franka_homing_gripper():
# g
def generate_folder(path):
def generate_ur_cmd(p,q):
def get_argv(value=None, index=1):
def get_control_degree(input_button):
def get_control_direction(input_button):
def get_overlapping_segments(line, ring):
def get_Point(point32):
def get_PointStamped(pointstamped):
def get_polygon_corners(polygon):
def get_Pose(pose):
def get_PoseArray(posearray):
def get_PoseStamped(posestamped):
def get_tf(frame_p, frame_ch):
def give_Path(frame, poses):
def give_Point(p):
def give_PointStamped(frame, p):
def give_Pose(p,q):
def give_PoseArray(frame, poses):
def give_PoseStamped(frame, q, p):
# h
# i
# j
def judge_decimal(data):
# k
# l
def load_str(file_path):
def load_str_lines(file_path): 
# m
def mic_to_rob(mic_angle, rob_joints):
# n
# o
# p
def p_cam_2_base(p_cam, frame_p = '/panda_link0', frame_ch = 'camera_color_optical_frame'): 
def p3_to_line_p12(p1,p2,p3):
def polyfit_2d_to_3d(pt_2d, param_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/'):
def pose_2D_to_3D(x_axis, y_axis, z_axis = 'down'):
def pq_to_T(p,q):
# q
def q_to_angle_axis(q):
def q_w_trans(q): 
def q_wxyz_to_xyzw(q_wxyz):
def q_xyzw_to_wxyz(q_xyzw):
# r
def rad_to_deg(joints):
def ray_from_point_slope(start_point, slope, vector_v, length=1000):
def recorder_corners(corners, mode):
def rot_Q(q_old, q_new):
def rotation_between_2v(v_old, v_new):
# s
def saveDataStep(data, file_path, if_clear = False):
def shorten_data(data):
# t
def trans_2D_to_3D(p_2D, p_list = [[659, 361], [371, 167], [0.005,-0.005], [-0.195,-0.305]], mode = 'point'):
def trans_v_to_q(v):
def transformation_P(v_old,trans,q_rot):
def transformation_Q(q_orig,q_rot):
# u
# v
def vector_clockwise_angle(x, y):
# w
# x
def xy_to_theta(x,y):
def xyz_axis_to_q(x_axis, y_axis, z_axis):
# y
# z
'''
# do not delet
grasping_pose_init = loadtxt(os.path.join(os.path.dirname(__file__), 'init_joints_grasp.txt'))
counting_pose_init = loadtxt(os.path.join(os.path.dirname(__file__), 'init_joints_count.txt'))
tempt_pose_init = loadtxt(os.path.join(os.path.dirname(__file__), 'init_joints_tempt.txt'))

#handover_pose_init = loadtxt(os.path.join(os.path.dirname(__file__), 'init_joints_handover.txt'))



def name_time():
  name = '%.7f' % time.time() 
  return name


def get_polygon_corners(polygon):
  """
  获取多边形(包括可能的内环)的所有角点坐标
  
  参数:
      polygon: Shapely Polygon对象
      
  返回:
      包含所有角点坐标的列表[(x1,y1), (x2,y2), ...]
  """
  if polygon is None or polygon.is_empty:
      return []
      
  corners = []
  
  # 获取外环坐标
  if hasattr(polygon, 'exterior'):
      exterior_coords = list(polygon.exterior.coords)
      corners.extend(exterior_coords)
  
  # 获取所有内环坐标
  if hasattr(polygon, 'interiors'):
      for interior in polygon.interiors:
          interior_coords = list(interior.coords)
          corners.extend(interior_coords)
  
  return corners
def get_overlapping_segments(line, ring):
  """
  计算LineString与圆环的重叠部分线段
  
  参数:
      line: LineString对象
      ring: 圆环(Polygon对象)
      
  返回:
      包含所有重叠线段的MultiLineString
  """
  # 计算交集
  intersection = line.intersection(ring)
  
  # 如果交集是LineString或MultiLineString，直接返回
  if intersection.is_empty:
      return None
  elif intersection.geom_type == 'LineString':
      return [intersection]
  elif intersection.geom_type == 'MultiLineString':
      return list(intersection.geoms)
  else:
      return None
      
def calculate_swept_area_with_end_circles(line, radius, resolution=32):
  """
  计算圆沿线段滑动所覆盖的范围，包含端点完整半圆
  
  参数:
      line: LineString对象，表示滑动路径
      radius: 圆的半径
      resolution: 圆形的近似精度（边数）
      
  返回:
      Polygon对象，表示覆盖的范围
  """
  # 1. 创建线段的缓冲区域（自动包含端点半圆）
  line_buffer = line.buffer(
      radius, 
      resolution=resolution,
      cap_style=2,  # 圆形端点
      join_style=2  # 圆形连接
  )
  
  # 2. 在端点添加完整圆（确保端点覆盖完整圆而非半圆）
  start_circle = Point(line.coords[0]).buffer(radius, resolution=resolution)
  end_circle = Point(line.coords[-1]).buffer(radius, resolution=resolution)
  
  # 3. 合并所有几何图形
  full_area = unary_union([line_buffer, start_circle, end_circle])
  
  return full_area
  
def create_ring(center, inner_radius, outer_radius, resolution=32):
  """创建圆环(环形)"""
  outer_circle = create_circle(center, outer_radius, resolution)
  inner_circle = create_circle(center, inner_radius, resolution)
  return outer_circle.difference(inner_circle)
    
def create_circle(center, radius, resolution=32):
  """
  使用buffer方法创建圆形
  
  参数:
      center: 圆心坐标(x,y)或Point对象
      radius: 半径
      resolution: 近似圆的多边形边数(默认32)
      
  返回:
      Shapely Polygon对象表示圆形
  """
  if not isinstance(center, Point):
      center = Point(center)
  return center.buffer(radius, resolution=resolution)
  
def vector_clockwise_angle(x, y):
  """
  计算原点指向点(x,y)的向量与x轴正向的顺时针角度(0-360度)
  
  参数:
      x: 点的x坐标
      y: 点的y坐标
      
  返回:
      顺时针角度(0-360度)
  """
  # 计算反正切值(弧度)，范围在(-π, π]
  angle_rad = math.atan2(y, x)
  
  # 转换为度数(-180到180度)
  angle_deg = math.degrees(angle_rad)
  
  # 将角度转换为顺时针方向(数学坐标系中atan2是逆时针方向)
  clockwise_angle = -angle_deg
  
  # 调整到0-360度范围
  if clockwise_angle < 0:
      clockwise_angle += 360
  elif clockwise_angle >= 360:
      clockwise_angle -= 360
  
  return clockwise_angle
  
def ray_from_point_slope(start_point, slope, vector_v, length=1000):
  """
  创建从起点出发，具有给定斜率，且与向量v成锐角的射线
  
  参数:
      start_point: 射线起点，可以是(x,y)元组或Shapely Point对象
      slope: 射线斜率
      vector_v: 参考向量(x,y)
      length: 射线的延伸长度(默认1000单位)
      
  返回:
      Shapely LineString对象表示的射线
  """
  if not isinstance(start_point, Point):
      start_point = Point(start_point)
  
  x0, y0 = start_point.x, start_point.y
  
  # 计算射线的两个可能方向
  dx = length / (1 + slope**2)**0.5
  dy = slope * dx
  
  # 两个可能的终点
  end_point1 = Point(x0 + dx, y0 + dy)
  end_point2 = Point(x0 - dx, y0 - dy)
  
  # 计算两个方向与向量v的点积
  vx, vy = vector_v
  dot1 = dx * vx + dy * vy
  dot2 = (-dx) * vx + (-dy) * vy
  
  # 选择点积为正的方向(锐角)
  if dot1 > dot2:
      end_point = end_point1
  else:
      end_point = end_point2
  
  return LineString([start_point, end_point])

def detect_hand_outliers(data, threshold=3):
  """离群点检测"""
  mean_d = np.mean(data)
  std_d = np.std(data)
  outliers = []

  for y in data:
      z_score = (y - mean_d) / std_d
      if np.abs(z_score) > threshold:
          outliers.append(y)
  return outliers

def generate_folder(path):
  if os.path.exists(path):
    print('the folder exists')
  else:
    os.system('mkdir ' + path)
'''
def franka_open_gripper(client=actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction), width=0.025, speed=0.1):
  gripper_move_client = client
#  gripper_move_client.wait_for_server()  
  gripper_open = franka_gripper.msg.MoveGoal()
  gripper_open.width = width
  gripper_open.speed = speed
  gripper_move_client.send_goal(gripper_open)
  gripper_move_client.wait_for_result()
  return gripper_move_client.get_result().success

def franka_close_gripper(client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction), speed=0.1):
  gripper_grasp_client = client
#  gripper_grasp_client.wait_for_server()  
  gripper_close = franka_gripper.msg.GraspGoal()
  gripper_close.width = 0.0
  gripper_close.epsilon.inner = 0.1
  gripper_close.epsilon.outer = 0.1
  gripper_close.speed = 0.1
  gripper_close.force = 5
  gripper_grasp_client.send_goal(gripper_close)
  gripper_grasp_client.wait_for_result()
  return gripper_grasp_client.get_result().success

def franka_homing_gripper(client = actionlib.SimpleActionClient('/franka_gripper/homing', franka_gripper.msg.HomingAction)):
  gripper_homing_client = client
#  gripper_homing_client.wait_for_server()  
  gripper_homing = franka_gripper.msg.HomingGoal()
  gripper_homing_client.send_goal(gripper_homing)
  gripper_homing_client.wait_for_result()
  return gripper_homing_client.get_result().success  
'''

def generate_pt(p, Cx, Cy, fx, fy):
  scale = 1000.0
  d = float(p[2])
  pt = [(float(p[0])-Cx)*d/fx/scale,(float(p[1])-Cy)*d/fy/scale,d/scale]
  return pt

def realsense_intrinsics(cam_type, height, width):
  if cam_type == "l515" or cam_type == "L515":
    if height == 540 and width == 960:
      P = [677.20751953125, 0.0, 490.4091491699219, 0.0, 0.0, 677.1104125976562, 273.6672058105469, 0.0, 0.0, 0.0, 1.0, 0.0]
    if height == 720 and width == 1280:
      P = [902.943359375, 0.0, 653.8788452148438, 0.0, 0.0, 902.8138427734375, 364.88958740234375, 0.0, 0.0, 0.0, 1.0, 0.0]
    if height ==1080 and width == 1920:
      P = [1354.4150390625, 0.0, 980.8182983398438, 0.0, 0.0, 1354.2208251953125, 547.3344116210938, 0.0, 0.0, 0.0, 1.0, 0.0]
  if cam_type == "d435" or cam_type == "D435":
    if height == 480 and width == 640:
      P = [614.5758056640625, 0.0, 326.93829345703125, 0.0, 0.0, 615.0447998046875, 238.32223510742188, 0.0, 0.0, 0.0, 1.0, 0.0]    
  Cx, Cy, fx, fy = P[2], P[6], P[0], P[5]
  return Cx, Cy, fx, fy
  
def xy_to_theta(x,y): #theta in [-pi, pi]
  sin = y/(x**2 + y**2 )**0.5
  cos = x/(x**2 + y**2 )**0.5
  arcsin = asin(sin)
  arccos = acos(cos)
  
  if sin > 0 and cos > 0:
    area = 1
    theta = arcsin
  elif sin < 0 and cos > 0:
    area = 4
    theta = arcsin
  elif sin > 0 and cos < 0:
    area = 2
    theta = arccos
  elif sin < 0 and cos < 0:
    area = 3
    theta = -arccos
  return theta

def mic_to_rob(mic_angle, rob_joints):
  print(1)
  print(mic_angle)
  rob_base_angle = abs(195 - mic_angle)
  print(2)
  print(rob_base_angle)
  rob_joints_target = deepcopy(rob_joints)
  print(3)
  print(rob_joints_target)
  rob_joints_target[0] = rob_base_angle
  print(4)
  print(rob_joints_target)
  return rob_joints_target
  
def file_num_in_dir(path):
  return len(os.listdir(path))

def check_file(file_path, remove_file = False):
  if remove_file:
    if os.path.isfile(file_path):
      os.remove(file_path)
    print('Delete: ' + file_path)
  return os.path.isfile(file_path)

def closest(mylist, Number):
    answer = []
    for i in mylist:
        answer.append(abs(Number-i))
    return answer.index(min(answer))

def bias_2d_to_3d(pt_2d, param_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/bias.txt'):
  # pt_2d is 3d point from rgb, not pix
  x_bias = loadtxt(param_path)[0]
  y_bias = loadtxt(param_path)[1]
  x = pt_2d[0] + x_bias 
  y = pt_2d[1] + y_bias  
  return [x,y]

def func(x,a,b):
  return a*np.exp(b/x)
          
def polyfit_2d_to_3d(pt_2d, param_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/'):
  x_param = loadtxt(param_path + 'x_param.txt')
  y_param = loadtxt(param_path + 'y_param.txt')
  x = 0
  y = 0
  for i in range(len(x_param)):
    x += x_param[i] * float(pt_2d[0]) ** (len(x_param) - i - 1)
  for i in range(len(y_param)):
    y += y_param[i] * float(pt_2d[1]) ** (len(y_param) - i - 1)  
  return [x,y]  

def get_argv(value=None, index=1):
  if len(sys.argv) > 1:
    return sys.argv[index]
  else:
    return value

def p3_to_line_p12(p1,p2,p3):
  return norm(cross(p2-p1, p1-p3))/norm(p2-p1)
  
def rotation_between_2v(v_old, v_new):
  vec1 = v_old
  vec2 = v_new
  angle = np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
  axis = np.cross(vec1,vec2)
  q = tf.transformations.quaternion_about_axis(angle, axis)
  return q

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
  elif angle_type == "rad":
    a = float(angle)
  else:
    print("Please set angle_type as degree or rad.")
  R = tf.transformations.rotation_matrix(a, r)      
  q = tf.transformations.quaternion_from_matrix(R) 
  return q

def generate_ur_cmd(p,q):
  ra = q_to_angle_axis(array(q))
  cmd = np.concatenate((array(p),ra)) 
  return cmd

def load_str(file_path):
  with open(file_path, 'r') as file:
    data = file.read().rstrip()
  return data
    
def load_str_lines(file_path):    
  with open(file_path, 'r') as file:
    data = file.read().replace('\n', '')  
  return data
  
def deg_to_rad(joints):
  if type(joints) is list or array:
    for i in range(len(joints)):
      joints[i] = float(joints[i])/180.0 * pi
    return joints   
  else:
    return float(joints)/180.0 * pi  
    
def rad_to_deg(joints):
  if type(joints) is list or array:
    for i in range(len(joints)):
      joints[i] = float(joints[i])/pi * 180.0
    return joints   
  else:
    return float(joints)/180.0 * pi      
    
def check_make_clear_folder(path):
  if not os.path.exists(path):
    print('No such folder. Now create one.')
    os.makedirs(path)
  else:
    print('The folder exists. Press Enter if you want to clear it.')
    input()
    clear_folder(path)

def clear_folder(folder_path):
  files = os.listdir(folder_path)#+'*'
  for f in files:
    os.remove(os.path.join(folder_path, f))
  print('folder: ' + str(folder_path))
  print('files: ' + str(len(files)))
  print('the folder has been emptied.')
  
def judge_decimal(data):
  a = format(float(data), '.3e')
  index = a.find('e')
  if int(a[index+1:]) < -4:
    result = 'e'
  else:
    result = 'd'
  return result 
  
# shorten one line data
def shorten_data(data):
  data_list = []
  for i in data:
    i = float(i)
    result = judge_decimal(i)
    if result == 'd':
      data_list.append(float('{:.4f}'.format(i)))
    elif result == 'e':
      data_list.append(float('{:.3e}'.format(i)))
  return data_list

def clean_data(data):
  data_str = str(data)[1:-1]
  remove_chr = [",", "'"]
  for i in remove_chr:
    data_str = data_str.replace(i, "")
  return data_str

def saveDataStep(data, file_path, if_clear = False):
  data_list = shorten_data(list(data))
  data_str = clean_data(data_list)
  f = open(file_path, "a")
  if if_clear:
    f.seek(0)
  f.truncate()
  f.write(data_str)
  f.write('\n')
  f.close()  

def ee_pose_link8_to_ee(pose):
  # MoveGroupCommander set panda_link8 as the default ee
  # the input pose is PoseStamped() returned from MoveGroupCommander("panda_arm").get_current_pose()
  trans = array([pose.pose.position.x, pose.pose.position.y, pose.pose.position.z])
  q_rot = array([pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w])
  # rosrun tf tf_echo panda_link8 panda_EE
  # B_T_ee = B_T_link8 * link8_T_ee
  v_old = array([0.000, 0.000, 0.103]) # ee to link8
  q_orig = array([0.000, 0.000, -0.383, 0.924])
  p_ee = transformation_P(v_old,trans,q_rot) 
  q_ee = transformation_Q(q_orig,q_rot)  
  return p_ee, q_ee

def q_xyzw_to_wxyz(q_xyzw):
  return [q_xyzw[3],q_xyzw[0],q_xyzw[1],q_xyzw[2]]

def q_wxyz_to_xyzw(q_wxyz):
  return [q_wxyz[1],q_wxyz[2],q_wxyz[3],q_wxyz[0]]

def trans_v_to_q(v):
  vec1 = (1,0,0)
  vec2 = v
  angle = np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
  axis = np.cross(vec1,vec2)
  q = tf.transformations.quaternion_about_axis(angle, axis)
  return q

def q_w_trans(q): 
  q_w = zeros(4)
  q_w[0] = q[-1]
  q_w[1:4] = q[0:3]
  return q_w 

def p_cam_2_base(p_cam, frame_p = '/panda_link0', frame_ch = 'camera_color_optical_frame'): # trans p from camera frame to base frame 
  trans, q_rot = get_tf(frame_p, frame_ch)
  v_old = p_cam
  p_ee = transformation_P(v_old,trans,q_rot)
  return p_ee
  
def cam_2_ee_pose(pose_cam):# input the desired camera pose, return the ee pose
  frame_p = '/camera_color_optical_frame'
  frame_ch = '/panda_hand_tcp'
  trans = pose_cam[0:3]
  q_rot = pose_cam[3:7]
  v_old, q_orig = get_tf(frame_p, frame_ch)
  #q_ee = q_w_trans(transformation_Q(q_orig,q_rot)) # input q = [x,y,z,w], return q = [w, x, y, z]
  q_ee = transformation_Q(q_orig,q_rot)# input q = [x,y,z,w], return q = [x,y,z,w]
  p_ee = transformation_P(v_old,trans,q_rot)
  pose_ee = list(p_ee)+list(q_ee)
  return pose_ee

def pq_to_T(p,q):
  R = tf.transformations.quaternion_matrix(q)
  R[0:3,3] = p
  return R

def get_tf(frame_p, frame_ch):
  listener = tf.TransformListener() 
  listener.waitForTransform(frame_p, frame_ch, rospy.Time(), rospy.Duration(4.0))
  (p,q) = listener.lookupTransform(frame_p, frame_ch, rospy.Time(0))
  return p, q
  
def recorder_corners(corners, mode):
  corners = corners.reshape((4,2))
  new_corners = zeros((4,2))
  add = corners.sum(axis = 1)
  subtract = diff(corners, axis = 1)
  if mode == "1243":
    # 1 2
    # 3 4
    new_corners[0] = corners[argmin(add)]
    new_corners[1] = corners[argmin(subtract)]
    new_corners[2] = corners[argmax(subtract)]
    new_corners[3] = corners[argmax(add)]
  elif mode == "1234":
    # 1 2
    # 4 3  
    new_corners[0] = corners[argmin(add)]
    new_corners[1] = corners[argmin(subtract)]
    new_corners[2] = corners[argmax(add)]
    new_corners[3] = corners[argmax(subtract)]
  return new_corners.astype(int)

def pose_2D_to_3D(x_axis, y_axis, z_axis = 'down'):
  if z_axis == 'down':
    z_axis = [0,0,-1,0]
  elif z_axis == 'up':
    z_axis = [0,0,1,0]
  x_axis = list(x_axis) + [0,0]
  y_axis = list(y_axis) + [0,0]
  R = []
  R.append(x_axis)
  R.append(y_axis)
  R.append(z_axis)
  R.append([0,0,0,1])
  R = array(R).T
  q = tf.transformations.quaternion_from_matrix(R)
  return q

def trans_2D_to_3D(p_2D, p_list = [[659, 361], [371, 167], [0.005,-0.005], [-0.195,-0.305]], mode = 'point'):
  p1_2D = p_list[0]
  p2_2D = p_list[1]
  p1_3D = p_list[2]
  p2_3D = p_list[3]
  if mode =='point':
  # p_3Dx = a * p_2Dx + b
  # p_3Dy = c * p_2Dy + d  
    a = float((p1_3D[0] - p2_3D[0])/(p1_2D[0] - p2_2D[0]))
    b = p1_3D[0] - a * p1_2D[0]
    c = float((p1_3D[1] - p2_3D[1])/(p1_2D[1] - p2_2D[1]))
    d = p2_3D[1] - c * p2_2D[1]  
    p_3Dx = a * p_2D[0] + b  
    p_3Dy = c * p_2D[1] + d
    p_3D = [p_3Dx, p_3Dy]
  elif mode == 'scalar':
    d_2D = norm(array(p1_2D)-array(p2_2D))
    d_3D = norm(array(p1_3D)-array(p2_3D))
    p_3D = float(p_2D * d_3D / d_2D)
  return p_3D


def detect_qrcode(frame, h, w, intrinsics = [317.494, 246.239, 607.652, 607.507]):
  blank_image = zeros((h,w), uint8)
  # 640x480
  Cx = intrinsics[0]#317.494
  Cy = intrinsics[1]#246.239
  fx = intrinsics[2]#607.652
  fy = intrinsics[3]#607.507
  mtx = array([[fx, 0, Cx],[0, fy, Cy], [0,0,1]])
  dist=array(([[-5.2706437e-01, 3.21889628e+00, 1.21024516e-03, 4.08411881e-03, -1.78243955e+01]]))
  h1, w1 = frame.shape[:2]
  newcameramtx = mtx
#  newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (h1,w1), 0, (h1, w1))
  frame = cv2.undistort(frame, mtx, None, None, newcameramtx)
	
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#  aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
  dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)	
#  parameters = aruco.DetectorParameters_create()
  parameters =  aruco.DetectorParameters()
  
#  corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
  detector = aruco.ArucoDetector(dictionary, parameters)
  markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(gray)
  
  contours = []
  for i in range(len(markerCorners)):
    contour = markerCorners[i][0].reshape(-1,1,2).astype(int32)
    contours.append(contour)

  return contours, markerIds 


def d_time_ms(t1, t2):
  t = (t2-t1)*1000.0
  print('time: %s ms' % t)
  return t
  
def give_Point(p):
  point = Point32()
  point.x = p[0]
  point.y = p[1]
  point.z = p[2]
  return point
  
def give_PointStamped(frame, p):
  point = PointStamped()
  point.header.frame_id = frame
  point.header.stamp = rospy.Time.now() 
  point.point.x = p[0]
  point.point.y = p[1]
  point.point.z = p[2]
  return point

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

def give_Path(frame, poses):
  path = Path()
  path.header.frame_id = frame#"camera1_color_optical_frame"
  path.header.stamp = rospy.Time.now()
  path.poses = poses
  return path
  
def give_Pose(p,q):
  pose = Pose()
  pose.orientation.x = q[0]
  pose.orientation.y = q[1]
  pose.orientation.z = q[2]
  pose.orientation.w = q[3]
  pose.position.x = p[0]
  pose.position.y = p[1]
  pose.position.z = p[2]
  return pose
  
def give_PoseArray(frame, poses):
  pose = PoseArray()
  pose.header.frame_id = frame
  pose.header.stamp = rospy.Time.now()
  pose.poses = poses #Pose()
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
  
def get_Pose(pose):
  pose = [pose.position.x, 
    pose.position.y, 
    pose.position.z, 
    pose.orientation.x,
    pose.orientation.y,
    pose.orientation.z,
    pose.orientation.w]
  return pose
    
def get_PoseArray(posearray):
  pose_list = []
  for pose in posearray.poses:
    pose_list.append([
      pose.position.x, 
      pose.position.y, 
      pose.position.z, 
      pose.orientation.x,
      pose.orientation.y,
      pose.orientation.z,
      pose.orientation.w
      ]) 
  return pose_list

def get_PointStamped(pointstamped):
  p = [pointstamped.point.x, pointstamped.point.y, pointstamped.point.z]
  return p

def get_Point(point32):
  p = [point32.x, point32.y, point32.z]
  return p
  
def get_control_degree(input_button):
  degree = zeros(6)
  if input_button == 'x':
    degree = [1, 0, 0, 0, 0, 0]
  elif input_button == 'y':
    degree = [0, 1, 0, 0, 0, 0]
  elif input_button == 'z':
    degree = [0, 0, 1, 0, 0, 0]
  elif input_button == 'p':
    degree = [0, 0, 0, 1, 0, 0]
  elif input_button == 'a':
    degree = [0, 0, 0, 0, 1, 0]
  elif input_button == 'r':
    degree = [0, 0, 0, 0, 0, 1]
#  print('input: ' + input_button)
#  print(degree)
  return array(degree)

def get_control_direction(input_button):
  direction = 0
  if input_button == '-':
    direction = -1
  elif input_button == '+':
    direction = 1
#  print('input: ' + input_button)
#  print(direction)
  return direction

# c_T_a =    c_T_b    * b_T_a
# new   =  trans,rot  * old
def transformation_P(v_old,trans,q_rot):
  transform = tf.transformations.quaternion_matrix(q_rot)
  transform[0,3] = trans[0]
  transform[1,3] = trans[1]
  transform[2,3] = trans[2]
  v_old = np.append(v_old,1)
  v_old = v_old.reshape((4,1))
  v_new = np.dot(transform,v_old).T
  return array([v_new[0,0],v_new[0,1],v_new[0,2]])

# c_T_a =    c_T_b    * b_T_a
# new   =  trans,rot  * old
def transformation_Q(q_orig,q_rot):
  q_new = tf.transformations.quaternion_multiply(q_rot,q_orig)
  return array(q_new)

def rot_Q(q_old, q_new):
  transform_old = tf.transformations.quaternion_matrix(q_old)
  transform_new = tf.transformations.quaternion_matrix(q_new)
#  T = dot(inv(transform_old),transform_new)
  T = dot(transform_new,inv(transform_old))
#  T = dot(inv(transform_new),transform_old)
#  T = dot(transform_old,inv(transform_new))
  q_rot = tf.transformations.quaternion_from_matrix(T) 

#  q_old_inv = tf.transformations.quaternion_inverse(q_old)
#  q_rot = tf.transformations.quaternion_multiply(q_new,q_old_inv)
#  q_rot = tf.transformations.quaternion_multiply(q_old_inv,q_new)
  return q_rot

def q_to_angle_axis(q):
  R = tf.transformations.quaternion_matrix(q)
  angle, direc, point = tf.transformations.rotation_from_matrix(R)
  r = np.dot(angle,direc)
  return r

def angle_axis_to_q(r):
  if norm(r) == 0:
    q = array([0,0,0,1])
  else:
    d = norm(r)
    R = tf.transformations.rotation_matrix(d, r/d)
    q = tf.transformations.quaternion_from_matrix(R) 
  return q
  
def xyz_axis_to_q(x_axis, y_axis, z_axis):
  T = tf.transformations.identity_matrix()
  T[0][0:3] = x_axis
  T[1][0:3] = y_axis
  T[2][0:3] = z_axis
  T = array(T)
  q = tf.transformations.quaternion_from_matrix(T.T) 
  return q
    
# weight
def filter3(data, k):
  temp_data = np.zeros(len(data))
  for i in range(1, len(data)):
    temp_data[i-1] = k*data[i-1] + (1-k)*data[i]
  return temp_data
  
  
  
  
  
  
