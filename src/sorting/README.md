`$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM1 _baud:=57600`  
`$ rostopic pub /control_pump std_msgs/Float64 "data: 3.8"`  
`$ rostopic pub /control_power std_msgs/Int32 "data: 1"`  
`$ rostopic pub /control_magnet std_msgs/Int32 "data: 1"`  


`$ roslaunch grasping launch_cam.launch`  
`$ sudo iptables -I INPUT -p udp -j ACCEPT`  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ rosrun franka_basic_motion grasping_init.py tempt`  
`$ roslaunch grasping launch_tfs.launch`  
`$ roslaunch grasping launch_tf_subs.launch`  
`$ rosrun sorting get_grasping_point.py`  
`$ rosrun sorting generate_pick_target.py`  
`$ rosrun sorting get_place_point.py` 
`$ rosrun sorting generate_place_target.py`  
`$ rosrun sorting rob_move.py` 
`$ rosrun sorting save_images.py` 

`$ rosrun grasping generate_target.py`  
