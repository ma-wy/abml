#!/usr/bin/env python2.7
import sys 
sys.path.append("/home/mawanyu/MAws/lib")
from mwy_lib import *
from mwy_path import *

class image_converter:
  def __init__(self):
#=======input==================================================================================
    self.obj_sub = rospy.Subscriber('/filterPoints_1', PointCloud2, self.callback_obj)
    self.center_sub = rospy.Subscriber('/CenterResult', PointStamped, self.callback_center)
    self.radius_sub = rospy.Subscriber('/RadiusResult', Float32, self.callback_radius)
    self.normal_v_sub = rospy.Subscriber("/NormalResult",Vector3Stamped, self.callback_normal_v)
#=======output==================================================================================
    self.point_pub = rospy.Publisher("/order_points",PointCloud2,queue_size=10)
    self.vector_pub = rospy.Publisher("/left_to_right",PoseStamped,queue_size=1)
    self.obj_pose_arr_pub = rospy.Publisher("/obj_pose_arr",PoseArray,queue_size=10)
    file_name = '/home/mawanyu/MAws/src/packing/temp/target_shape.txt'
    f = open(file_name)
    self.shape = f.read()
    f.close()
#===============================================================================================
# members
    self.radius = 0.0
    self.center = [0,0,0]
    self.normal = [0,0,1]
    self.normal2vis = PoseStamped()
    (self.base,q_rot) = get_tf('/camera1_color_optical_frame', '/base')
# rosrun tf tf_echo camera1_color_optical_frame base
# functions

  def callback_radius(self,data):
    self.radius = data.data

  def callback_center(self,data):
    self.center[0] = data.point.x
    self.center[1] = data.point.y
    self.center[2] = data.point.z
    self.center = np.array(self.center)

  def callback_normal_v(self,data):
    self.normal[0] = data.vector.x
    self.normal[1] = data.vector.y
    self.normal[2] = data.vector.z
    self.normal = np.array(self.normal)

  def callback_obj(self,data):
    mark1=time.time()
    points = []
    for pt in point_cloud2.read_points(data):
      points.append([pt[0],pt[1],pt[2]])
    P = np.array(points, dtype=np.float32) 
    d_c = 0
    center = array(self.base)
    for pt in P:
      d_c = d_c + norm(pt-center)
    radius = d_c/len(P[:,0])
#    normal = self.normal
    normal = array([0.0,0.0,1.0])
##########################################
    self.normal2vis.header.frame_id = "camera1_color_optical_frame"
    self.normal2vis.header.stamp = rospy.Time.now()
    self.normal2vis.pose.position.x = 0.0
    self.normal2vis.pose.position.y = 0.0
    self.normal2vis.pose.position.z = 0.0
    self.normal2vis.pose.orientation.x = 0.0
    self.normal2vis.pose.orientation.y = 0.0
    self.normal2vis.pose.orientation.z = 0.0
    self.normal2vis.pose.orientation.w = 1.0
    self.vector_pub.publish(self.normal2vis)
##########################################

    angle = []
    x_axis = array([1.0, 0.0, 0.0]) # y axis in camera
    i = 0
    while i<len(P[...,0]):
      pt = P[i,:]
      i = i+1
#      CP = array([pt[0],pt[1],self.base[2]])-array([center[0],center[1],self.base[2]])
      CP = array([pt[0],pt[1],self.base[2]])-array(self.base)
      c = dot(CP,x_axis)/(norm(CP)*norm(x_axis))
      s = sign(dot(cross(x_axis,CP),normal))*norm(cross(x_axis,CP))/(norm(CP)*norm(x_axis))
      angle_c = np.arccos(c)
      if s >= 0: 
        angle.append(angle_c)
      elif s < 0: 
        angle.append(2.0*pi-angle_c)

      if abs(angle_c) < 5.0/180.0*3.14:
        r1 = Rotation.from_euler('z', 90, degrees=True)
        x_axis = r1.apply(x_axis)
        angle = []
        i = 0
    print x_axis

# detect two tips
    tip_angle = 2.0/180*np.pi # degrees
# distance fixed
    delta = 3.0/100 #3cm
    theta = delta / radius

    cut_d = 0.0/100 #1cm
    cut_a = cut_d / radius

    area_num = int((max(angle) - min(angle) -2*tip_angle) / theta)+1
    theta = (max(angle) - min(angle) -2*tip_angle)/area_num
    area_num = area_num + 2
    print
    
    print 'theta = ' + str(theta)
    print 'points number = ' + str(area_num)
    print 'max_angle = ' + str(max(angle))
    print 'min_angle = ' + str(min(angle))
    
    A = [[] for x in range(area_num)]
#    A_index = [[] for x in range(area_num)]
    A_a = [[] for x in range(area_num)]
    i = 0
    for j in range(0,len(P[...,0])):
      pt = P[j]
      a = angle[j]
      if a-min(angle)<=tip_angle+cut_a and a-min(angle) > cut_a:
        i = 0
      elif max(angle)-a<=tip_angle+cut_a and max(angle)-a > cut_a:
        i = area_num-1
      else:
        i = int((a-min(angle)-tip_angle-cut_a)/theta)+1
      if i < area_num:
        A[i].append(pt)
#        A_index[i].append(j)
        A_a[i].append(a)
# generate skeleton points with gradient color map 
    A_len = np.zeros(area_num)
    pt = np.zeros(4)
    p = []
#    p = np.zeros((area_num,4))
#    clr_s = [46,255,255] # light blue
    clr_s = [255,57,146] # pink
#    clr_e = [255,0,0] # red
    clr_e = [0,0,200] # dark blue
#    clr_s = [0,0,0] #black
#    r = arange(0,255,int(256/area_num))
#    g = arange(0,255,int(256/area_num))
#    b = arange(0,255,int(256/area_num))
#    r = arange(clr_s[0],clr_e[0],(clr_e[0]-clr_s[0])/area_num)
#    g = arange(clr_s[1],clr_e[1],(clr_e[1]-clr_s[1])/area_num)
#    b = arange(clr_s[2],clr_e[2],(clr_e[2]-clr_s[2])/area_num)
    a = 255

    for i in range(area_num):
      A_len[i] = len(A[i])
      r = clr_s[0] + int(float(clr_e[0]-clr_s[0])/area_num*i)
      g = clr_s[1] + int(float(clr_e[1]-clr_s[1])/area_num*i)
      b = clr_s[2] + int(float(clr_e[2]-clr_s[2])/area_num*i)
      if len(A[i]) > 0:
        for j in range(3):
          pt[j] = np.mean(np.array(A[i])[...,j])
        rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]
        pt[3] = rgb
        p.append(list(pt))
      else:
        continue

    print A_len

####################################################
    HEADER = Header()
    HEADER.frame_id = 'camera1_color_optical_frame'
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = list(p)#list
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.point_pub.publish(outputPoints)
    mark2=time.time()
    print 'Order points: '+ str((mark2-mark1)*1000) +' ms'
########################################################
    obj_pose_arr = PoseArray()
    obj_pose_arr.header.frame_id = "camera1_color_optical_frame"
    obj_pose_arr.header.stamp = rospy.Time.now()


    p = array(p)
    for i in range(len(p)-1):
      z = (0,0,1)
      y = cross(p[i+1,0:3]-p[i,0:3],z)
      x = cross(z,y)
      vec1 = (1,0,0)
      vec2 = x
      angle = np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
      axis = np.cross(vec1,vec2)
      if math.isnan(angle) == True:
        angle = 0.0
        axis = array([0.0, 0.0, 1.0])
      if abs(angle - int(angle/3.14)*3.14) < 0.01:
        axis = array([0.0, 0.0, 1.0])
      q = tf.transformations.quaternion_about_axis(angle, axis)
      obj_pose = Pose()
      obj_pose.position.x = p[i,0]
      obj_pose.position.y = p[i,1]
      obj_pose.position.z = p[i,2]
      obj_pose.orientation.x = q[0]
      obj_pose.orientation.y = q[1]
      obj_pose.orientation.z = q[2]
      obj_pose.orientation.w = q[3]
      obj_pose_arr.poses.append(obj_pose)
    obj_pose = Pose()
    obj_pose.position.x = p[-1,0]
    obj_pose.position.y = p[-1,1]
    obj_pose.position.z = p[-1,2]
    obj_pose.orientation.x = q[0]
    obj_pose.orientation.y = q[1]
    obj_pose.orientation.z = q[2]
    obj_pose.orientation.w = q[3]
    obj_pose_arr.poses.append(obj_pose)
    self.obj_pose_arr_pub.publish(obj_pose_arr)




# class end=========================================================================================
def main(args):
  rospy.init_node('line_order', anonymous=True)
  ic = image_converter()

  try:
#    while not rospy.is_shutdown():
#      ic.vector_pub.publish(ic.normal2vis)
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)

