## Usage  
### V2  
`$ roslaunch franka_interface interface.launch`  
‵ $ roslaunch move\_franka launch\_tfs.launch`  
`$ roslaunch move_franka launch_tf_subs.launch`  
__Move franka given a camera's pose__  
`$ rosrun move_franka move_to_camera_goal.py`  
To reset:  
`$ rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.40, 0.0, 0.50, 0.707, -0.707, 0.0, 0.0]"`  
__Move franka given an assistant finger's pose__  
`$ rosrun move_franka move_to_ee3_goal.py`  

### V1  
`$ roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda`  
‵ $ roslaunch move\_franka launch\_tfs.launch`  
`$ rosrun move_franka move_franka.py`  
`$ rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.40, 0.0, 0.50, 0.707, -0.707, 0.0, 0.0]"`  

##  

/home/abml/zoe_ws/src/franka_ros_interface/franka_interface/src/franka_interface/arm.py  
from franka_moveit import PandaMoveGroupInterface  


/home/abml/zoe_ws/src/franka_ros_interface/franka_moveit/src/franka_moveit/movegroup_interface.py  
1. import moveit_commander  
2. from franka_moveit import ExtendedPlanningSceneInterface  
class PandaMoveGroupInterface:  
  self._robot = moveit_commander.RobotCommander()
  self._scene = ExtendedPlanningSceneInterface()
  self._arm_group = moveit_commander.MoveGroupCommander("panda_arm")
  try:
    rospy.get_param("/franka_gripper/robot_ip")
    self._gripper_group = moveit_commander.MoveGroupCommander("panda_hand")

  def robot_state_interface(self):  return self._robot  
  def scene(self):  return self._scene  
  def arm_group(self):  return self._arm_group  
  def gripper_group(self):  return self._gripper_group

/opt/ros/noetic/lib/python3/dist-packages/moveit_commander/move_group.py
/home/abml/zoe_ws/src/franka_ros_interface/franka_moveit/src/franka_moveit/extended_planning_scene_interface.py  
class ExtendedPlanningSceneInterface(moveit_commander.PlanningSceneInterface):
