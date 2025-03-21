; Auto-generated. Do not edit!


(cl:in-package handover-msg)


;//! \htmlinclude hand_mp.msg.html

(cl:defclass <hand_mp> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (handedness
    :reader handedness
    :initarg :handedness
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (wrist
    :reader wrist
    :initarg :wrist
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (thumb_tip
    :reader thumb_tip
    :initarg :thumb_tip
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (index_tip
    :reader index_tip
    :initarg :index_tip
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (middle_tip
    :reader middle_tip
    :initarg :middle_tip
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (ring_tip
    :reader ring_tip
    :initarg :ring_tip
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (pinky_tip
    :reader pinky_tip
    :initarg :pinky_tip
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (index_mcp
    :reader index_mcp
    :initarg :index_mcp
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (middle_mcp
    :reader middle_mcp
    :initarg :middle_mcp
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (ring_mcp
    :reader ring_mcp
    :initarg :ring_mcp
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (pinky_mcp
    :reader pinky_mcp
    :initarg :pinky_mcp
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass hand_mp (<hand_mp>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <hand_mp>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'hand_mp)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name handover-msg:<hand_mp> is deprecated: use handover-msg:hand_mp instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:header-val is deprecated.  Use handover-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'handedness-val :lambda-list '(m))
(cl:defmethod handedness-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:handedness-val is deprecated.  Use handover-msg:handedness instead.")
  (handedness m))

(cl:ensure-generic-function 'wrist-val :lambda-list '(m))
(cl:defmethod wrist-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:wrist-val is deprecated.  Use handover-msg:wrist instead.")
  (wrist m))

(cl:ensure-generic-function 'thumb_tip-val :lambda-list '(m))
(cl:defmethod thumb_tip-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:thumb_tip-val is deprecated.  Use handover-msg:thumb_tip instead.")
  (thumb_tip m))

(cl:ensure-generic-function 'index_tip-val :lambda-list '(m))
(cl:defmethod index_tip-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:index_tip-val is deprecated.  Use handover-msg:index_tip instead.")
  (index_tip m))

(cl:ensure-generic-function 'middle_tip-val :lambda-list '(m))
(cl:defmethod middle_tip-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:middle_tip-val is deprecated.  Use handover-msg:middle_tip instead.")
  (middle_tip m))

(cl:ensure-generic-function 'ring_tip-val :lambda-list '(m))
(cl:defmethod ring_tip-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:ring_tip-val is deprecated.  Use handover-msg:ring_tip instead.")
  (ring_tip m))

(cl:ensure-generic-function 'pinky_tip-val :lambda-list '(m))
(cl:defmethod pinky_tip-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:pinky_tip-val is deprecated.  Use handover-msg:pinky_tip instead.")
  (pinky_tip m))

(cl:ensure-generic-function 'index_mcp-val :lambda-list '(m))
(cl:defmethod index_mcp-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:index_mcp-val is deprecated.  Use handover-msg:index_mcp instead.")
  (index_mcp m))

(cl:ensure-generic-function 'middle_mcp-val :lambda-list '(m))
(cl:defmethod middle_mcp-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:middle_mcp-val is deprecated.  Use handover-msg:middle_mcp instead.")
  (middle_mcp m))

(cl:ensure-generic-function 'ring_mcp-val :lambda-list '(m))
(cl:defmethod ring_mcp-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:ring_mcp-val is deprecated.  Use handover-msg:ring_mcp instead.")
  (ring_mcp m))

(cl:ensure-generic-function 'pinky_mcp-val :lambda-list '(m))
(cl:defmethod pinky_mcp-val ((m <hand_mp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader handover-msg:pinky_mcp-val is deprecated.  Use handover-msg:pinky_mcp instead.")
  (pinky_mcp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <hand_mp>) ostream)
  "Serializes a message object of type '<hand_mp>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'handedness) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'wrist) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'thumb_tip) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'index_tip) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'middle_tip) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ring_tip) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pinky_tip) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'index_mcp) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'middle_mcp) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ring_mcp) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pinky_mcp) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <hand_mp>) istream)
  "Deserializes a message object of type '<hand_mp>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'handedness) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'wrist) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'thumb_tip) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'index_tip) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'middle_tip) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ring_tip) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pinky_tip) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'index_mcp) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'middle_mcp) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ring_mcp) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pinky_mcp) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<hand_mp>)))
  "Returns string type for a message object of type '<hand_mp>"
  "handover/hand_mp")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'hand_mp)))
  "Returns string type for a message object of type 'hand_mp"
  "handover/hand_mp")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<hand_mp>)))
  "Returns md5sum for a message object of type '<hand_mp>"
  "c180baaf221b3c9ea1b674a724ca2e79")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'hand_mp)))
  "Returns md5sum for a message object of type 'hand_mp"
  "c180baaf221b3c9ea1b674a724ca2e79")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<hand_mp>)))
  "Returns full string definition for message of type '<hand_mp>"
  (cl:format cl:nil "Header header~%std_msgs/String handedness~%geometry_msgs/Point wrist~%geometry_msgs/Point thumb_tip~%geometry_msgs/Point index_tip~%geometry_msgs/Point middle_tip~%geometry_msgs/Point ring_tip~%geometry_msgs/Point pinky_tip~%geometry_msgs/Point index_mcp~%geometry_msgs/Point middle_mcp~%geometry_msgs/Point ring_mcp~%geometry_msgs/Point pinky_mcp~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'hand_mp)))
  "Returns full string definition for message of type 'hand_mp"
  (cl:format cl:nil "Header header~%std_msgs/String handedness~%geometry_msgs/Point wrist~%geometry_msgs/Point thumb_tip~%geometry_msgs/Point index_tip~%geometry_msgs/Point middle_tip~%geometry_msgs/Point ring_tip~%geometry_msgs/Point pinky_tip~%geometry_msgs/Point index_mcp~%geometry_msgs/Point middle_mcp~%geometry_msgs/Point ring_mcp~%geometry_msgs/Point pinky_mcp~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <hand_mp>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'handedness))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'wrist))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'thumb_tip))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'index_tip))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'middle_tip))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ring_tip))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pinky_tip))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'index_mcp))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'middle_mcp))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ring_mcp))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pinky_mcp))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <hand_mp>))
  "Converts a ROS message object to a list"
  (cl:list 'hand_mp
    (cl:cons ':header (header msg))
    (cl:cons ':handedness (handedness msg))
    (cl:cons ':wrist (wrist msg))
    (cl:cons ':thumb_tip (thumb_tip msg))
    (cl:cons ':index_tip (index_tip msg))
    (cl:cons ':middle_tip (middle_tip msg))
    (cl:cons ':ring_tip (ring_tip msg))
    (cl:cons ':pinky_tip (pinky_tip msg))
    (cl:cons ':index_mcp (index_mcp msg))
    (cl:cons ':middle_mcp (middle_mcp msg))
    (cl:cons ':ring_mcp (ring_mcp msg))
    (cl:cons ':pinky_mcp (pinky_mcp msg))
))
