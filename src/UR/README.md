# UR Packages  
Donnot use ros-industrial version!  
## ur_modern_driver  
`git clone -b iron-kinetic-devel https://github.com/iron-ox/ur_modern_driver.git`  
### Notes:  
In the file `src/ur_hardware_interface.cpp`, replace `controller_it->hardware_interface` with `controller_it->type`.

## universal_robot  
`git clone -b calibration_devel https://github.com/rxjia/fmauch_universal_robot.git`  
### Notes:  
1. Under the path `path/to/universal_robot-melodic-devel`,  
![] (https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/1.png) 

| right | wrong |  
| --- | --- |   
| <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/1.png align=center /> | ./markdown_source/3.png |  

2. Under the path `path/to/universal_robot-melodic-devel/ur5_moveit_config/config`,   

| right | wrong |    
| --- | --- |   
| ![] (./markdown_source/2.png) | ![] (./markdown_source/4.png) |  

3. In the file `controllers.yaml`  

| right | wrong |    
| --- | --- |   
| ![] (./markdown_source/5.png) | ![] (./markdown_source/6.png) |  

4. Under the path `path/to/universal_robot-melodic-devel/ur5_moveit_config/launch`, if `moveit_rviz.launch` cannot run correctly, replace the content with ros-industrial verion.

## Useage:  
`$ roslaunch roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=169.254.162.54`  
`$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch`  
`$ roslaunch ur5_moveit_config moveit_rviz.launch`  
