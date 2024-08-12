# Calibration
* Reset TCP at flange. Make sure   
* Set speed < 30%  
__step 1:__ run UR  
`$ roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=169.254.162.54`  
__step 2:__ connect NDI  
`$ rosrun ndi tool_tracking P9-01872.local`  
__step 3:__ publish and check tool frame
`$ rosrun ndi tool_frame`  
Output: /robot\_ref\_frame  
`$ rviz`  
__step 4:__ calibrate the tool to the end-effector  
`$ rosrun ndi calibration_rr_to_ee`   
* Make sure the end-effector's position doesn't change.  
* Only change the end-effector's orientation on the UR control panel.  
* The result is saved in  
`/home/abml/ndi_ws/src/ndi/calibration/rf_ee.txt`  
7 coordinates of the result: 
1-3 local, 4-6 global, 7 error  
__step 5:__ calibrate the opical track system to the robot base  
`$ rosrun ndi calibration_ots_to_rb`  
* Randomly change the pose of the end-effector by changing ee position and 6 joints on the UR control panel.  
* The result is saved in  
`/home/abml/ndi_ws/src/ndi/calibration/T_ots_to_rb.txt`  
__step 6:__ publish transformation between ost and robot base as tf    
`$ rosrun ndi static_frame`  
Output: /ost  

# Notes
__API__  
/home/abml/Downloads/Combined API Sample C++ v1.9.7.zip  
__NDI Toolbox__  
/opt/NDIToolBox  
Run GUI  
`$ cd /opt/NDIToolBox`  
`$ ./Tack`  
Load .rom file for the particular equipment with markers  
__ROS Package__  
by Yitian  

