#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import unary_union
import matplotlib.pyplot as plt

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

# 使用示例
if __name__ == "__main__":
    # 创建测试线段
    line = LineString([(1, 1), (4, 1), (7, 3)])
    radius = 1.0
    
    # 计算覆盖范围
    swept_area = calculate_swept_area_with_end_circles(line, radius)
    
    # 可视化
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制原始线段
    x, y = line.xy
    ax.plot(x, y, 'b-', linewidth=2, label='Original Line')
    
    # 绘制覆盖范围边界
    if swept_area.geom_type == 'Polygon':
        ext_x, ext_y = swept_area.exterior.xy
        ax.plot(ext_x, ext_y, 'r-', label='Swept Area')
        ax.fill(ext_x, ext_y, 'r', alpha=0.2)
        
        # 绘制所有内环（如果有）
        for interior in swept_area.interiors:
            int_x, int_y = interior.xy
            ax.plot(int_x, int_y, 'r-')
            ax.fill(int_x, int_y, 'w')
    
    # 标记端点
    ax.plot(line.coords[0][0], line.coords[0][1], 'go', markersize=8, label='Start Point')
    ax.plot(line.coords[-1][0], line.coords[-1][1], 'yo', markersize=8, label='End Point')
    
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
    plt.title(f'Area Swept by Circle (r={radius}) with Full End Circles')
    plt.show()
    
    print(f"覆盖区域面积: {swept_area.area:.2f}")
    print(f"覆盖区域周长: {swept_area.length:.2f}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

