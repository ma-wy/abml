; Auto-generated. Do not edit!


(cl:in-package onrobot_rg_control-msg)


;//! \htmlinclude OnRobotRGInput.msg.html

(cl:defclass <OnRobotRGInput> (roslisp-msg-protocol:ros-message)
  ((gFOF
    :reader gFOF
    :initarg :gFOF
    :type cl:fixnum
    :initform 0)
   (gGWD
    :reader gGWD
    :initarg :gGWD
    :type cl:fixnum
    :initform 0)
   (gSTA
    :reader gSTA
    :initarg :gSTA
    :type cl:fixnum
    :initform 0)
   (gWDF
    :reader gWDF
    :initarg :gWDF
    :type cl:fixnum
    :initform 0))
)

(cl:defclass OnRobotRGInput (<OnRobotRGInput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OnRobotRGInput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OnRobotRGInput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name onrobot_rg_control-msg:<OnRobotRGInput> is deprecated: use onrobot_rg_control-msg:OnRobotRGInput instead.")))

(cl:ensure-generic-function 'gFOF-val :lambda-list '(m))
(cl:defmethod gFOF-val ((m <OnRobotRGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:gFOF-val is deprecated.  Use onrobot_rg_control-msg:gFOF instead.")
  (gFOF m))

(cl:ensure-generic-function 'gGWD-val :lambda-list '(m))
(cl:defmethod gGWD-val ((m <OnRobotRGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:gGWD-val is deprecated.  Use onrobot_rg_control-msg:gGWD instead.")
  (gGWD m))

(cl:ensure-generic-function 'gSTA-val :lambda-list '(m))
(cl:defmethod gSTA-val ((m <OnRobotRGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:gSTA-val is deprecated.  Use onrobot_rg_control-msg:gSTA instead.")
  (gSTA m))

(cl:ensure-generic-function 'gWDF-val :lambda-list '(m))
(cl:defmethod gWDF-val ((m <OnRobotRGInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:gWDF-val is deprecated.  Use onrobot_rg_control-msg:gWDF instead.")
  (gWDF m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OnRobotRGInput>) ostream)
  "Serializes a message object of type '<OnRobotRGInput>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFOF)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gFOF)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGWD)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gGWD)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gWDF)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gWDF)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OnRobotRGInput>) istream)
  "Deserializes a message object of type '<OnRobotRGInput>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFOF)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gFOF)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGWD)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gGWD)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gWDF)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gWDF)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OnRobotRGInput>)))
  "Returns string type for a message object of type '<OnRobotRGInput>"
  "onrobot_rg_control/OnRobotRGInput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OnRobotRGInput)))
  "Returns string type for a message object of type 'OnRobotRGInput"
  "onrobot_rg_control/OnRobotRGInput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OnRobotRGInput>)))
  "Returns md5sum for a message object of type '<OnRobotRGInput>"
  "94435113a24b6809371af29f68843bdb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OnRobotRGInput)))
  "Returns md5sum for a message object of type 'OnRobotRGInput"
  "94435113a24b6809371af29f68843bdb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OnRobotRGInput>)))
  "Returns full string definition for message of type '<OnRobotRGInput>"
  (cl:format cl:nil "# gFOF : Current fingertip offset in 1/10 millimeters. The value is a signed two's complement number.~%~%uint16 gFOF~%~%# gGWD : Current width between the gripper fingers in 1/10 millimeters.~%#        The width is provided without any fingertip offset, as it is measured between the insides of the aluminum fingers.~%~%uint16 gGWD~%~%# gSTA : Current device status, which indicates the status of the gripper and its motion.~%# Bit       - Name              - Description~%# 0 (LSB)   - Busy              - High (1) when a motion is ongoing, low (0) when not. The gripper will only accept new commands when this flag is low.~%# 1         - Grip detected     - High (1) when an internal- or external grip is detected.~%# 2         - S1 pushed         - High (1) when safety switch 1 is pushed.~%# 3         - S1 trigged        - High (1) when safety circuit 1 is activated. The gripper will not move while this flag is high.~%# 4         - S2 pushed         - High (1) when safety switch 2 is pushed.~%# 5         - S2 trigged        - High (1) when safety circuit 2 is activated. The gripper will not move while this flag is high.~%# 6         - Safety error      - High (1) when on power on any of the safety switch is pushed.~%# 7 - 15    - Reserved          - Not used.~%~%uint8 gSTA~%~%# gWDF : Current width between the gripper fingers in 1/10 millimeters.~%#        The set fingertip offset is considered.~%~%uint16 gWDF~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OnRobotRGInput)))
  "Returns full string definition for message of type 'OnRobotRGInput"
  (cl:format cl:nil "# gFOF : Current fingertip offset in 1/10 millimeters. The value is a signed two's complement number.~%~%uint16 gFOF~%~%# gGWD : Current width between the gripper fingers in 1/10 millimeters.~%#        The width is provided without any fingertip offset, as it is measured between the insides of the aluminum fingers.~%~%uint16 gGWD~%~%# gSTA : Current device status, which indicates the status of the gripper and its motion.~%# Bit       - Name              - Description~%# 0 (LSB)   - Busy              - High (1) when a motion is ongoing, low (0) when not. The gripper will only accept new commands when this flag is low.~%# 1         - Grip detected     - High (1) when an internal- or external grip is detected.~%# 2         - S1 pushed         - High (1) when safety switch 1 is pushed.~%# 3         - S1 trigged        - High (1) when safety circuit 1 is activated. The gripper will not move while this flag is high.~%# 4         - S2 pushed         - High (1) when safety switch 2 is pushed.~%# 5         - S2 trigged        - High (1) when safety circuit 2 is activated. The gripper will not move while this flag is high.~%# 6         - Safety error      - High (1) when on power on any of the safety switch is pushed.~%# 7 - 15    - Reserved          - Not used.~%~%uint8 gSTA~%~%# gWDF : Current width between the gripper fingers in 1/10 millimeters.~%#        The set fingertip offset is considered.~%~%uint16 gWDF~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OnRobotRGInput>))
  (cl:+ 0
     2
     2
     1
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OnRobotRGInput>))
  "Converts a ROS message object to a list"
  (cl:list 'OnRobotRGInput
    (cl:cons ':gFOF (gFOF msg))
    (cl:cons ':gGWD (gGWD msg))
    (cl:cons ':gSTA (gSTA msg))
    (cl:cons ':gWDF (gWDF msg))
))
