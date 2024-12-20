`$ ./showimages.py 1`  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ rosrun franka_basic_motion grasping_init.py grasping`  

`$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600`  
`$ rostopic pub /control_magnet std_msgs/Int32 "data: 1"`  
`$ rostopic pub /control_pump std_msgs/Float64 "data: 3.8"`  
`$ rostopic pub /control_power std_msgs/Int32 "data: 1"`  

`$ rosrun franka_basic_motion gripper_close.py`    
`$ rosrun franka_basic_motion gripper_open.py`

`$ rosrun franka_basic_motion trans_axis.py axis displacement speed`  
