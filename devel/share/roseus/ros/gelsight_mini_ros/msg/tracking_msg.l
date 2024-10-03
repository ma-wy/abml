;; Auto-generated. Do not edit!


(when (boundp 'gelsight_mini_ros::tracking_msg)
  (if (not (find-package "GELSIGHT_MINI_ROS"))
    (make-package "GELSIGHT_MINI_ROS"))
  (shadow 'tracking_msg (find-package "GELSIGHT_MINI_ROS")))
(unless (find-package "GELSIGHT_MINI_ROS::TRACKING_MSG")
  (make-package "GELSIGHT_MINI_ROS::TRACKING_MSG"))

(in-package "ROS")
;;//! \htmlinclude tracking_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass gelsight_mini_ros::tracking_msg
  :super ros::object
  :slots (_header _marker_x _marker_y _marker_displacement_x _marker_displacement_y ))

(defmethod gelsight_mini_ros::tracking_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:marker_x __marker_x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:marker_y __marker_y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:marker_displacement_x __marker_displacement_x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:marker_displacement_y __marker_displacement_y) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _marker_x __marker_x)
   (setq _marker_y __marker_y)
   (setq _marker_displacement_x __marker_displacement_x)
   (setq _marker_displacement_y __marker_displacement_y)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:marker_x
   (&optional __marker_x)
   (if __marker_x (setq _marker_x __marker_x)) _marker_x)
  (:marker_y
   (&optional __marker_y)
   (if __marker_y (setq _marker_y __marker_y)) _marker_y)
  (:marker_displacement_x
   (&optional __marker_displacement_x)
   (if __marker_displacement_x (setq _marker_displacement_x __marker_displacement_x)) _marker_displacement_x)
  (:marker_displacement_y
   (&optional __marker_displacement_y)
   (if __marker_displacement_y (setq _marker_displacement_y __marker_displacement_y)) _marker_displacement_y)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32[] _marker_x
    (* 4    (length _marker_x)) 4
    ;; float32[] _marker_y
    (* 4    (length _marker_y)) 4
    ;; float32[] _marker_displacement_x
    (* 4    (length _marker_displacement_x)) 4
    ;; float32[] _marker_displacement_y
    (* 4    (length _marker_displacement_y)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32[] _marker_x
     (write-long (length _marker_x) s)
     (dotimes (i (length _marker_x))
       (sys::poke (elt _marker_x i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _marker_y
     (write-long (length _marker_y) s)
     (dotimes (i (length _marker_y))
       (sys::poke (elt _marker_y i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _marker_displacement_x
     (write-long (length _marker_displacement_x) s)
     (dotimes (i (length _marker_displacement_x))
       (sys::poke (elt _marker_displacement_x i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _marker_displacement_y
     (write-long (length _marker_displacement_y) s)
     (dotimes (i (length _marker_displacement_y))
       (sys::poke (elt _marker_displacement_y i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32[] _marker_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _marker_x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _marker_x i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _marker_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _marker_y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _marker_y i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _marker_displacement_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _marker_displacement_x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _marker_displacement_x i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _marker_displacement_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _marker_displacement_y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _marker_displacement_y i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get gelsight_mini_ros::tracking_msg :md5sum-) "8b99f4a1ff1377c066f07003f01617ae")
(setf (get gelsight_mini_ros::tracking_msg :datatype-) "gelsight_mini_ros/tracking_msg")
(setf (get gelsight_mini_ros::tracking_msg :definition-)
      "# timestamp
Header header

# position and displacement of markers
float32[] marker_x
float32[] marker_y
float32[] marker_displacement_x
float32[] marker_displacement_y

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :gelsight_mini_ros/tracking_msg "8b99f4a1ff1377c066f07003f01617ae")


