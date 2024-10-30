#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *



class detect_table:
  def __init__(self):
#=======input==================================================================================
    self.rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
    self.image2_sub = message_filters.Subscriber('/camera/aligned_depth_to_color/image_raw', Image)#, queue_size=2
    self.image2_sub.registerCallback(self.callback_image2) 
#=======output==================================================================================
    self.interest_area_pub = rospy.Publisher("/table_rgb",Image,queue_size=10)
    self.table_frame_pub = rospy.Publisher("/table_frame",PoseStamped,queue_size=1)
    self.point_pub = rospy.Publisher("/table_pc",PointCloud2,queue_size=10)
    self.table_corner_pc_pub = rospy.Publisher("/table_corner_pc",PointCloud2,queue_size=10)
    self.tool_poses_pub = rospy.Publisher("/tool_poses",PoseArray,queue_size=1)
#===============================================================================================
# members
#311.867 254.023 
#369.615 552.456 460.460 520.072 336.453 172.203 245.607 204.587
    self.bridge = CvBridge()
    #self.row = 720
    #self.col = 1280
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.output = np.zeros((self.row,self.col,3), np.uint8)
    self.cv_image2 = np.zeros((self.row,self.col,3), np.uint8)
    self.aruco_l_mm = 33
    self.table_l_mm = 600
    self.table_h_mm = 400
    self.box_l_mm = self.table_l_mm - self.aruco_l_mm
    self.box_h_mm = self.table_h_mm - self.aruco_l_mm
    self.table_corners_mm = float32([[0,0],[self.box_l_mm,0],[self.box_l_mm,self.box_h_mm],[0,self.box_h_mm]])
    self.table_corners_pix = []
    self.table_corners_3d = [] 
    self.p_pre = zeros(3)
    self.q_pre = zeros(4)
    self.p = zeros(3)
    self.q = zeros(4)  
    self.grasp_pix = [[280,189],[280, 189]]
    self.handle_pix = [[242,134],[242,134]]
    self.table_center = mean(self.table_corners_mm, axis=0)
    self.z_axis = zeros(3)
    # change the intrinsics
    self.Cx = 317.494
    self.Cy = 246.239
    self.fx = 607.652
    self.fy = 607.507
    self.intrinsics = [self.Cx, self.Cy, self.fx, self.fy]
  
  
  def callback_image2(self, data):
    self.cv_image2 = self.bridge.imgmsg_to_cv2(data, "passthrough")
    cv_image2 = self.cv_image2
    colNum = data.width
    rowNum = data.height
    scale = 1000.0##mm  scale = 1000 # mm->m
    step = 10
    pointsNum = 0

    Cx = self.Cx
    Cy = self.Cy
    fx = self.fx
    fy = self.fy
#    edge_bias = 0.0 #calibration
    depth_img = []
    for i in range(0,rowNum,step):
      for j in range(0,colNum,step):
        d = cv_image2[i][j]
        r = int(self.blank_image[i,j][0])
        g = int(self.blank_image[i,j][1])
        b = int(self.blank_image[i,j][2])
        a = 255
        rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
        pt = [(float(j)-Cx)*d/fx/scale,(float(i)-Cy)*d/fy/scale,float(d)/scale,rgb]
        depth_img.append(pt)
        pointsNum = pointsNum +1 
#    print ('pointsNum = ' + str(pointsNum))
    HEADER = Header()
    HEADER.frame_id = 'camera_color_optical_frame'
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = depth_img#list
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.point_pub.publish(outputPoints)
 
    depth_img = []
    if len(self.table_corners_pix) == 4:
      table_corners_pix = self.table_corners_pix
      for uv in table_corners_pix:
        i = int(uv[1])
        j = int(uv[0])
        d = cv_image2[i][j]
        r = int(self.blank_image[i,j][0])
        g = int(self.blank_image[i,j][1])
        b = int(self.blank_image[i,j][2])
        a = 255
        rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
        pt = [(float(j)-Cx)*d/fx/scale,(float(i)-Cy)*d/fy/scale,float(d)/scale,rgb]
        depth_img.append(pt)

    HEADER = Header()
    HEADER.frame_id = 'camera_color_optical_frame'
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = depth_img#list
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.table_corner_pc_pub.publish(outputPoints) 

    table_corners_3d = []   
    if len(self.table_corners_pix) == 4:
      table_corners_pix = self.table_corners_pix
      for uv in table_corners_pix:
        i = int(uv[1])
        j = int(uv[0])
        d = cv_image2[i][j]
        pt = array([(float(j)-Cx)*d/fx/scale,(float(i)-Cy)*d/fy/scale,float(d)/scale])
        table_corners_3d.append(pt)
      self.table_corners_3d = table_corners_3d    
      
#      x_axis = self.table_corners_3d[1]  - self.table_corners_3d[0]
#      y_axis = self.table_corners_3d[3] - self.table_corners_3d[0]
#      z_axis = cross(x_axis, y_axis)      
      x_axis = -self.table_corners_3d[0] - self.table_corners_3d[3] + self.table_corners_3d[1] + self.table_corners_3d[2]
      y_axis = self.table_corners_3d[0] + self.table_corners_3d[1] - self.table_corners_3d[2] - self.table_corners_3d[3]
      z_axis = cross(self.table_corners_3d[3] - self.table_corners_3d[1], self.table_corners_3d[2] - self.table_corners_3d[0])
      
      x_axis = x_axis/norm(x_axis)
      y_axis = y_axis/norm(y_axis)
      z_axis = z_axis/norm(z_axis)
      self.z_axis = z_axis
      self.p = mean(self.table_corners_3d,axis=0)
      T = identity(4)
      T[0:3,0] = x_axis
      T[0:3,1] = y_axis
      T[0:3,2] = z_axis
      T[0:3,3] = self.p
      self.q = tf.transformations.quaternion_from_matrix(T)
      
      '''  
      k_p = 0.8self.table_center_bias
      self.p = k_p * self.p_pre + (1-k_p) * self.p
      k_q = 0.8
      self.q = k_q * self.q_pre + (1-k_q) * self.qself.table_center_bias
      '''
      
      self.p_pre = self.p
      self.q_pre = self.q                
    table_frame = give_PoseStamped("camera_color_optical_frame", self.q, self.p)  
    if table_frame.pose.position.z > 0.1:
      self.table_frame_pub.publish(table_frame)

    
  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    intrinsics = self.intrinsics
    contours, ids = detect_qrcode(self.blank_image, self.row, self.col, intrinsics)
    if len(contours) == 4:
      '''
      self.table_corners_pix = array([contours[3][2], contours[1][2], contours[0][2], contours[2][3]])
      print("2")
      print(self.table_corners_pix)
      '''
      self.table_corners_pix = array([mean(contours[0],axis=0).astype(int),  mean(contours[1],axis=0).astype(int),  mean(contours[2],axis=0).astype(int), mean(contours[3],axis=0).astype(int)])
      self.table_corners_pix = recorder_corners(self.table_corners_pix, mode = "1234")
      # draw aruco results
      if ids is not None:
        aruco.drawDetectedMarkers(self.blank_image, contours, ids) # rgb image with green contours
      # draw table area
      self.output = cv2.drawContours(self.blank_image, [self.table_corners_pix], 0, (0,255,0),3)
      self.interest_area_pub.publish(self.bridge.cv2_to_imgmsg(self.output, "passthrough"))
      # compute projection
      self.table_corners_pix = float32(self.table_corners_pix)
      '''
      table_corners_3d_temp = array(self.table_corners_3d)[:,0:2]*1000.0
      table_corners_3d_temp_bias = array(min(table_corners_3d_temp[:,0]), min(table_corners_3d_temp[:,1]))
      table_corners_3d_temp[:,0] = table_corners_3d_temp[:,0] - min(table_corners_3d_temp[:,0])
      table_corners_3d_temp[:,1] = table_corners_3d_temp[:,1] - min(table_corners_3d_temp[:,1])
      print(table_corners_3d_temp)
      '''
      matrix = cv2.getPerspectiveTransform(src=self.table_corners_pix, dst=self.table_corners_mm)
      '''
      self.output = cv2.warpPerspective(self.output,matrix,(self.col,self.row))
      self.interest_area_pub.publish(self.bridge.cv2_to_imgmsg(self.output, "passthrough"))
      '''
      corners = zeros((4,3))
      for i in range(len(self.table_corners_pix)):
        p = self.table_corners_pix[i]
        p_2d = list(p) + [1]     
        pp = dot(p_2d,matrix.T)
        corners[i,0:2] = pp[0:2]/pp[2]/1000.0
    #    corners[i,2] = self.p[-1] 
       
      scale = 1000.0
      cv_image2 = self.cv_image2
      poses = []
      center_bias = array(self.table_corners_3d[0])*scale
      #center_bias = array([]
      for i in range(len(self.grasp_pix)):
        i = 0
        g_pix = array(self.grasp_pix[i] + [1])#self.grasp_pix[i]
        temp = dot(g_pix,matrix.T)
        g_xy = temp[0:2]/temp[2] + center_bias[0:2]
        g_d = cv_image2[int(g_pix[1])][int(g_pix[0])]
        g_3d = array([g_xy[0]/scale,g_xy[1]/scale,float(g_d)/scale])
        h_pix = array(self.handle_pix[i] + [1])
        temp = dot(h_pix,matrix.T)
        h_xy = temp[0:2]/temp[2] + center_bias[0:2]
        h_d = cv_image2[int(h_pix[1])][int(h_pix[0])]
        h_3d = array([h_xy[0]/scale,h_xy[1]/scale,float(h_d)/scale])
        x_axis = h_3d - g_3d  # x_axis of grasp target
        z_axis = -self.z_axis # align target z_axis with table  z_axis
        y_axis = cross(z_axis, x_axis)
        T = identity(4)
        T[0:3,0] = x_axis/norm(x_axis)
        T[0:3,1] = y_axis/norm(y_axis)
        T[0:3,2] = z_axis/norm(z_axis)
        T[0:3,3] = g_3d
        q = tf.transformations.quaternion_from_matrix(T)        
        #q = trans_v_to_q(v)
        pose = give_Pose(g_3d,q)
        poses.append(pose)
      poses_to_pub = give_PoseArray("camera_color_optical_frame", poses)
      self.tool_poses_pub.publish(poses_to_pub)

      
      # compute table frame
    else:
      print(str(time.time())+" less than four aruco")  
      self.interest_area_pub.publish(self.bridge.cv2_to_imgmsg(self.blank_image, "passthrough"))
      
# class end=========================================================================================




def main(args):
 
  
  
  rospy.init_node('detect_table', anonymous=True)
  dt = detect_table()



  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)





