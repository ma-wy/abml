;; Auto-generated. Do not edit!


(when (boundp 'handover::hand_mp)
  (if (not (find-package "HANDOVER"))
    (make-package "HANDOVER"))
  (shadow 'hand_mp (find-package "HANDOVER")))
(unless (find-package "HANDOVER::HAND_MP")
  (make-package "HANDOVER::HAND_MP"))

(in-package "ROS")
;;//! \htmlinclude hand_mp.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass handover::hand_mp
  :super ros::object
  :slots (_header _wrist _thumb_tip _index_tip _middle_tip _ring_tip _pinky_tip ))

(defmethod handover::hand_mp
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:wrist __wrist) (instance geometry_msgs::Point :init))
    ((:thumb_tip __thumb_tip) (instance geometry_msgs::Point :init))
    ((:index_tip __index_tip) (instance geometry_msgs::Point :init))
    ((:middle_tip __middle_tip) (instance geometry_msgs::Point :init))
    ((:ring_tip __ring_tip) (instance geometry_msgs::Point :init))
    ((:pinky_tip __pinky_tip) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _wrist __wrist)
   (setq _thumb_tip __thumb_tip)
   (setq _index_tip __index_tip)
   (setq _middle_tip __middle_tip)
   (setq _ring_tip __ring_tip)
   (setq _pinky_tip __pinky_tip)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:wrist
   (&rest __wrist)
   (if (keywordp (car __wrist))
       (send* _wrist __wrist)
     (progn
       (if __wrist (setq _wrist (car __wrist)))
       _wrist)))
  (:thumb_tip
   (&rest __thumb_tip)
   (if (keywordp (car __thumb_tip))
       (send* _thumb_tip __thumb_tip)
     (progn
       (if __thumb_tip (setq _thumb_tip (car __thumb_tip)))
       _thumb_tip)))
  (:index_tip
   (&rest __index_tip)
   (if (keywordp (car __index_tip))
       (send* _index_tip __index_tip)
     (progn
       (if __index_tip (setq _index_tip (car __index_tip)))
       _index_tip)))
  (:middle_tip
   (&rest __middle_tip)
   (if (keywordp (car __middle_tip))
       (send* _middle_tip __middle_tip)
     (progn
       (if __middle_tip (setq _middle_tip (car __middle_tip)))
       _middle_tip)))
  (:ring_tip
   (&rest __ring_tip)
   (if (keywordp (car __ring_tip))
       (send* _ring_tip __ring_tip)
     (progn
       (if __ring_tip (setq _ring_tip (car __ring_tip)))
       _ring_tip)))
  (:pinky_tip
   (&rest __pinky_tip)
   (if (keywordp (car __pinky_tip))
       (send* _pinky_tip __pinky_tip)
     (progn
       (if __pinky_tip (setq _pinky_tip (car __pinky_tip)))
       _pinky_tip)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Point _wrist
    (send _wrist :serialization-length)
    ;; geometry_msgs/Point _thumb_tip
    (send _thumb_tip :serialization-length)
    ;; geometry_msgs/Point _index_tip
    (send _index_tip :serialization-length)
    ;; geometry_msgs/Point _middle_tip
    (send _middle_tip :serialization-length)
    ;; geometry_msgs/Point _ring_tip
    (send _ring_tip :serialization-length)
    ;; geometry_msgs/Point _pinky_tip
    (send _pinky_tip :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Point _wrist
       (send _wrist :serialize s)
     ;; geometry_msgs/Point _thumb_tip
       (send _thumb_tip :serialize s)
     ;; geometry_msgs/Point _index_tip
       (send _index_tip :serialize s)
     ;; geometry_msgs/Point _middle_tip
       (send _middle_tip :serialize s)
     ;; geometry_msgs/Point _ring_tip
       (send _ring_tip :serialize s)
     ;; geometry_msgs/Point _pinky_tip
       (send _pinky_tip :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Point _wrist
     (send _wrist :deserialize buf ptr-) (incf ptr- (send _wrist :serialization-length))
   ;; geometry_msgs/Point _thumb_tip
     (send _thumb_tip :deserialize buf ptr-) (incf ptr- (send _thumb_tip :serialization-length))
   ;; geometry_msgs/Point _index_tip
     (send _index_tip :deserialize buf ptr-) (incf ptr- (send _index_tip :serialization-length))
   ;; geometry_msgs/Point _middle_tip
     (send _middle_tip :deserialize buf ptr-) (incf ptr- (send _middle_tip :serialization-length))
   ;; geometry_msgs/Point _ring_tip
     (send _ring_tip :deserialize buf ptr-) (incf ptr- (send _ring_tip :serialization-length))
   ;; geometry_msgs/Point _pinky_tip
     (send _pinky_tip :deserialize buf ptr-) (incf ptr- (send _pinky_tip :serialization-length))
   ;;
   self)
  )

(setf (get handover::hand_mp :md5sum-) "bee6e7ec827cd5a686ce9e3c8b2a5b20")
(setf (get handover::hand_mp :datatype-) "handover/hand_mp")
(setf (get handover::hand_mp :definition-)
      "Header header
geometry_msgs/Point wrist
geometry_msgs/Point thumb_tip
geometry_msgs/Point index_tip
geometry_msgs/Point middle_tip
geometry_msgs/Point ring_tip
geometry_msgs/Point pinky_tip

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

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :handover/hand_mp "bee6e7ec827cd5a686ce9e3c8b2a5b20")


