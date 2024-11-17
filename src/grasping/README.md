## Usage  
### V4  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
__initial pose to grasp:__  
joints: [90, -50, 0, -150, 0, 100, 45] degree  
ee pose: p = [0.001, 0.288, 0.399], q = [0.710, 0.705, -0.004, 0.007]   

__initial pose to handover:__  
joints: [0, -50, 0, -150, 0, 100, 45] degree  
ee pose: p = [0.289, 0.000, 0.400], q = [1.000, -0.002, -0.006, 0.002]   

`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ rosrun franka_basic_motion grasping_init.py grasping`  
`$ roslaunch grasping launch_tfs.launch`  
`$ roslaunch grasping launch_tf_subs.launch`  
`$ rosrun llm_rob_fun generate_target.py`  
`$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600`  
`$ rostopic pub /control_magnet std_msgs/Int32 "data: 1"`  
`$ rostopic pub /control_pump std_msgs/Float64 "data: 3.8"`  
`$ rosrun llm_rob_fun rob_move.py`  

### V3  
(to be improved)  
revise self.grasp\_pix and self.handle\_pix in detect_table.py   
`$ roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda`  
`$ roslaunch grasping launch_tfs.launch`  
`$ roslaunch grasping launch_tf_subs.launch`  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ rosrun grasping detect_table.py`  
`$ rosrun grasping generate_target.py`  
`$ rosrun grasping move_to_ee3_goal.py (test_grasp.py)`  
`$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600`  
`$ rosrun grasping move_method_2.py`  
step 1: reset robot pose    
`$ rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.515, 0.707, -0.707, 0.0, 0.0]" `  
step 2: get the target p=\[x\_d, y\_d, z\_d\] and q\_d  
`$ rostopic echo /ee_target_in_base`  
step 3: get the current p=\[x, y, z\]  
`$ rostopic echo /cartesian_pose`  
step 4: reach the target orientation  
`$ rostopic pub /set_goal_ee3 std_msgs/Bool "data: True" `  
step 5: move to the above of the instrument  
`$ rostopic pub /position_goal std_msgs/Float64MultiArray "data: [x_d, y_d, z]" `  
step 6: move to the instrument, progressively approaching the target z_d   
`$ rostopic pub /position_goal std_msgs/Float64MultiArray "data: [x_d, y_d, 0.0]" `  
`$ rostopic pub /position_goal std_msgs/Float64MultiArray "data: [x_d, y_d, z_d]" `  
step 7: activate the electral magnet  
`$ rostopic pub /control_magnet std_msgs/Int32 "data: 1"`  
step 8: activate the bellow  
`$ rostopic pub /control_pump std_msgs/Float64 "data: 3.8"`  
step 9: close the gripper in rviz via moveit  
step 10: raise the instrument  
`$ rostopic pub /position_goal std_msgs/Float64MultiArray "data: [x_d, y_d, 0.2]" `  

### V2  
`$ roslaunch franka_interface interface.launch`  
`$ roslaunch grasping launch_tfs.launch`  
`$ roslaunch grasping launch_tf_subs.launch`  
__Move franka given a camera's pose__  
`$ rosrun grasping move_to_camera_goal.py`  
To reset:  
`$ rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.40, 0.0, 0.50, 0.707, -0.707, 0.0, 0.0]"`  
__Move franka given an assistant finger's pose__  
`$ rosrun grasping move_to_ee3_goal.py`  

### V1  
`$ roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda`  
`$ roslaunch grasping launch_tfs.launch`  
`$ rosrun grasping move_franka.py`  
`$ rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.40, 0.0, 0.50, 0.707, -0.707, 0.0, 0.0]"`  



