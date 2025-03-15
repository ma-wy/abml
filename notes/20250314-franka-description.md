## Problem:  
__1. rviz: 执行器link_6变红，gripper变成绿色球状组合__
__2. terminal: [ WARN] [1741952425.837718627]: Link 'panda_link0_sc' is not known to URDF. Cannot specify collision default.__  
__3. 如果rviz中移动机械臂，会报错无法plan__  
## Solution:  
删除franka\_ros中的franka\_description  
安装ros自带franka_description: `$ sudo apt install ros-noetic-franka-description`  
更改`franka_ros/franka_control/launch/franka_control.launch`:  
`<param name="robot_description" command="$(find xacro)/xacro $(find franka_description)/robots/panda_arm.urdf.xacro hand:=$(arg load_gripper)" />`  
->  
`<param name="robot_description" command="$(find xacro)/xacro $(find franka_description)/robots/panda/panda.urdf.xacro hand:=$(arg load_gripper)" />`  
