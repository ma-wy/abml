## Air Pump  
### command:  
__step 1__  
unplug the Arduino to check which name disappeared  
check the port name:  
`ls /dev/`  
__step 2__  
`rosrun rosserial_python serial_node.py /dev/ttyACM0`  
`rosrun rosserial_python serial_node.py /dev/port_name`  
output:  
```  
[INFO] [1711443649.197924]: ROS Serial Python Node
[INFO] [1711443649.202890]: Connecting to /dev/ttyACM0 at 57600 baud
[INFO] [1711443651.313960]: Requesting topics...
[INFO] [1711443651.336107]: Note: subscribe buffer size is 512 bytes
[INFO] [1711443651.337412]: Setup subscriber on value_topic [std_msgs/Int64]
^C[INFO] [1711443732.591054]: Sending tx stop request
[INFO] [1711443732.592487]: shutdown hook activated
```  
__step 3__  
subscriber on value_topic [std_msgs/Int64]:  
give a positive air pressure:  
`rostopic pub /value_topic std_msgs/Int64 "data: 1" `  
stop the air stream (0 pressure):  
`rostopic pub /value_topic std_msgs/Int64 "data: -1" `  
__step 4__
`rostopic echo /value_topic`  

P.S.  
in scrubnurseicravideo.py:  
`pub_gripper = rospy.Publisher('/value_topic', Int64, queue_size=10)`   
`pub_gripper.publish(1)`  


