## commands  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  


## launch structure  
old (include MoveIt demo):  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
new (2 launch):  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  
  
1 (old) $(find franka\_control)/launch/franka_control.launch  
1 (new, launch: 1 launch, 4 nodes) $(dirname)/franka\_control\_in\_franka\_ros.launch  
1-1 (launch: 1 node) $(find franka\_gripper)/launch/franka_gripper.launch (1 node)   
1-1-1 (__node__) name="franka\_gripper" pkg="franka\_gripper" type="franka\_gripper\_node"  
1-2 (__node__) name="franka\_control" pkg="franka\_control" type="franka\_control\_node"  
1-3 (__node__) name="state\_controller\_spawner" pkg="controller_manager" type="spawner" respawn="false"  
1-4 (__node__) name="robot\_state\_publisher" pkg="robot\_state\_publisher" type="robot\_state\_publisher"  
1-5 (__node__) name="joint\_state\_publisher" pkg="joint\_state\_publisher" type="joint\_state\_publisher"   

2 (launch: 1 node) $(find panda\_moveit\_config)/launch/ros\_controllers.launch  
arg name="transmission" default="position" passed to 1-2  
2-1 (node) pkg="controller\_manager" type="spawner" respawn="false"  (repeat node 1-3)
> try to remove this launch  


## node info  
1. 1-1-1 gripper   
`$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`  
franka\_gripper\_node.cpp: publish the topic /franka\_gripper/joint\_states   
```
Publications: 
 * /franka_gripper/joint_states [sensor_msgs/JointState] (to node 1-5 joint_state_publisher)
 
 * /franka_gripper/grasp/feedback [franka_gripper/GraspActionFeedback]
 * /franka_gripper/grasp/result [franka_gripper/GraspActionResult]
 * /franka_gripper/grasp/status [actionlib_msgs/GoalStatusArray]
 
 * /franka_gripper/gripper_action/feedback [control_msgs/GripperCommandActionFeedback]
 * /franka_gripper/gripper_action/result [control_msgs/GripperCommandActionResult]
 * /franka_gripper/gripper_action/status [actionlib_msgs/GoalStatusArray]
 
 * /franka_gripper/homing/feedback [franka_gripper/HomingActionFeedback]
 * /franka_gripper/homing/result [franka_gripper/HomingActionResult]
 * /franka_gripper/homing/status [actionlib_msgs/GoalStatusArray]

 * /franka_gripper/move/feedback [franka_gripper/MoveActionFeedback]
 * /franka_gripper/move/result [franka_gripper/MoveActionResult]
 * /franka_gripper/move/status [actionlib_msgs/GoalStatusArray]
 
 * /franka_gripper/stop/feedback [franka_gripper/StopActionFeedback]
 * /franka_gripper/stop/result [franka_gripper/StopActionResult]
 * /franka_gripper/stop/status [actionlib_msgs/GoalStatusArray]

Subscriptions: 
 * /franka_gripper/grasp/cancel [unknown type]
 * /franka_gripper/grasp/goal [unknown type]
 * /franka_gripper/gripper_action/cancel [unknown type]
 * /franka_gripper/gripper_action/goal [unknown type]
 * /franka_gripper/homing/cancel [unknown type]
 * /franka_gripper/homing/goal [unknown type]
 * /franka_gripper/move/cancel [unknown type]
 * /franka_gripper/move/goal [unknown type]
 * /franka_gripper/stop/cancel [unknown type]
 * /franka_gripper/stop/goal [unknown type]

Services: 
 * /node_name/get_loggers, set_logger_level  
```
 
2. 1-2 name="franka\_control" pkg="franka\_control" type="franka\_control_node"   
```
Publications:   
 * /franka_control/error_recovery/feedback [franka_msgs/ErrorRecoveryActionFeedback]  
 * /franka_control/error_recovery/result [franka_msgs/ErrorRecoveryActionResult]  
 * /franka_control/error_recovery/status [actionlib_msgs/GoalStatusArray]  
 
 * /franka_state_controller/F_ext [geometry_msgs/WrenchStamped]  
 * /franka_state_controller/franka_states [franka_msgs/FrankaState]  
 * /franka_state_controller/joint_states [sensor_msgs/JointState] (to node 1-5 joint_state_publisher) 
 * /franka_state_controller/joint_states_desired [sensor_msgs/JointState]  
 
 * /tf [tf2_msgs/TFMessage]  

Subscriptions:   
 * /franka_control/error_recovery/cancel [unknown type]  
 * /franka_control/error_recovery/goal [unknown type]  

Services: 
 * /node_name/get_loggers, set_logger_level   
 
 * /controller_manager/list_controller_types  
 * /controller_manager/list_controllers  
 * /controller_manager/load_controller  
 * /controller_manager/reload_controller_libraries  
 * /controller_manager/switch_controller  
 * /controller_manager/unload_controller  
 * /franka_control/connect  
 * /franka_control/disconnect   
 * /franka_control/set_EE_frame  
 * /franka_control/set_K_frame   
 * /franka_control/set_cartesian_impedance  
 * /franka_control/set_force_torque_collision_behavior  
 * /franka_control/set_full_collision_behavior  
 * /franka_control/set_joint_impedance  
 * /franka_control/set_load  
```

3. 1-3 name="state\_controller\_spawner" pkg="controller_manager" type="spawner" respawn="false"  
```  
Publications: X
Subscriptions: X
Services: X
 * /node_name/get_loggers, set_logger_level  
```

4. 1-4 name="robot\_state\_publisher" pkg="robot\_state\_publisher" type="robot\_state_publisher"  
```
Publications:    
 * /tf [tf2_msgs/TFMessage]  
 * /tf_static [tf2_msgs/TFMessage] 
Subscriptions:   
 * /joint_states [sensor_msgs/JointState]  (from node 1-5 joint_state_publisher)
Services: X
 * /node_name/get_loggers, set_logger_level
```

5. 1-5 name="joint\_state\_publisher" pkg="joint\_state\_publisher" type="joint\_state_publisher"   
```
Publications:  
 * /joint_states [sensor_msgs/JointState] (to node 1-4 robot_state_publisher) 
Subscriptions:  
 * /franka_gripper/joint_states [sensor_msgs/JointState] (from node 1-1-1 franka_gripper)
 * /franka_state_controller/joint_states [sensor_msgs/JointState] (from node 1-2 franka_control) 
Services: X  
 * /node_name/get_loggers, set_logger_level 
```

## important topic  
* __node 1-1-1__ franka\_gripper -> /franka\_gripper/joint\_states [sensor_msgs/JointState] -> node 1-5 joint\_state\_publisher  

* __node 1-2__ franka\_control -> /franka\_state\_controller/joint\_states [sensor_msgs/JointState] -> node 1-5 joint\_state\_publisher  

* __node 1-5__ joint\_state\_publisher -> /joint\_states [sensor_msgs/JointState] -> node 1-4 robot\_state\_publisher  

* node 1-3 state\_controller\_spawner: services noly  
> What's the function of this node? Try to remove it?  

* packages are under /opt/ros/noetic/share/   
For example:  
run:   
`$ rospack find robot_state_publisher`  
output:  
> /opt/ros/noetic/share/robot\_state\_publisher  

* Definitions of messages are also under this path.  
For example:  
/opt/ros/noetic/share/robot\_state\_publisher/sensor_msgs/JointState.msg  
```
Header header  

string[] name
float64[] position
float64[] velocity
float64[] effort
```

* Show message description  
`$ rosmsg info /msg_name`  
For example:  
`$ rosmsg info sensor_msgs/JointState`  
output:  
```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string[] name
float64[] position
float64[] velocity
float64[] effort
```

1. /franka\_gripper/joint\_states [sensor_msgs/JointState]   
from node 1-1-1 franka\_gripper to node 1-5 joint\_state\_publisher  
run:  
`$ rostopic echo /franka_gripper/joint_states`  
output:  
```
header: 
  seq: 9558
  stamp: 
    secs: 1710421306
    nsecs: 571185133
  frame_id: ''
name: 
  - panda_finger_joint1
  - panda_finger_joint2
position: [-1.8386666852165945e-05, -1.8386666852165945e-05]
velocity: [0.0, 0.0]  
effort: [0.0, 0.0]  
```
This topic publishes the states of the two fingers of the gripper.   
 
2.  /franka\_state\_controller/joint\_states [sensor_msgs/JointState] 
from node 1-2 franka\_control to node 1-5 joint\_state_publisher
```
header: 
  seq: 208206
  stamp: 
    secs: 1710484933
    nsecs: 126548471
  frame_id: ''
name: 
  - panda_joint1
  - panda_joint2
  - panda_joint3
  - panda_joint4
  - panda_joint5
  - panda_joint6
  - panda_joint7
position: [0.89522913440069, 0.44167418931520475, -0.8973612387972845, -2.31483014484874, 0.4912188812295596, 2.2763984821312713, 0.5283940817870442]
velocity: [-0.0007187489802257906, 0.0006938567564774313, 0.000862680079172758, 0.0006432245071607099, -1.2711813091633669e-05, 0.0002131094376944469, -0.00029667792283876864]
effort: [0.17024928331375122, -25.941246032714844, -9.267027854919434, 16.101726531982422, 0.6915948987007141, 1.904165506362915, -0.14393071830272675]
```
 
3. /joint\_states [sensor_msgs/JointState]   
from node 1-5 joint\_state\_publisher to node 1-4 robot\_state\_publisher  
```
header: 
  seq: 220238
  stamp: 
    secs: 1710485183
    nsecs: 689952611
  frame_id: ''
name: 
  - panda_joint1
  - panda_joint2
  - panda_joint3
  - panda_joint4
  - panda_joint5
  - panda_joint6
  - panda_joint7
  - panda_finger_joint1
  - panda_finger_joint2
position: [0.8952338259139105, 0.4416706966237804, -0.8973665285109783, -2.3148277219504196, 0.49121888122955953, 2.2763983280311013, 0.5283901368914931, 0.04010230675339699, 0.04010230675339699]
velocity: [-0.0003650391902504162, 0.0015916082667817475, 0.0008829863979122501, 0.0020634986393326432, -0.00016033748655701753, 0.00031076818906534466, 0.0020899901188669435, 0.0, 0.0]
effort: [0.13057643175125122, -25.901573181152344, -9.191649436950684, 16.066020965576172, 0.6915948987007141, 1.904165506362915, -0.13385991752147675, 0.0, 0.0]
```

## communication  
### Flow  
node 1-1-1 franka\_gripper + node 1-2 franka\_control  
-> node 1-5 joint\_state\_publisher  
-> node 1-4 robot\_state\_publisher  
-> topic /tf [tf2_msgs/TFMessage] + /tf\_static [tf2_msgs/TFMessage]  
### Final output:  
`$ rostopic echo /tf`  
```
transforms: 
      frame_id: "panda_hand"
    child_frame_id: "panda_leftfinger"
      frame_id: "panda_hand"
    child_frame_id: "panda_rightfinger"
      frame_id: "panda_link0"
    child_frame_id: "panda_link1"
      frame_id: "panda_link1"
    child_frame_id: "panda_link2"
      frame_id: "panda_link2"
    child_frame_id: "panda_link3"
      frame_id: "panda_link3"
    child_frame_id: "panda_link4"
      frame_id: "panda_link4"
    child_frame_id: "panda_link5"
      frame_id: "panda_link5"
    child_frame_id: "panda_link6"
      frame_id: "panda_link6"
    child_frame_id: "panda_link7"
      frame_id: "panda_link8"
    child_frame_id: "panda_NE"
      frame_id: "panda_NE"
    child_frame_id: "panda_EE"
      frame_id: "panda_EE"
    child_frame_id: "panda_K"
```  
  
`$ rostopic echo /tf_static`  
```
transforms: 
      frame_id: "panda_link8"
    child_frame_id: "panda_hand"
      frame_id: "panda_hand"
    child_frame_id: "panda_hand_sc"
      frame_id: "panda_hand"
    child_frame_id: "panda_hand_tcp"
      frame_id: "panda_link7"
    child_frame_id: "panda_link8"
      frame_id: "panda_link0"
    child_frame_id: "panda_link0_sc"
      frame_id: "panda_link1"
    child_frame_id: "panda_link1_sc"
      frame_id: "panda_link2"
    child_frame_id: "panda_link2_sc"
      frame_id: "panda_link3"
    child_frame_id: "panda_link3_sc"
      frame_id: "panda_link4"
    child_frame_id: "panda_link4_sc"
      frame_id: "panda_link5"
    child_frame_id: "panda_link5_sc"
      frame_id: "panda_link6"
    child_frame_id: "panda_link6_sc"
```

  
## test   
1. `$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`    
  
2. `$ roslaunch pick-and-place franka_control_in_franka_ros.launch robot_ip:=192.168.1.110`  
This file will kill franka_gripper.launch  
2. `$ rosparam load rosparam load ~/catkin_cl/src/franka_ros/franka_control/config/franka_control_node.yaml subst_value:=true`   

3. `$ rosrun franka_control franka_control_node`  
xxx   


4. `$ rosparam load rosparam load ~/catkin_cl/src/franka_ros/franka_control/config/default_controllers.yaml subst_value:=true`  



----------------------------------------
## notes  
* test communication between franka and pc:  
`$ communication_test 192.168.1.110`  
`$ rosrun libfranka communication_test 192.168.1.110`    
`$ ping 192.168.1.110`  


* commands  
`$ source ./catkin_cl/devel/setup.bash`  
(This command had already been added in the ~/.bashrc)
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ python3 scrubnurseicravideo.py`  run:


* where is franka_control  
run  
`$ rospack find franka_control`  
output  
>/home/abml/catkin\_cl/src/franka\_ros/franka_control  
 

* $(dirname) in the launch file returns the absolute path of this launch file.  
For example:  
`<include file="$(dirname)/other.launch" />`  
Will expect to find other.launch in the same directory as the launch file which it appears in.  


* look for a python module:  
Opend a terminal, run   
`$ python3`   
`help("moveit_commander")`  
press 'q' to exit  

output:  
>/opt/ros/noetic/lib/python3/dist-packages/moveit_commander/\_\_init\_\_.py  

* franka lib source code   
moveit_commander.robot.RobotCommander.Link	 
moveit\_commander.move_group.MoveGroupCommander	 
moveit_commander.interpreter.MoveGroupCommandInterpreter	
moveit_commander.interpreter.MoveGroupInfoLevel	 
moveit\_commander.planning_scene_interface.PlanningSceneInterface	
moveit_commander.robot.RobotCommander	 






