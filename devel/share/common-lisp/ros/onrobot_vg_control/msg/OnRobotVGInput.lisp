; Auto-generated. Do not edit!


(cl:in-package onrobot_vg_control-msg)


;//! \htmlinclude OnRobotVGInput.msg.html

(cl:defclass <OnRobotVGInput> (roslisp-msg-protocol:ros-message)
  ((gVCA
    :reader gVCA
    :initarg :gVCA
    :type cl:fixnum
    :initform 0)
   (gVCB
    :reader gVCB
    :initarg :gVCB
    :type cl:fixnum
    :initform 0))
)

(cl:defclass OnRobotVGInput (<OnRobotVGInput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OnRobotVGInput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OnRobotVGInput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name onrobot_vg_control-msg:<OnRobotVGInput> is deprecated: use onrobot_vg_control-msg:OnRobotVGInput instead.")))

(cl:ensure-generic-function 'gVCA-val :lambda-list '(m))
(cl:defmethod gVCA-val ((m <OnRobotVGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:gVCA-val is deprecated.  Use onrobot_vg_control-msg:gVCA instead.")
  (gVCA m))

(cl:ensure-generic-function 'gVCB-val :lambda-list '(m))
(cl:defmethod gVCB-val ((m <OnRobotVGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:gVCB-val is deprecated.  Use onrobot_vg_control-msg:gVCB instead.")
  (gVCB m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OnRobotVGInput>) ostream)
  "Serializes a message object of type '<OnRobotVGInput>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gVCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gVCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gVCB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gVCB)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OnRobotVGInput>) istream)
  "Deserializes a message object of type '<OnRobotVGInput>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gVCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gVCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gVCB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gVCB)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OnRobotVGInput>)))
  "Returns string type for a message object of type '<OnRobotVGInput>"
  "onrobot_vg_control/OnRobotVGInput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OnRobotVGInput)))
  "Returns string type for a message object of type 'OnRobotVGInput"
  "onrobot_vg_control/OnRobotVGInput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OnRobotVGInput>)))
  "Returns md5sum for a message object of type '<OnRobotVGInput>"
  "3b28006a7c1a9b8e6a658a70e5ab4a0d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OnRobotVGInput)))
  "Returns md5sum for a message object of type 'OnRobotVGInput"
  "3b28006a7c1a9b8e6a658a70e5ab4a0d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OnRobotVGInput>)))
  "Returns full string definition for message of type '<OnRobotVGInput>"
  (cl:format cl:nil "# gVCA : Current vacuum value on Channel A.~%#        The vacuum is provided in 1/1000 of relative vacuum.~%#        Please note that this differs from the setpoint given in percent,~%#        as extra accuracy is desirable on the actual vacuum.~%~%uint16 gVCA~%~%# gVCB : Same as the one of channel A.~%~%uint16 gVCB~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OnRobotVGInput)))
  "Returns full string definition for message of type 'OnRobotVGInput"
  (cl:format cl:nil "# gVCA : Current vacuum value on Channel A.~%#        The vacuum is provided in 1/1000 of relative vacuum.~%#        Please note that this differs from the setpoint given in percent,~%#        as extra accuracy is desirable on the actual vacuum.~%~%uint16 gVCA~%~%# gVCB : Same as the one of channel A.~%~%uint16 gVCB~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OnRobotVGInput>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OnRobotVGInput>))
  "Converts a ROS message object to a list"
  (cl:list 'OnRobotVGInput
    (cl:cons ':gVCA (gVCA msg))
    (cl:cons ':gVCB (gVCB msg))
))
