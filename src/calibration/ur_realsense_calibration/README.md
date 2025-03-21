## Calibrate franka and realsense
### ref  
https://github.com/IFL-CAMP/easy_handeye/tree/master  
https://www.guyuehome.com/35290  
### usage of the launch files in this folder  
`$ roslaunch ur_realsense_calibration step-1.launch`  

`$ roslaunch ur_realsense_calibration step-2.launch`  

---
`$ rosrun franka_realsense_calibration reset_rob.py`  

1. The first launch file should open an rviz GUI. The second launch file should open 2 rqt GUI.  
1. robot\_effector\_frame is set as "tool0" but "tool0\_controller" is the __tcp__ frame. If the tcp is reset in the script, tool0\_controller 
2. Pay attention to the camera __resolution__ included in the first launch file.  
3. Add the image topic `/aruco_tracker/result` in rviz to check if the aruco is successfully detected.   
4. Follow the blog https://www.guyuehome.com/35290  
> Step 1: Move the robot until the aruco is in the middle of the camera view.  
> Step 2: Click **Check starting pose**.  
> Step 3: Sequentially press **Next Pose**, **Plan**, **Execute**. If the aruco is not successfully detected, don't take this pose as a sample.  
> Step 4: Press **Take Sample**  
> Step 5: Repeat Step 3 and Step 4 until all 17 poses are generated. Finally, 17 poses might not all are effective samples. But, 10 poses mgiht be enough to compute. You can also adjust the aruco or the initial pose of the robot (in Step 1) and redo take samples.  
> Step 6: Press **Compute**  
> Step 7: Publish the result via a tf static\_transform\_publisher  

### result  
The result has been recorded in `tf_rob_cam.launch`  


