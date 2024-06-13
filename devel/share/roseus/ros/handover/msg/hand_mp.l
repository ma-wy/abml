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
  :slots (_header _handedness _wrist _thumb_tip _index_tip _middle_tip _ring_tip _pinky_tip _index_mcp _middle_mcp _ring_mcp _pinky_mcp ))

(defmethod handover::hand_mp
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:handedness __handedness) (instance std_msgs::String :init))
    ((:wrist __wrist) (instance geometry_msgs::Point :init))
    ((:thumb_tip __thumb_tip) (instance geometry_msgs::Point :init))
    ((:index_tip __index_tip) (instance geometry_msgs::Point :init))
    ((:middle_tip __middle_tip) (instance geometry_msgs::Point :init))
    ((:ring_tip __ring_tip) (instance geometry_msgs::Point :init))
    ((:pinky_tip __pinky_tip) (instance geometry_msgs::Point :init))
    ((:index_mcp __index_mcp) (instance geometry_msgs::Point :init))
    ((:middle_mcp __middle_mcp) (instance geometry_msgs::Point :init))
    ((:ring_mcp __ring_mcp) (instance geometry_msgs::Point :init))
    ((:pinky_mcp __pinky_mcp) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _handedness __handedness)
   (setq _wrist __wrist)
   (setq _thumb_tip __thumb_tip)
   (setq _index_tip __index_tip)
   (setq _middle_tip __middle_tip)
   (setq _ring_tip __ring_tip)
   (setq _pinky_tip __pinky_tip)
   (setq _index_mcp __index_mcp)
   (setq _middle_mcp __middle_mcp)
   (setq _ring_mcp __ring_mcp)
   (setq _pinky_mcp __pinky_mcp)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:handedness
   (&rest __handedness)
   (if (keywordp (car __handedness))
       (send* _handedness __handedness)
     (progn
       (if __handedness (setq _handedness (car __handedness)))
       _handedness)))
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
  (:index_mcp
   (&rest __index_mcp)
   (if (keywordp (car __index_mcp))
       (send* _index_mcp __index_mcp)
     (progn
       (if __index_mcp (setq _index_mcp (car __index_mcp)))
       _index_mcp)))
  (:middle_mcp
   (&rest __middle_mcp)
   (if (keywordp (car __middle_mcp))
       (send* _middle_mcp __middle_mcp)
     (progn
       (if __middle_mcp (setq _middle_mcp (car __middle_mcp)))
       _middle_mcp)))
  (:ring_mcp
   (&rest __ring_mcp)
   (if (keywordp (car __ring_mcp))
       (send* _ring_mcp __ring_mcp)
     (progn
       (if __ring_mcp (setq _ring_mcp (car __ring_mcp)))
       _ring_mcp)))
  (:pinky_mcp
   (&rest __pinky_mcp)
   (if (keywordp (car __pinky_mcp))
       (send* _pinky_mcp __pinky_mcp)
     (progn
       (if __pinky_mcp (setq _pinky_mcp (car __pinky_mcp)))
       _pinky_mcp)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/String _handedness
    (send _handedness :serialization-length)
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
    ;; geometry_msgs/Point _index_mcp
    (send _index_mcp :serialization-length)
    ;; geometry_msgs/Point _middle_mcp
    (send _middle_mcp :serialization-length)
    ;; geometry_msgs/Point _ring_mcp
    (send _ring_mcp :serialization-length)
    ;; geometry_msgs/Point _pinky_mcp
    (send _pinky_mcp :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/String _handedness
       (send _handedness :serialize s)
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
     ;; geometry_msgs/Point _index_mcp
       (send _index_mcp :serialize s)
     ;; geometry_msgs/Point _middle_mcp
       (send _middle_mcp :serialize s)
     ;; geometry_msgs/Point _ring_mcp
       (send _ring_mcp :serialize s)
     ;; geometry_msgs/Point _pinky_mcp
       (send _pinky_mcp :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; std_msgs/String _handedness
     (send _handedness :deserialize buf ptr-) (incf ptr- (send _handedness :serialization-length))
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
   ;; geometry_msgs/Point _index_mcp
     (send _index_mcp :deserialize buf ptr-) (incf ptr- (send _index_mcp :serialization-length))
   ;; geometry_msgs/Point _middle_mcp
     (send _middle_mcp :deserialize buf ptr-) (incf ptr- (send _middle_mcp :serialization-length))
   ;; geometry_msgs/Point _ring_mcp
     (send _ring_mcp :deserialize buf ptr-) (incf ptr- (send _ring_mcp :serialization-length))
   ;; geometry_msgs/Point _pinky_mcp
     (send _pinky_mcp :deserialize buf ptr-) (incf ptr- (send _pinky_mcp :serialization-length))
   ;;
   self)
  )

(setf (get handover::hand_mp :md5sum-) "c180baaf221b3c9ea1b674a724ca2e79")
(setf (get handover::hand_mp :datatype-) "handover/hand_mp")
(setf (get handover::hand_mp :definition-)
      "Header header
std_msgs/String handedness
geometry_msgs/Point wrist
geometry_msgs/Point thumb_tip
geometry_msgs/Point index_tip
geometry_msgs/Point middle_tip
geometry_msgs/Point ring_tip
geometry_msgs/Point pinky_tip
geometry_msgs/Point index_mcp
geometry_msgs/Point middle_mcp
geometry_msgs/Point ring_mcp
geometry_msgs/Point pinky_mcp

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
MSG: std_msgs/String
string data

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :handover/hand_mp "c180baaf221b3c9ea1b674a724ca2e79")


