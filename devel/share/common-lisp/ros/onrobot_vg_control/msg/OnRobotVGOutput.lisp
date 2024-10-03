; Auto-generated. Do not edit!


(cl:in-package onrobot_vg_control-msg)


;//! \htmlinclude OnRobotVGOutput.msg.html

(cl:defclass <OnRobotVGOutput> (roslisp-msg-protocol:ros-message)
  ((rMCA
    :reader rMCA
    :initarg :rMCA
    :type cl:fixnum
    :initform 0)
   (rVCA
    :reader rVCA
    :initarg :rVCA
    :type cl:fixnum
    :initform 0)
   (rMCB
    :reader rMCB
    :initarg :rMCB
    :type cl:fixnum
    :initform 0)
   (rVCB
    :reader rVCB
    :initarg :rVCB
    :type cl:fixnum
    :initform 0))
)

(cl:defclass OnRobotVGOutput (<OnRobotVGOutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OnRobotVGOutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OnRobotVGOutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name onrobot_vg_control-msg:<OnRobotVGOutput> is deprecated: use onrobot_vg_control-msg:OnRobotVGOutput instead.")))

(cl:ensure-generic-function 'rMCA-val :lambda-list '(m))
(cl:defmethod rMCA-val ((m <OnRobotVGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:rMCA-val is deprecated.  Use onrobot_vg_control-msg:rMCA instead.")
  (rMCA m))

(cl:ensure-generic-function 'rVCA-val :lambda-list '(m))
(cl:defmethod rVCA-val ((m <OnRobotVGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:rVCA-val is deprecated.  Use onrobot_vg_control-msg:rVCA instead.")
  (rVCA m))

(cl:ensure-generic-function 'rMCB-val :lambda-list '(m))
(cl:defmethod rMCB-val ((m <OnRobotVGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:rMCB-val is deprecated.  Use onrobot_vg_control-msg:rMCB instead.")
  (rMCB m))

(cl:ensure-generic-function 'rVCB-val :lambda-list '(m))
(cl:defmethod rVCB-val ((m <OnRobotVGOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader onrobot_vg_control-msg:rVCB-val is deprecated.  Use onrobot_vg_control-msg:rVCB instead.")
  (rVCB m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OnRobotVGOutput>) ostream)
  "Serializes a message object of type '<OnRobotVGOutput>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rMCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rMCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rVCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rVCA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rMCB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rMCB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rVCB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rVCB)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OnRobotVGOutput>) istream)
  "Deserializes a message object of type '<OnRobotVGOutput>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rMCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rMCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rVCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rVCA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rMCB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rMCB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rVCB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rVCB)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OnRobotVGOutput>)))
  "Returns string type for a message object of type '<OnRobotVGOutput>"
  "onrobot_vg_control/OnRobotVGOutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OnRobotVGOutput)))
  "Returns string type for a message object of type 'OnRobotVGOutput"
  "onrobot_vg_control/OnRobotVGOutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OnRobotVGOutput>)))
  "Returns md5sum for a message object of type '<OnRobotVGOutput>"
  "4d69df47809c592e1c34e330d53678dd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OnRobotVGOutput)))
  "Returns md5sum for a message object of type 'OnRobotVGOutput"
  "4d69df47809c592e1c34e330d53678dd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OnRobotVGOutput>)))
  "Returns full string definition for message of type '<OnRobotVGOutput>"
  (cl:format cl:nil "# rMCA : The Control mode~%# rVCA : The Target vacuume field~%#~%#        The register allows for control of channel A.~%#        The register is split into two 8-bit fields:~%#        Bits 15-8        Bits 7-0~%#        Control mode     Target vacuum~%#~%#        The Control mode field must contain one of these three values:~%#~%#        Value    Name    Description~%#        0 (0x00) Release Commands the channel to release~%#                         any work item and stop the pump,~%#                         if not required by the other channel.~%#        1 (0x01) Grip    Commands the channel to build up~%#                         and maintain vacuum on this channel.~%#        2 (0x02) Idle    Commands the channel to neither release nor grip.~%#                         Workpieces may \"stick\" to the channel~%#                         if physically pressed towards its vacuum cups,~%#                         but the VG will use slightly less power.~%#~%#        The Target vacuum field sets the level of vacuum~%#        to be build up and maintained by the chann el.~%#        It is used only when the control mode is 1 (0x01) / Grip.~%#        The target vacuum should be provided in % vacuum.~%#        It should never exceed 80.~%#~%#        Examples:~%#        Setting the register value 0 (0x0000)~%#            will command the VG to release the work item.~%#        Setting the register value 276 (0x0114)~%#            will command the VG to grip at 20 % vacuum.~%#        Setting the register value 296 (0x0128)~%#            will command the VG to grip at 40 % vacuum.~%#        Setting the register value 331 (0x014B)~%#            will command the VG to grip at 75 % vacuum.~%#        Setting the register value 512 (0x0200)~%#            will command the VG to idle the channel.~%~%uint16 rMCA~%uint16 rVCA~%~%# rVCB : Same as the one of channel A.~%~%uint16 rMCB~%uint16 rVCB~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OnRobotVGOutput)))
  "Returns full string definition for message of type 'OnRobotVGOutput"
  (cl:format cl:nil "# rMCA : The Control mode~%# rVCA : The Target vacuume field~%#~%#        The register allows for control of channel A.~%#        The register is split into two 8-bit fields:~%#        Bits 15-8        Bits 7-0~%#        Control mode     Target vacuum~%#~%#        The Control mode field must contain one of these three values:~%#~%#        Value    Name    Description~%#        0 (0x00) Release Commands the channel to release~%#                         any work item and stop the pump,~%#                         if not required by the other channel.~%#        1 (0x01) Grip    Commands the channel to build up~%#                         and maintain vacuum on this channel.~%#        2 (0x02) Idle    Commands the channel to neither release nor grip.~%#                         Workpieces may \"stick\" to the channel~%#                         if physically pressed towards its vacuum cups,~%#                         but the VG will use slightly less power.~%#~%#        The Target vacuum field sets the level of vacuum~%#        to be build up and maintained by the chann el.~%#        It is used only when the control mode is 1 (0x01) / Grip.~%#        The target vacuum should be provided in % vacuum.~%#        It should never exceed 80.~%#~%#        Examples:~%#        Setting the register value 0 (0x0000)~%#            will command the VG to release the work item.~%#        Setting the register value 276 (0x0114)~%#            will command the VG to grip at 20 % vacuum.~%#        Setting the register value 296 (0x0128)~%#            will command the VG to grip at 40 % vacuum.~%#        Setting the register value 331 (0x014B)~%#            will command the VG to grip at 75 % vacuum.~%#        Setting the register value 512 (0x0200)~%#            will command the VG to idle the channel.~%~%uint16 rMCA~%uint16 rVCA~%~%# rVCB : Same as the one of channel A.~%~%uint16 rMCB~%uint16 rVCB~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OnRobotVGOutput>))
  (cl:+ 0
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OnRobotVGOutput>))
  "Converts a ROS message object to a list"
  (cl:list 'OnRobotVGOutput
    (cl:cons ':rMCA (rMCA msg))
    (cl:cons ':rVCA (rVCA msg))
    (cl:cons ':rMCB (rMCB msg))
    (cl:cons ':rVCB (rVCB msg))
))
