; Auto-generated. Do not edit!


(cl:in-package gelsight_mini_ros-msg)


;//! \htmlinclude judging_msg.msg.html

(cl:defclass <judging_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (is_contact
    :reader is_contact
    :initarg :is_contact
    :type cl:boolean
    :initform cl:nil)
   (is_overforced
    :reader is_overforced
    :initarg :is_overforced
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass judging_msg (<judging_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <judging_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'judging_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gelsight_mini_ros-msg:<judging_msg> is deprecated: use gelsight_mini_ros-msg:judging_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <judging_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:header-val is deprecated.  Use gelsight_mini_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'is_contact-val :lambda-list '(m))
(cl:defmethod is_contact-val ((m <judging_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:is_contact-val is deprecated.  Use gelsight_mini_ros-msg:is_contact instead.")
  (is_contact m))

(cl:ensure-generic-function 'is_overforced-val :lambda-list '(m))
(cl:defmethod is_overforced-val ((m <judging_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:is_overforced-val is deprecated.  Use gelsight_mini_ros-msg:is_overforced instead.")
  (is_overforced m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <judging_msg>) ostream)
  "Serializes a message object of type '<judging_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_contact) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_overforced) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <judging_msg>) istream)
  "Deserializes a message object of type '<judging_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:slot-value msg 'is_contact) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'is_overforced) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<judging_msg>)))
  "Returns string type for a message object of type '<judging_msg>"
  "gelsight_mini_ros/judging_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'judging_msg)))
  "Returns string type for a message object of type 'judging_msg"
  "gelsight_mini_ros/judging_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<judging_msg>)))
  "Returns md5sum for a message object of type '<judging_msg>"
  "10ed4c6e740e87d5c0e7f8d06f6ac17c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'judging_msg)))
  "Returns md5sum for a message object of type 'judging_msg"
  "10ed4c6e740e87d5c0e7f8d06f6ac17c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<judging_msg>)))
  "Returns full string definition for message of type '<judging_msg>"
  (cl:format cl:nil "# timestamp~%Header header~%~%# contact and over-forced judgement~%bool is_contact~%bool is_overforced~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'judging_msg)))
  "Returns full string definition for message of type 'judging_msg"
  (cl:format cl:nil "# timestamp~%Header header~%~%# contact and over-forced judgement~%bool is_contact~%bool is_overforced~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <judging_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <judging_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'judging_msg
    (cl:cons ':header (header msg))
    (cl:cons ':is_contact (is_contact msg))
    (cl:cons ':is_overforced (is_overforced msg))
))
