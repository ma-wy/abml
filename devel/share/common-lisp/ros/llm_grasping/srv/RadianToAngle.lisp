; Auto-generated. Do not edit!


(cl:in-package llm_grasping-srv)


;//! \htmlinclude RadianToAngle-request.msg.html

(cl:defclass <RadianToAngle-request> (roslisp-msg-protocol:ros-message)
  ((radian
    :reader radian
    :initarg :radian
    :type cl:float
    :initform 0.0))
)

(cl:defclass RadianToAngle-request (<RadianToAngle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RadianToAngle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RadianToAngle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_grasping-srv:<RadianToAngle-request> is deprecated: use llm_grasping-srv:RadianToAngle-request instead.")))

(cl:ensure-generic-function 'radian-val :lambda-list '(m))
(cl:defmethod radian-val ((m <RadianToAngle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_grasping-srv:radian-val is deprecated.  Use llm_grasping-srv:radian instead.")
  (radian m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RadianToAngle-request>) ostream)
  "Serializes a message object of type '<RadianToAngle-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'radian))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RadianToAngle-request>) istream)
  "Deserializes a message object of type '<RadianToAngle-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'radian) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RadianToAngle-request>)))
  "Returns string type for a service object of type '<RadianToAngle-request>"
  "llm_grasping/RadianToAngleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RadianToAngle-request)))
  "Returns string type for a service object of type 'RadianToAngle-request"
  "llm_grasping/RadianToAngleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RadianToAngle-request>)))
  "Returns md5sum for a message object of type '<RadianToAngle-request>"
  "8dd47fc5494973709ed579a85c77ce44")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RadianToAngle-request)))
  "Returns md5sum for a message object of type 'RadianToAngle-request"
  "8dd47fc5494973709ed579a85c77ce44")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RadianToAngle-request>)))
  "Returns full string definition for message of type '<RadianToAngle-request>"
  (cl:format cl:nil "float64 radian~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RadianToAngle-request)))
  "Returns full string definition for message of type 'RadianToAngle-request"
  (cl:format cl:nil "float64 radian~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RadianToAngle-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RadianToAngle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RadianToAngle-request
    (cl:cons ':radian (radian msg))
))
;//! \htmlinclude RadianToAngle-response.msg.html

(cl:defclass <RadianToAngle-response> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RadianToAngle-response (<RadianToAngle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RadianToAngle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RadianToAngle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_grasping-srv:<RadianToAngle-response> is deprecated: use llm_grasping-srv:RadianToAngle-response instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <RadianToAngle-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_grasping-srv:angle-val is deprecated.  Use llm_grasping-srv:angle instead.")
  (angle m))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <RadianToAngle-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_grasping-srv:success-val is deprecated.  Use llm_grasping-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RadianToAngle-response>) ostream)
  "Serializes a message object of type '<RadianToAngle-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RadianToAngle-response>) istream)
  "Deserializes a message object of type '<RadianToAngle-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RadianToAngle-response>)))
  "Returns string type for a service object of type '<RadianToAngle-response>"
  "llm_grasping/RadianToAngleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RadianToAngle-response)))
  "Returns string type for a service object of type 'RadianToAngle-response"
  "llm_grasping/RadianToAngleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RadianToAngle-response>)))
  "Returns md5sum for a message object of type '<RadianToAngle-response>"
  "8dd47fc5494973709ed579a85c77ce44")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RadianToAngle-response)))
  "Returns md5sum for a message object of type 'RadianToAngle-response"
  "8dd47fc5494973709ed579a85c77ce44")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RadianToAngle-response>)))
  "Returns full string definition for message of type '<RadianToAngle-response>"
  (cl:format cl:nil "float64 angle~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RadianToAngle-response)))
  "Returns full string definition for message of type 'RadianToAngle-response"
  (cl:format cl:nil "float64 angle~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RadianToAngle-response>))
  (cl:+ 0
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RadianToAngle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RadianToAngle-response
    (cl:cons ':angle (angle msg))
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RadianToAngle)))
  'RadianToAngle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RadianToAngle)))
  'RadianToAngle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RadianToAngle)))
  "Returns string type for a service object of type '<RadianToAngle>"
  "llm_grasping/RadianToAngle")