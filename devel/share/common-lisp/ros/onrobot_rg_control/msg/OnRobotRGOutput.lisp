; Auto-generated. Do not edit!


(cl:in-package onrobot_rg_control-msg)


;//! \htmlinclude OnRobotRGOutput.msg.html

(cl:defclass <OnRobotRGOutput> (roslisp-msg-protocol:ros-message)
  ((rGFR
    :reader rGFR
    :initarg :rGFR
    :type cl:fixnum
    :initform 0)
   (rGWD
    :reader rGWD
    :initarg :rGWD
    :type cl:fixnum
    :initform 0)
   (rCTR
    :reader rCTR
    :initarg :rCTR
    :type cl:fixnum
    :initform 0))
)

(cl:defclass OnRobotRGOutput (<OnRobotRGOutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OnRobotRGOutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OnRobotRGOutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name onrobot_rg_control-msg:<OnRobotRGOutput> is deprecated: use onrobot_rg_control-msg:OnRobotRGOutput instead.")))

(cl:ensure-generic-function 'rGFR-val :lambda-list '(m))
(cl:defmethod rGFR-val ((m <OnRobotRGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:rGFR-val is deprecated.  Use onrobot_rg_control-msg:rGFR instead.")
  (rGFR m))

(cl:ensure-generic-function 'rGWD-val :lambda-list '(m))
(cl:defmethod rGWD-val ((m <OnRobotRGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:rGWD-val is deprecated.  Use onrobot_rg_control-msg:rGWD instead.")
  (rGWD m))

(cl:ensure-generic-function 'rCTR-val :lambda-list '(m))
(cl:defmethod rCTR-val ((m <OnRobotRGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_rg_control-msg:rCTR-val is deprecated.  Use onrobot_rg_control-msg:rCTR instead.")
  (rCTR m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OnRobotRGOutput>) ostream)
  "Serializes a message object of type '<OnRobotRGOutput>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rGFR)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rGFR)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rGWD)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rGWD)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rCTR)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OnRobotRGOutput>) istream)
  "Deserializes a message object of type '<OnRobotRGOutput>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rGFR)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rGFR)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rGWD)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rGWD)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rCTR)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OnRobotRGOutput>)))
  "Returns string type for a message object of type '<OnRobotRGOutput>"
  "onrobot_rg_control/OnRobotRGOutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OnRobotRGOutput)))
  "Returns string type for a message object of type 'OnRobotRGOutput"
  "onrobot_rg_control/OnRobotRGOutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OnRobotRGOutput>)))
  "Returns md5sum for a message object of type '<OnRobotRGOutput>"
  "d99680fed3cb1854614e74f47d8e8f52")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OnRobotRGOutput)))
  "Returns md5sum for a message object of type 'OnRobotRGOutput"
  "d99680fed3cb1854614e74f47d8e8f52")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OnRobotRGOutput>)))
  "Returns full string definition for message of type '<OnRobotRGOutput>"
  (cl:format cl:nil "# rGFR : The target force to be reached when gripping and holding a workpiece.~%#        It must be provided in 1/10th Newtons.~%#        The valid range is 0 to 400 for the RG2 and 0 to 1200 for the RG6.~%~%uint16 rGFR~%~%# rGWD : The target width between the finger to be moved to and maintained.~%#        It must be provided in 1/10th millimeters.~%#        The valid range is 0 to 1100 for the RG2 and 0 to 1600 for the RG6.~%#        Please note that the target width should be provided corrected for any fingertip offset,~%#        as it is measured between the insides of the aluminum fingers.~%~%uint16 rGWD~%~%# rCTR : The control field is used to start and stop gripper motion.~%#        Only one option should be set at a time.~%#        Please note that the gripper will not start a new motion~%#        before the one currently being executed is done (see busy flag in the Status field).~%# 0x0001 - grip~%#          Start the motion, with the preset target force and width.~%#          Width is calculated without the fingertip offset.~%#          Please note that the gripper will ignore this command~%#          if the busy flag is set in the status field.~%# 0x0008 - stop~%#          Stop the current motion.~%# 0x0010 - grip_w_offset~%#          Same as grip, but width is calculated with the set fingertip offset.~%~%uint8 rCTR~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OnRobotRGOutput)))
  "Returns full string definition for message of type 'OnRobotRGOutput"
  (cl:format cl:nil "# rGFR : The target force to be reached when gripping and holding a workpiece.~%#        It must be provided in 1/10th Newtons.~%#        The valid range is 0 to 400 for the RG2 and 0 to 1200 for the RG6.~%~%uint16 rGFR~%~%# rGWD : The target width between the finger to be moved to and maintained.~%#        It must be provided in 1/10th millimeters.~%#        The valid range is 0 to 1100 for the RG2 and 0 to 1600 for the RG6.~%#        Please note that the target width should be provided corrected for any fingertip offset,~%#        as it is measured between the insides of the aluminum fingers.~%~%uint16 rGWD~%~%# rCTR : The control field is used to start and stop gripper motion.~%#        Only one option should be set at a time.~%#        Please note that the gripper will not start a new motion~%#        before the one currently being executed is done (see busy flag in the Status field).~%# 0x0001 - grip~%#          Start the motion, with the preset target force and width.~%#          Width is calculated without the fingertip offset.~%#          Please note that the gripper will ignore this command~%#          if the busy flag is set in the status field.~%# 0x0008 - stop~%#          Stop the current motion.~%# 0x0010 - grip_w_offset~%#          Same as grip, but width is calculated with the set fingertip offset.~%~%uint8 rCTR~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OnRobotRGOutput>))
  (cl:+ 0
     2
     2
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OnRobotRGOutput>))
  "Converts a ROS message object to a list"
  (cl:list 'OnRobotRGOutput
    (cl:cons ':rGFR (rGFR msg))
    (cl:cons ':rGWD (rGWD msg))
    (cl:cons ':rCTR (rCTR msg))
))
