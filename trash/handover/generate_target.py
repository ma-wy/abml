#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

from handover.msg import hand_mp

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.target_sub = rospy.Subscriber('/grasping_uv', Pose, self.callback_grasping_uv)
#=======output==================================================================================
    self.grasping_state_pub = rospy.Publisher("/grasping_state", Bool, queue_size=1)
#===============================================================================================
# members
    self.grasping_uv = zeros(3)
    self.handle_uv = zeros(3)
    self.grapsing_point = zeros(3)
    self.handle_point = zeros(3)
    self.grasping_state = Bool()
    self.grasping_state.data = False
    self.rob = urx.Robot("169.254.162.54")
    self.rob.set_tcp((0, 0, 0, 0, 0, 0))
    self.rob.set_payload(2, (0, 0, 0.1))
    self.a = 0.2
    self.v = 0.3    
    self.z_axis = zeros(3)
    # change the intrinsics 
    self.row = 480
    self.col = 640
    self.Cx = 317.494
    self.Cy = 246.239
    self.fx = 607.652
    self.fy = 607.507
    self.intrinsics = [self.Cx, self.Cy, self.fx, self.fy]
    
    
  def callback_grasping_uv(self, data):
    print('before movement')
    self.grasping_uv[0] = data.orientation.x
    self.grasping_uv[1] = data.orientation.y
    self.handle_uv[0] = data.orientation.z
    self.handle_uv[1] = data.orientation.w
    
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
    
    self.grasping_state.data = True
    self.grasping_state_pub.publish(self.grasping_state)
    
    
    print(rob.getj())
    degree = -10
    joints = [0,0,0,0,0,float(degree)/180.0*numpy.pi]
    rob.movej(joints, acc=a, vel=v, wait=True, relative=True, threshold=None)
    print('after movement')
    print(rob.getj())
    rob.close()    
    
def main(args):
  rospy.init_node('hand_detect', anonymous=True)

  hd = hand_detect()
  

  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
    
if __name__ == '__main__':

    main(sys.argv)
    
    
