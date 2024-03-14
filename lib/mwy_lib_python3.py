#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

#import sys 
#sys.path.append("/home/mawanyu/MAws/lib")
#from mwy_lib import *


'''
@author: mwy
'''
import sys 
sys.path.append("/home/mawanyu/MAws/lib")
from mwy_path_python3 import *




def fun_step_list(x, k=pow(10,6), thr=0.0015, mode = 'no-diff'):
  dx = [0]
  for i in range(len(x)-1):
    dx.append(x[i+1]-x[i])
  x_s = array([fun_step(i,k,thr,mode) for i in x])
  return x_s,dx

def fun_step(x, k=pow(10,6), thr=0.0015, mode = 'no-diff'):
  try:
    ans = math.exp(k*(x-thr))
    try:
      ans_d = pow(ans+1,2)
    except OverflowError:
      ans_d = float('inf')
    d = -k*ans/ans_d
  except OverflowError:
    ans = float('inf')
    d = -k/float('inf')

  if mode == 'diff':
    return [1/(ans+1), d]
  else:
    return 1/(ans+1)

def remove_label(data_list, label):
  index = []
  data_list = list(data_list)
  while(label in data_list):
    index.append(data_list.index(label))
    data_list.remove(label)
  return index, data_list

def save_file(path, file_name, data_list):
  files = glob.glob(path+'*')
  if path + file_name in files:
    os.remove(file_name)
  for i in data_list:
    if len(shape(data_list)) == 1:
      saveDataStep([i], file_name)
    else:
      saveDataStep(i, file_name)

def rob_obj_img(rob,img, rob_l_r = 'left'):
  rob_box = trans_base2box(rob, rob_l_r)
  rob_pix = trans_3D_to_2D(rob_box[0:2])
  d_min_2D = d_2D(rob_pix, img)
  d_min_3D = trans_2D_to_3D(d_min_2D, mode = 'scalar')
  rob_obj = d_min_3D
  return rob_obj
  
def d_2D(pix_in, img):  
  area = get_interest_area(img)
  d_list = []
  for pix in area:
    d_list.append(norm(array(pix_in)-array(pix)))
  d_min_2D = min(d_list)
  return d_min_2D  
  
def get_interest_area(img):
  row = shape(img)[0]
  col = shape(img)[1]
  area_temp = []
  for j in range(0,row,10):
    for k in range(0,col,10):
      if not (img[j,k]-array([255,255,255])).any():
        area_temp.append([j,k])  
  return area_temp
  
def trans_base2box(rob_p, rob='left'):
  if rob == 'left':
    p = [-0.424,  0.005,  0.00]
    q = [0., 0., 0.70710678,  0.70710678]
  elif rob == 'right':
    p = [0.42,  0.007,  0.00]
    q = [0., 0., -0.70710678, 0.70710678]
  rob_p_box = transformation_P(rob_p,p,q)
  return rob_p_box

def clean_tar(raw_list, tar_seg, seg_index):
  data_num = len(raw_list)
  if not seg_index[0] == 0:
    seg_index = [0] + seg_index
  if not seg_index[-1] == data_num:
    seg_index.append(data_num)
  new_list = zeros((shape(raw_list)[0],shape(raw_list)[1]))
  for i in range(len(seg_index)-1):
    for j in range(seg_index[i],seg_index[i+1]):
      new_list[j,:] = raw_list[random.randint(tar_seg[i][0], tar_seg[i][1])]
  return new_list
    
def trans_2D_to_3D(p_2D, p_list = [[0,0],[1280,720],[-0.690,-0.365],[0.610,0.365]], mode = 'point'):
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
    d = p1_3D[1] - a * p1_2D[1]  
    p_3Dx = a * p_2D[0] + b  
    p_3Dy = c * p_2D[1] + d
    p_3D = [p_3Dx, p_3Dy]
  elif mode == 'scalar':
    d_2D = norm(array(p1_2D)-array(p2_2D))
    d_3D = norm(array(p1_3D)-array(p2_3D))
    p_3D = float(p_2D * d_3D / d_2D)
  return p_3D
        
def trans_3D_to_2D(p_3D, p_list = [[0,0],[1280,720],[-0.690,-0.365],[0.610,0.365]], mode = 'point'):
  p1_2D = p_list[0]
  p2_2D = p_list[1]
  p1_3D = p_list[2]
  p2_3D = p_list[3]
  if mode =='point':
  # p_2Dx = a * p_3Dx + b
  # p_2Dy = c * p_3Dy + d  
    a = float((p1_2D[0] - p2_2D[0])/(p1_3D[0] - p2_3D[0]))
    b = p1_2D[0] - a * p1_3D[0]
    c = float((p1_2D[1] - p2_2D[1])/(p1_3D[1] - p2_3D[1]))
    d = p1_2D[1] - a * p1_3D[1]  
    p_2Dx = a * p_3D[0] + b  
    p_2Dy = c * p_3D[1] + d
    p_2D = [p_2Dx, p_2Dy]
  elif mode == 'scalar':
    d_2D = norm(array(p1_2D)-array(p2_2D))
    d_3D = norm(array(p1_3D)-array(p2_3D))
    p_2D = float(p_3D * d_2D / d_3D)
  return p_2D 

def normalize_seg(v,index):
  num = len(v)
  index = [0] + index + [num]
  result = ones(num)
  for i in range(len(index)-1):
    if mean(v[index[i]:index[i+1]])<0.001:#not any(j > 0.001 for j in v[index[i]:index[i+1]]):
      result[index[i]:index[i+1]] = v[index[i]:index[i+1]]#
    else:
      result[index[i]:index[i+1]] = normalize_list(v[index[i]:index[i+1]])#
  return result
  
def normalize_list(v_list, mode = ''):
  if mode == 'bottom-0':
    return [(i-min(v_list))/(max(v_list)-min(v_list)) for i in v_list]
  else:
    return [i/max(v_list) for i in v_list]


def thres_list(v_list, thr, mode='below'):
  v_list = list(v_list)
  result = []
  for i in v_list:
    result.append(thres(i,thr,mode))
  return result  
    

def thres(v,thr,mode='below'):
  if mode == 'below':
    if v > thr:
      return 0
    else:
      return 1
  elif mode == 'above':
    if v > thr:
      return 1
    else:
      return 0    

def dead_zone(value, threshold):
  if abs(value) < threshold:
    return 0
  else:
    return sign(value)

def ra_from_2v(v_old, v_new):
  axis = cross(v_old/norm(v_old), v_new/norm(v_new))
  axis = axis/norm(axis)
  axis_temp = [abs(axis[0]),abs(axis[1]),abs(axis[2])]
  if any(axis_temp):
    axis_i = argmax(axis_temp)
    axis_new = zeros(3)
    axis_new[axis_i] = 1.0
    angle = sign(axis[axis_i]) * acos(dot(v_old, v_new))
  else:
    axis_new = zeros(3)
    angle = 0.0
  return axis_new, angle


def trans_v_to_q(v):
  vec1 = (1,0,0)
  vec2 = v
  angle = np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
  axis = np.cross(vec1,vec2)
  q = tf.transformations.quaternion_about_axis(angle, axis)
  return q

def transformation_P(v_old,trans,rot):
  transform = tf.transformations.quaternion_matrix(rot)
  transform[0,3] = trans[0]
  transform[1,3] = trans[1]
  transform[2,3] = trans[2]
  v_old = np.append(v_old,1)
  v_old = v_old.reshape((4,1))
  v_new = np.dot(transform,v_old).T
  return array([v_new[0,0],v_new[0,1],v_new[0,2]])

def transformation_Q(q_orig,q_rot):
  q_new = tf.transformations.quaternion_multiply(q_rot,q_orig)
  return array(q_new)      
      
def pq_to_T(p,q):
  R = tf.transformations.quaternion_matrix(q)
  R[0:3,3] = p
  return R      

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
  
def saveDataStep(data, file_path):
  data_list = shorten_data(list(data))
  data_str = clean_data(data_list)
  f = open(file_path, "a")
  f.truncate()
  f.write(data_str)
  f.write('\n')
  f.close()      
      
def q_to_angle_axis(q):
  R = tf.transformations.quaternion_matrix(q)
  angle, direc, point = tf.transformations.rotation_from_matrix(R)
  r = np.dot(angle,direc)
  return r

def angle_axis_to_q(r):
  R = tf.transformations.rotation_matrix(norm(r), r/norm(r))
  q = tf.transformations.quaternion_from_matrix(R) 
  return q      
      
def keep_ee_z(q_now):
  z= array([0,0,-1])
  R = tf.transformations.quaternion_matrix(q_now)
  z_now = array(R[0:3,2])  
  axis_new, angle = ra_from_2v(z_now, z)# old, new    
  ra = axis_new*angle
  q_rot = angle_axis_to_q(ra)
  q = transformation_Q(q_now,q_rot)
  return q





