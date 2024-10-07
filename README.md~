# useful command:  
## make packages isolatedly  
`$ catkin_make_isolated`  
* some packages (e.g. ur_client_library) is not a catkin pacakge  
## create a new package  
`$ catkin_create_pkg pkg_name rospy roscpp std_msgs`  
## compile specific package  
`$ catkin_make -DCATKIN_WHITELIST_PACKAGES="package_name1; package_name2"`   

## Franka   
`https://192.168.1.110/desk/
joints unlock  
activate FCI    

## git  
`$ git add .`  
`$ git commit -m "data" `  
`$ git push origin main`  

## check rs camera intrinsics  
__Method 1__  
__step 1:__ cut down all launchs to the camera  
__step 2:__ run the command  
`$ rs-sensor-control`  
__step 3:__ choose the device and the stream. Simply identify the image size. Their intrinsics are the same.  
__Method 2__  
__step 1:__ launch the camera 
`$ roslaunch current_pkg launch_cam.launch`  
__step 2:__ echo the image_info topic and get the result from K or P  
`$ rostopic echo /camera/color/camera_info`  
__Note:__  
image size: 720x1280  
`$ rostopic echo /camera/aligned_depth_to_color/camera_info`  
returns the same result, but 
`$ rostopic echo /camera/depth/camera_info`  
resutns a different result
