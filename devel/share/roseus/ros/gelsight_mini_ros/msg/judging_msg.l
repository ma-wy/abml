;; Auto-generated. Do not edit!


(when (boundp 'gelsight_mini_ros::judging_msg)
  (if (not (find-package "GELSIGHT_MINI_ROS"))
    (make-package "GELSIGHT_MINI_ROS"))
  (shadow 'judging_msg (find-package "GELSIGHT_MINI_ROS")))
(unless (find-package "GELSIGHT_MINI_ROS::JUDGING_MSG")
  (make-package "GELSIGHT_MINI_ROS::JUDGING_MSG"))

(in-package "ROS")
;;//! \htmlinclude judging_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass gelsight_mini_ros::judging_msg
  :super ros::object
  :slots (_header _is_contact _is_overforced ))

(defmethod gelsight_mini_ros::judging_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:is_contact __is_contact) nil)
    ((:is_overforced __is_overforced) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _is_contact __is_contact)
   (setq _is_overforced __is_overforced)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:is_contact
   (&optional (__is_contact :null))
   (if (not (eq __is_contact :null)) (setq _is_contact __is_contact)) _is_contact)
  (:is_overforced
   (&optional (__is_overforced :null))
   (if (not (eq __is_overforced :null)) (setq _is_overforced __is_overforced)) _is_overforced)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _is_contact
    1
    ;; bool _is_overforced
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _is_contact
       (if _is_contact (write-byte -1 s) (write-byte 0 s))
     ;; bool _is_overforced
       (if _is_overforced (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _is_contact
     (setq _is_contact (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _is_overforced
     (setq _is_overforced (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get gelsight_mini_ros::judging_msg :md5sum-) "10ed4c6e740e87d5c0e7f8d06f6ac17c")
(setf (get gelsight_mini_ros::judging_msg :datatype-) "gelsight_mini_ros/judging_msg")
(setf (get gelsight_mini_ros::judging_msg :definition-)
      "# timestamp
Header header

# contact and over-forced judgement
bool is_contact
bool is_overforced

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



(provide :gelsight_mini_ros/judging_msg "10ed4c6e740e87d5c0e7f8d06f6ac17c")


