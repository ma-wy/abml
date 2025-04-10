#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from shapely.geometry import LineString, Point

import plotly.graph_objects as go
import numpy as np
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import unary_union

def plot_shapely_geometries(p_mic, ring, center_line, hand_area_init, hand_area, p_min, p_max):
    # 创建图形对象
    fig = go.Figure()
    # 1. 绘制圆环(ring)
    if ring.geom_type == 'Polygon':
        # 外环
        ext_x, ext_y = ring.exterior.xy
        fig.add_trace(go.Scatter(
            x=deepcopy(array(ext_x)), y=deepcopy(array(ext_y)),
            fill='toself',
            fillcolor='rgba(200,200,200,0.2)',
            line=dict(color='gray', width=2),
            name='Ring'
        ))
        
        # 内环(如果有)
        for interior in ring.interiors:
            int_x, int_y = interior.xy
            fig.add_trace(go.Scatter(
                x=array(int_x), y=array(int_y),
                fill='toself',
                fillcolor='white',
                line=dict(color='gray', width=2),
                showlegend=False
            ))
    
    # 2. 绘制中心线(center_line)
    if center_line:
        print('center_line')
        for i, line in enumerate(center_line, 1):
            x, y = line.xy
            fig.add_trace(go.Scatter(
                x=array(x), y=array(y),
                mode='lines',
                line=dict(color='blue', width=3),
                name=f'Center Line {i}'
            ))
    
    # 3. 绘制初始手部区域(hand_area_init)
    if hand_area_init and not hand_area_init.is_empty:
        print('hand_area_init')
        if hand_area_init.geom_type == 'Polygon':
            ext_x, ext_y = hand_area_init.exterior.xy
            fig.add_trace(go.Scatter(
                x=deepcopy(array(ext_x)), y=deepcopy(array(ext_y)),
                fill='toself',
                fillcolor='rgba(0,255,0,0.3)',
                line=dict(color='green', width=2),
                name='Initial Hand Area'
            ))
    
    # 4. 绘制最终手部区域(hand_area)
    if hand_area and not hand_area.is_empty:
        if hand_area.geom_type == 'Polygon':
            ext_x, ext_y = hand_area.exterior.xy
            fig.add_trace(go.Scatter(
                x=deepcopy(array(ext_x)), y=deepcopy(array(ext_y)),
                fill='toself',
                fillcolor='rgba(255,0,0,0.3)',
                line=dict(color='red', width=2),
                name='Final Hand Area'
            ))
        elif hand_area.geom_type == 'MultiPolygon':
            for i, poly in enumerate(hand_area.geoms, 1):
                ext_x, ext_y = poly.exterior.xy
                fig.add_trace(go.Scatter(
                    x=deepcopy(array(ext_x)), y=deepcopy(array(ext_y)),
                    fill='toself',
                    fillcolor='rgba(255,0,0,0.3)',
                    line=dict(color='red', width=2),
                    name=f'Final Hand Area {i}'
                ))
    # mic            
    fig.add_trace(go.Scatter(
        x=[0, p_mic[0]], y=[0, p_mic[1]],
        mode='lines',
        line=dict(color='brown', width=3),
        name='Mic'
    ))      
    # p_min            
    fig.add_trace(go.Scatter(
        x=[0, p_min[0]], y=[0, p_min[1]],
        mode='lines',
        line=dict(color='red', width=3),
        name='p_min'
    ))      
    # p_max            
    fig.add_trace(go.Scatter(
        x=[0, p_max[0]], y=[0, p_max[1]],
        mode='lines',
        line=dict(color='green+', width=3),
        name='p_max'
    ))        
    # 设置图形布局
    fig.update_layout(
        title='Hand Movement Area Visualization',
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        showlegend=True,
        hovermode='closest'
    )
    
    return fig

# 修改后的主函数
def mic_wrist_mapping(mic_angle_deg):
    wrist_angle = mic_angle_deg - 15.
    return wrist_angle

# 测试数据
p_base = np.zeros(2)
p_mic = np.array([0, 0.4])
a_hum_in_mic = 45.
a_hum_in_base = mic_wrist_mapping(a_hum_in_mic)  # deg
a_base = 0.  # feedback

r_min = 0.4
r_max = 0.8
r_mid = (r_min + r_max)/2

center = (0, 0)  # 假设圆心在原点
inner_radius = r_min
outer_radius = r_max

ref_v = p_mic - p_base

ring = create_ring(center, inner_radius, outer_radius, resolution=32)
slope = np.tan(np.deg2rad(90 - a_hum_in_base))

if (a_hum_in_base > 0. and a_hum_in_base < 90) or (a_hum_in_base > 270. and a_hum_in_base < 360):
    ray = ray_from_point_slope(p_mic, slope, ref_v, length=15)
else:      
    ray = ray_from_point_slope(p_mic, slope, -ref_v, length=15)
center_line = get_overlapping_segments(ray, ring) 
hand_area_init = calculate_swept_area_with_end_circles(center_line[0], 0.4, resolution=32) 
hand_area = hand_area_init.intersection(ring) 
angle_list = []
corners = get_polygon_corners(hand_area)
for p in corners:
  angle_list.append(vector_clockwise_angle(p[0], p[1]))
  
p_min = corners[argmin(angle_list)]
p_max = corners[argmax(angle_list)]
print(p_min)
print(p_max)
# 可视化
fig = plot_shapely_geometries(p_mic, ring, center_line, hand_area_init, hand_area, p_min, p_max)
fig.show()

























