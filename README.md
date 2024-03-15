## commands  

## launch structure  
1. old:  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
new:  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  
> panda\_moveit\_config franka_control.launch
>> include 2 launch files   
>>>1. (old) $(find franka\_control)/launch/franka_control.launch  
>>>1. (new) $(dirname)/franka\_control\_in\_franka_ros.launch  
>>>> include: launch files:  
>>>>>1. $(find franka\_gripper)/launch/franka_gripper.launch  
>>>> include: nodes:  
>>>>>1. pkg="franka\_control" type="franka\_control_node"  
>>>>>2. pkg="controller_manager" type="spawner" respawn="false"  
>>>>>3. pkg="robot\_state\_publisher" type="robot\_state_publisher"  
>>>>>4. pkg="joint\_state\_publisher" type="joint\_state_publisher"   
>>>2. $(find panda\_moveit\_config)/launch/ros_controllers.launch  
>>>>include: node:  
>>>>>1. pkg="controller_manager" type="spawner" respawn="false"  


in "franka_control_in_franka_ros.launch"  
`$ roslaunch zoe_ws franka_control_in_franka_ros.launch robot_ip:=192.168.1.110`  

1. `$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`  
__note:__    
franka\_gripper\_node.cpp: publish the topic /franka_gripper/joint_states  
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
`$ python3 scrubnurseicravideo.py`  


* where is franka_control  
run  
`$ rospack find franka_control`  
output  
>/home/abml/catkin_cl/src/franka_ros/franka_control  
 

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
moveit_commander.move_group.MoveGroupCommander	 
moveit_commander.interpreter.MoveGroupCommandInterpreter	
moveit_commander.interpreter.MoveGroupInfoLevel	 
moveit_commander.planning_scene_interface.PlanningSceneInterface	
moveit_commander.robot.RobotCommander	 






