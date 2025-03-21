# Dataset 1   
## Launch devices and rviz  
__step 1:__ launch UR robot, camera, tfs, and rviz    
`$ roslaunch handover launch_cam_and_rob.launch`  
__step 2:__ run NDI and pulish tool frame and ots frame  
`$ rosrun ndi tool_tracking P9-01872.local`  
## Launch tfs and pubs  
__step 1__: launch tfs   
`$ roslaunch handover launch_tfs.launch`  

| parent frame | child frame |  
| ---          | ---         |
| base_link    | ost         |
| ost          | robot\_ref\_frame |
| base         | camera\_top\_color\_optical\_frame |
| robot\_ref\_frame | handle_frame |
 
__step 2:__ launch tf pubs  
`$ roslaunch handover launch_tf_pubs.launch`  
camera\_to\_base\_pub.py   
handle\_to\_base\_pub.py  

## Start to track hand   
`$ roslaunch handover hand_tracking.launch`  

## Start to save data  
__step 1:__ initialize the robot  
`$ cd /home/abml/zoe_ws/src/handover/src`   
`./ur_init_dataset_1.py`  
__step 2:__ adjust the robot's pose  
`./ur_move_dataset_1.py`  
__step 3:__ revise two params in `save_data.py`:  
  > dataset_num = 1  
  > member_num = 1   
  > pose_num = 1  
  
__step 4:__ save images   
`$ rosrun handover save_video.py`  

# Dataset 2  


## Start to save data  
__step 1:__ initialize the robot  
`$ cd /home/abml/zoe_ws/src/handover/src`   
`./ur_init_dataset_2.py`  
__step 2:__ human hands over the instrument to the robot  
`$ rosrun handover grasp_target_generate.py`  
__step 3:__ robot grasps the instrument  
`./ur_move_dataset_1.py`  
__step 4:__ revise two params in `save_data.py`:  
  > dataset_num = 2  
  > member_num = 1  
  > pose_num = 1  
  
__step 4:__ press `Enter` save data   
`$ rosrun handover save_data.py`  


# Process Images  
`$ cd /home/abml/zoe_ws/src/handover/data`  
revise parameters  
> image_num = 196  
> dataset_num = 1  
> member_num = 1  
> pose_num = 1  
`$ ./process_image.py`  

# Visualize Data  
`$ roslaunch visualize_data launch_visualize_hand.launch`  
`$ rosrun visualize_data visualize_hand.py`



























