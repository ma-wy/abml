; Auto-generated. Do not edit!


(cl:in-package llm_grasping-srv)


;//! \htmlinclude SetRobFun-request.msg.html

(cl:defclass <SetRobFun-request> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:string
    :initform ""))
)

(cl:defclass SetRobFun-request (<SetRobFun-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetRobFun-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetRobFun-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_grasping-srv:<SetRobFun-request> is deprecated: use llm_grasping-srv:SetRobFun-request instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <SetRobFun-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_grasping-srv:action-val is deprecated.  Use llm_grasping-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetRobFun-request>) ostream)
  "Serializes a message object of type '<SetRobFun-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetRobFun-request>) istream)
  "Deserializes a message object of type '<SetRobFun-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetRobFun-request>)))
  "Returns string type for a service object of type '<SetRobFun-request>"
  "llm_grasping/SetRobFunRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobFun-request)))
  "Returns string type for a service object of type 'SetRobFun-request"
  "llm_grasping/SetRobFunRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetRobFun-request>)))
  "Returns md5sum for a message object of type '<SetRobFun-request>"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetRobFun-request)))
  "Returns md5sum for a message object of type 'SetRobFun-request"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetRobFun-request>)))
  "Returns full string definition for message of type '<SetRobFun-request>"
  (cl:format cl:nil "string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetRobFun-request)))
  "Returns full string definition for message of type 'SetRobFun-request"
  (cl:format cl:nil "string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetRobFun-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetRobFun-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetRobFun-request
    (cl:cons ':action (action msg))
))
;//! \htmlinclude SetRobFun-response.msg.html

(cl:defclass <SetRobFun-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetRobFun-response (<SetRobFun-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetRobFun-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetRobFun-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_grasping-srv:<SetRobFun-response> is deprecated: use llm_grasping-srv:SetRobFun-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetRobFun-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_grasping-srv:success-val is deprecated.  Use llm_grasping-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetRobFun-response>) ostream)
  "Serializes a message object of type '<SetRobFun-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetRobFun-response>) istream)
  "Deserializes a message object of type '<SetRobFun-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetRobFun-response>)))
  "Returns string type for a service object of type '<SetRobFun-response>"
  "llm_grasping/SetRobFunResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobFun-response)))
  "Returns string type for a service object of type 'SetRobFun-response"
  "llm_grasping/SetRobFunResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetRobFun-response>)))
  "Returns md5sum for a message object of type '<SetRobFun-response>"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetRobFun-response)))
  "Returns md5sum for a message object of type 'SetRobFun-response"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetRobFun-response>)))
  "Returns full string definition for message of type '<SetRobFun-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetRobFun-response)))
  "Returns full string definition for message of type 'SetRobFun-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetRobFun-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetRobFun-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetRobFun-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetRobFun)))
  'SetRobFun-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetRobFun)))
  'SetRobFun-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobFun)))
  "Returns string type for a service object of type '<SetRobFun>"
  "llm_grasping/SetRobFun")