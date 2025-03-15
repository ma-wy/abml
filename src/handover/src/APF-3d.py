#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import sys 
sys.path.append("/home/shunlei/zoe_ws/lib")
from mwy_lib import *

from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import numpy as np
# Parameters
KP = 5.0  # attractive potential gain
ETA = 500.0  # repulsive potential gain
# 500 1.4958 - 24083.951
# 100 0.29915188390155495 - 4875.950997288746

AREA_WIDTH = 10.0  # potential area width [m]
# the number of previous positions used to check oscillations
OSCILLATIONS_DETECTION_LENGTH = 3

def generate_hand_info(config=1):
  p0 = [12.0,3.0]
  p1 = [7.0,7.0]
  p2 = [6.0,10.0]
  p3 = [5.0,13.0]
  p4 = [3.0,16.0]
  p5 = [9.0,14.0]
  p6 = [8.0,17.0]
  p7 = [7.0,21.0]
  p8 = [6.0,24.0]
  p9 = [12.0,15.0]
  p10 = [12.0,18.0]
  p11 = [12.0,22.0]
  p12 = [12.0,26.0]
  p13 = [16.0,15.0]
  p14 = [16.0,19.0]
  p15 = [17.0,22.0]
  p16 = [17.0,25.0]
  p17 = [20.0,14.0]
  p18 = [21.0,17.0]
  p19 = [22.0,20.0]
  p20 = [23.0,23.0]
  hand_list = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]
  hand_depth_1 = [15.0]
  hand_depth_2 = [0.0, 0,0,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
  hand_depth_3 = [0.0, 0,1,2,4,0,3,5,6,0,3,5,6,0,3,5,6,0,3,5,6]
  
  
  
  p = []
  if config == 1:
    for point in hand_list:
      p.append(point+hand_depth_1)
  elif config == 2:
    for i in range(len(hand_list)):
      p.append(hand_list[i]+[hand_depth_1[0] + hand_depth_2[i]])
  elif config == 3:
    hand_list[4] = [6,21]
    hand_list[6] = [hand_list[5][0],hand_list[5][1]+3]
    hand_list[7] = [hand_list[5][0],hand_list[5][1]+2]
    hand_list[8] = [hand_list[5][0],hand_list[5][1]]
    hand_list[10] = [hand_list[9][0],hand_list[9][1]+3]
    hand_list[11] = [hand_list[9][0],hand_list[9][1]+2]
    hand_list[12] = [hand_list[9][0],hand_list[9][1]+0]
    hand_list[14] = [hand_list[13][0],hand_list[13][1]+3]
    hand_list[15] = [hand_list[13][0],hand_list[13][1]+2]
    hand_list[16] = [hand_list[13][0],hand_list[13][1]+0]
    hand_list[18] = [hand_list[17][0],hand_list[17][1]+3]
    hand_list[19] = [hand_list[17][0],hand_list[17][1]+2]
    hand_list[20] = [hand_list[17][0],hand_list[17][1]+0]
    for i in range(len(hand_list)):
      p.append(hand_list[i]+[hand_depth_1[0] + hand_depth_3[i]])
      
      
      
  hand_links = [[p[0],p[1]],[p[0],p[5]],[p[5],p[9]],[p[9],p[13]],[p[13],p[17]],[p[1],p[2]],[p[2],p[3]],[p[3],p[4]],[p[5],p[6]],[p[6],p[7]],[p[7],p[8]],[p[9],p[10]],[p[10],p[11]],[p[11],p[12]],[p[13],p[14]],[p[14],p[15]],[p[15],p[16]],[p[17],p[18]],[p[18],p[19]],[p[19],p[20]],[p[0],p[17]]]
  palm = (array(p[0]) +array(p[5])+array(p[17]))/3
  return hand_links, palm


def generate_heatmap_3d(data, X, Y, Z, ug_max, ug_min):
    data = np.array(data).flatten()
   
    fig = go.Volume(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=data,
        isomin=ug_min,  # 设置最小值
        isomax=ug_max,#np.max(data)/500.0,  # 设置最大值
        opacity=0.1,  # 设置透明度
        surface_count=30,  # 表面数量
        colorscale = 'piyg',
    )
    return fig

def generate_two_ends(sx,sy,sz, gx,gy,gz):
    start = go.Scatter3d(x=[sx], y=[sy], z=[sz], mode='markers', marker_symbol = 'x', marker=dict(size=5,))
    goal = go.Scatter3d(x=[gx], y=[gy], z=[gz], mode='markers', marker_symbol = 'x', marker=dict(size=5,))
    return start, goal
    
def generate_path_3d(x,y,z):
    fig = go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color= 'rgb(0, 0, 0)',width=5),)
    return fig
    
def pt(p0, p1, t):
    p0 = np.array(p0)
    p1 = np.array(p1)
    return p0 + t * (p1 - p0)

def d_point_line(p, p0, p1):
    p = np.array(p)
    p0 = np.array(p0)
    p1 = np.array(p1)
    t = np.dot(p - p0, p1 - p0) / np.dot(p1 - p0, p1 - p0)
    if t > 0 and t < 1:
        d = np.linalg.norm(p - pt(p0, p1, t))
    else:  
        d = min(np.linalg.norm(p - p0), np.linalg.norm(p - p1))
    return d, t




def calc_potential_field(gx, gy, gz, ox, oy, oz, ox_line, oy_line, oz_line, reso, rr, sx, sy, sz):
    """ 计算势场图 gx,gy,gz: 目标坐标 ox,oy,oz: 障碍物坐标列表 reso: 势场图分辨率 rr: 机器人半径 sx,sy,sz: 起点坐标 """
    # 确定势场图坐标范围：
    min_hand_x = min(array(ox_line).reshape(2*len(ox_line)))
    min_hand_y = min(array(oy_line).reshape(2*len(oy_line)))
    min_hand_z = min(array(oz_line).reshape(2*len(oz_line)))
    max_hand_x = max(array(ox_line).reshape(2*len(ox_line)))
    max_hand_y = max(array(oy_line).reshape(2*len(oy_line)))
    max_hand_z = max(array(oz_line).reshape(2*len(oz_line)))

    minx = min(sx, min_hand_x) - AREA_WIDTH / 2.0
    miny = min(sy, min_hand_y) - AREA_WIDTH / 2.0
    minz = min(sz, min_hand_z) - AREA_WIDTH / 2.0
    
    maxx = max(sx, max_hand_x) + AREA_WIDTH / 2.0
    maxy = max(sy, max_hand_y) + AREA_WIDTH / 2.0
    maxz = max(sz, max_hand_z) + AREA_WIDTH / 2.0
    
    # 根据范围和分辨率确定格数：
    xw = int(round((maxx - minx) / reso))
    yw = int(round((maxy - miny) / reso))
    zw = int(round((maxz - minz) / reso))

    X, Y, Z = np.mgrid[minx:maxx:reso, miny:maxy:reso, minz:maxz:reso]
    print('field size')
    print(len(X.flatten()))
 
    # calc each potential
    pmap = [[[0.0 for _ in range(zw)] for _ in range(yw)] for _ in range(xw)]
    ug_list = []
    uo_list = []
    for ix in range(xw):
        x = ix * reso + minx   # 根据索引和分辨率确定x坐标

        for iy in range(yw):
            y = iy * reso + miny  # 根据索引和分辨率确定y坐标
            for iz in range(zw):
                z = iz * reso + minz  # 根据索引和分辨率确定z坐标
                ug = calc_attractive_potential(x, y, z, gx, gy, gz)  # 计算引力
                uo = calc_repulsive_potential(x, y, z, ox, oy, oz, ox_line, oy_line, oz_line, rr)  # 计算斥力
                ug_list.append(ug)
                uo_list.append(uo)
                uf = ug + uo
                pmap[ix][iy][iz] = uf
    ug_max = max(ug_list)
    ug_min = min(ug_list)
    
    return pmap, minx, miny, minz, X, Y, Z, ug_max, ug_min

def calc_attractive_potential(x, y, z, gx, gy, gz):
    """ 计算引力势能：1/2*KP*d """
    return 0.5 * KP * np.linalg.norm([x - gx, y - gy, z - gz])
# KP =5 max: 161.05123408406405, min: 0.0, mean: 76.28724281976407

def calc_repulsive_potential(x, y, z, ox, oy, oz, ox_line, oy_line, oz_line, rr):
    """ 计算斥力势能： 如果与最近障碍物的距离dq在机器人膨胀半径rr之内：1/2*ETA*(1/dq-1/rr)**2 否则：0.0 """
    # search nearest obstacle
    minid = -1
    minid_line = -1
    dmin = float("inf")
    dmin_line = float("inf")

    p_num = len(ox)
    l_num = len(ox_line)

    if p_num > 0:
        for i, _ in enumerate(ox):
            d = np.linalg.norm([x - ox[i], y - oy[i], z - oz[i]])
            if dmin >= d:
                dmin = d
                minid = i
    if l_num > 0:              
        for i, _ in enumerate(ox_line):
            d_line ,_ = d_point_line([x, y, z], [ox_line[i][0], oy_line[i][0], oz_line[i][0]], [ox_line[i][1], oy_line[i][1], oz_line[i][1]])
            if dmin_line >= d_line:
                dmin_line = d_line
                minid_line = i

    if dmin > dmin_line:
        dmin = dmin_line
        minid = minid_line
        # calc repulsive potential
        dq = dmin_line
    else:
        # calc repulsive potential
        dq = dmin

    if dq <= rr:
        if dq <= 0.1:
            dq = 0.1

        return 0.5 * ETA * (1.0 / dq - 1.0 / rr) ** 2
    else:
        return 0.0

def get_motion_model(config = 1):
    # dx, dy, dz
    # 27个可能的运动方向
    if config == 1:
        motion = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [-1, 0, 0],
                  [0, -1, 0],
                  [0, 0, -1],
                  [-1, -1, -1],
                  [-1, -1, 0],
                  [-1, -1, 1],
                  [-1, 0, -1],
                  [-1, 0, 0],
                  [-1, 0, 1],
                  [-1, 1, -1],
                  [-1, 1, 0],
                  [-1, 1, 1],
                  [0, -1, -1],
                  [0, -1, 0],
                  [0, -1, 1],
                  [0, 0, -1],
                  [0, 0, 1],
                  [0, 1, -1],
                  [0, 1, 0],
                  [0, 1, 1],
                  [1, -1, -1],
                  [1, -1, 0],
                  [1, -1, 1],
                  [1, 0, -1],
                  [1, 0, 0],
                  [1, 0, 1],
                  [1, 1, -1],
                  [1, 1, 0],
                  [1, 1, 1]]
    elif config == 2:
        motion = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [-1, 0, 0],
                  [0, -1, 0],
                  [-1, -1, 0],
                  [-1, -1, 1],
                  [-1, 0, 0],
                  [-1, 0, 1],
                  [-1, 1, 0],
                  [-1, 1, 1],
                  [0, -1, 0],
                  [0, -1, 1],
                  [0, 0, 1],
                  [0, 1, 0],
                  [0, 1, 1],
                  [1, -1, 0],
                  [1, -1, 1],
                  [1, 0, 0],
                  [1, 0, 1],
                  [1, 1, 0],
                  [1, 1, 1]]

    return motion


def oscillations_detection(previous_ids, ix, iy, iz):
    """ 振荡检测：避免“反复横跳” """
    previous_ids.append((ix, iy, iz))

    if (len(previous_ids) > OSCILLATIONS_DETECTION_LENGTH):
        previous_ids.popleft()

    # check if contains any duplicates by copying into a set
    previous_ids_set = set()
    for index in previous_ids:
        if index in previous_ids_set:
            return True
        else:
            previous_ids_set.add(index)
    return False

def potential_field_planning(sx, sy, sz, gx, gy, gz, ox, oy, oz, ox_line, oy_line, oz_line, reso, rr):
    # calc potential field
    pmap, minx, miny, minz, X, Y, Z, ug_max, ug_min = calc_potential_field(gx, gy, gz, ox, oy, oz, ox_line, oy_line, oz_line, reso, rr, sx, sy, sz)

    # search path
    d = np.linalg.norm([sx - gx, sy - gy, sz - gz])
    ix = round((sx - minx) / reso) # start
    iy = round((sy - miny) / reso)
    iz = round((sz - minz) / reso)
    gix = round((gx - minx) / reso) # goal
    giy = round((gy - miny) / reso)
    giz = round((gz - minz) / reso)

    rx, ry, rz = [sx], [sy], [sz]
    previous_ids = deque()
    hand_x = array(ox_line).reshape(2*len(ox_line))
    hand_y = array(oy_line).reshape(2*len(oy_line))
    hand_z = array(oz_line).reshape(2*len(oz_line))
    hand_x_min = min(hand_x)
    hand_y_min = min(hand_y)
    hand_z_min = min(hand_z)
    
    while d >= reso:
        minp = float("inf")
        minix, miniy, miniz = -1, -1, -1
        # 寻找27个运动方向中势场最小的方向
        if any([p_x > min(gx,rx[-1]) and p_x < max(gx,rx[-1]) for p_x in hand_x]) or any([p_y > min(gy,ry[-1]) and p_y < max(gy,ry[-1]) for p_y in hand_y]):
            motion = get_motion_model(config=2)
            for i, _ in enumerate(motion):
                inx = int(ix + motion[i][0])
                iny = int(iy + motion[i][1])
                inz = int(iz + motion[i][2])
                if inx >= len(pmap) or iny >= len(pmap[0]) or inz >= len(pmap[0][0]) or inx < 0 or iny < 0 or inz < 0:
                    p = float("inf")  # outside area
                    #print("outside potential!")
                else:
                    p = pmap[inx][iny][inz]
                if minp > p:
                    minp = p
                    minix = inx
                    miniy = iny
                    miniz = inz
        else:
            motion = get_motion_model(config=1)
            for i, _ in enumerate(motion):
                inx = int(ix + motion[i][0])
                iny = int(iy + motion[i][1])
                inz = int(iz + motion[i][2])
                if inx >= len(pmap) or iny >= len(pmap[0]) or inz >= len(pmap[0][0]) or inx < 0 or iny < 0 or inz < 0:
                    p = float("inf")  # outside area
                    #print("outside potential!")
                else:
                    p = pmap[inx][iny][inz]
                if minp > p:
                    minp = p
                    minix = inx
                    miniy = iny
                    miniz = inz
        ix = minix
        iy = miniy
        iz = miniz
        xp = ix * reso + minx
        yp = iy * reso + miny
        zp = iz * reso + minz
        d = np.linalg.norm([gx - xp, gy - yp, gz - zp])
        rx.append(xp)
        ry.append(yp)
        rz.append(zp)
        # 振荡检测，以避免陷入局部最小值：
        if (oscillations_detection(previous_ids, ix, iy, iz)):
            print("Oscillation detected at ({},{},{})!".format(ix, iy, iz))
            break

    print("Goal!!")

    return rx, ry, rz, pmap, ix, iy, iz, gix, giy, giz, X, Y, Z, ug_max, ug_min


    
def main():
    t1 = time.time()
    print("potential_field_planning start")
    start = [[0.0, 10.0, 20],[10.0, 30.0, 20], [10.0, -10.0, 10], [10.0, -10.0, 20]]
    sx = 10.0  # start x position [m]
    sy = -10.0  # start y positon [m]
    sz = 20.0  # start z position [m]
    gx = 30.0  # goal x position [m]
    gy = 30.0  # goal y position [m]
    gz = 15.0  # goal z position [m]
    grid_size = 0.5  # potential grid size [m]
    robot_radius = 5.0  # robot radius [m]
    ox = [15.0, 32.0]  # obstacle x position list [m]
    oy = [25.0, 27.0]  # obstacle y position list [m]
    oz = [5.0, 10.0]  # obstacle z position list [m]
    ox = [12.0, 15.0, 19.0, 28.0, 27.0, 23.0, 30.0, 32.0]  # obstacle x position list [m]
    oy = [12.0, 20.0, 29.0, 28.0, 26.0, 25.0, 28.0, 27.0]  # obstacle y position list [m]
    oz = [5.0, 10.0, 8.0, 20.0, 13.0, 18.0, 18.0, 10.0]  # obstacle z position list [m]
    ox_line = [[15.0, 5.0],[20.0, 25.0]]
    oy_line = [[25.0, 15.0],[26.0, 25.0]]
    oz_line = [[5.0, 10.0],[15.0, 10.0]]
    hand_links, palm = generate_hand_info(config=3)
    gx = palm[0]  # goal x position [m]
    gy = palm[1]  # goal y position [m]
    gz = palm[2]  # goal z position [m]

    ox = []
    oy = []
    oz = []

    
    ox_line = []
    oy_line = []
    oz_line = []
    
    for i in range(len(hand_links)):
      ox_line.append([hand_links[i][0][0],hand_links[i][1][0]])
      oy_line.append([hand_links[i][0][1],hand_links[i][1][1]])
      oz_line.append([hand_links[i][0][2],hand_links[i][1][2]])
      
      
    # path generation
    rx, ry, rz, pmap, ix, iy, iz, gix, giy, giz, X, Y, Z, ug_max, ug_min = potential_field_planning(
        sx, sy, sz, gx, gy, gz, ox, oy, oz, ox_line, oy_line, oz_line, grid_size, robot_radius)

    t2 = time.time()
    print(d_time_ms(t1, t2))

    # 使用 plotly 绘制势场图
    
    #save pmap, X.flatten(), rx
    ''' 
    for i in array(pmap).flatten():
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/pmap.txt')
 
    for i in X.flatten():
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/X.txt')
    for i in Y.flatten():
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/Y.txt')
    for i in Z.flatten():
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/Z.txt')

    for i in rx:
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/rx.txt')
    for i in ry:
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/ry.txt')
    for i in rz:
      saveDataStep([i], '/home/shunlei/zoe_ws/src/test_code/rz.txt')
    '''  
    

    heatmap = generate_heatmap_3d(pmap, X, Y, Z, ug_max, ug_min)
    path = generate_path_3d(rx, ry, rz)
    p_s, p_e = generate_two_ends(sx,sy,sz, gx,gy,gz)
    fig = go.Figure()
    fig.add_trace(heatmap)
    fig.add_trace(path)
    fig.add_trace(p_s)
    fig.add_trace(p_e)
    fig.show()

    
if __name__ == '__main__':
    print(__file__ + " start!!")
    main()
    print(__file__ + " Done!!")
    
    
    
    
    
    
    
    
    
    
    

