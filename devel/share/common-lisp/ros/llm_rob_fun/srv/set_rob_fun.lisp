; Auto-generated. Do not edit!


(cl:in-package llm_rob_fun-srv)


;//! \htmlinclude set_rob_fun-request.msg.html

(cl:defclass <set_rob_fun-request> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:string
    :initform ""))
)

(cl:defclass set_rob_fun-request (<set_rob_fun-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <set_rob_fun-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'set_rob_fun-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_rob_fun-srv:<set_rob_fun-request> is deprecated: use llm_rob_fun-srv:set_rob_fun-request instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <set_rob_fun-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_rob_fun-srv:action-val is deprecated.  Use llm_rob_fun-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <set_rob_fun-request>) ostream)
  "Serializes a message object of type '<set_rob_fun-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <set_rob_fun-request>) istream)
  "Deserializes a message object of type '<set_rob_fun-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<set_rob_fun-request>)))
  "Returns string type for a service object of type '<set_rob_fun-request>"
  "llm_rob_fun/set_rob_funRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_rob_fun-request)))
  "Returns string type for a service object of type 'set_rob_fun-request"
  "llm_rob_fun/set_rob_funRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<set_rob_fun-request>)))
  "Returns md5sum for a message object of type '<set_rob_fun-request>"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'set_rob_fun-request)))
  "Returns md5sum for a message object of type 'set_rob_fun-request"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<set_rob_fun-request>)))
  "Returns full string definition for message of type '<set_rob_fun-request>"
  (cl:format cl:nil "string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'set_rob_fun-request)))
  "Returns full string definition for message of type 'set_rob_fun-request"
  (cl:format cl:nil "string action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <set_rob_fun-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <set_rob_fun-request>))
  "Converts a ROS message object to a list"
  (cl:list 'set_rob_fun-request
    (cl:cons ':action (action msg))
))
;//! \htmlinclude set_rob_fun-response.msg.html

(cl:defclass <set_rob_fun-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass set_rob_fun-response (<set_rob_fun-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <set_rob_fun-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'set_rob_fun-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name llm_rob_fun-srv:<set_rob_fun-response> is deprecated: use llm_rob_fun-srv:set_rob_fun-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <set_rob_fun-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader llm_rob_fun-srv:success-val is deprecated.  Use llm_rob_fun-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <set_rob_fun-response>) ostream)
  "Serializes a message object of type '<set_rob_fun-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <set_rob_fun-response>) istream)
  "Deserializes a message object of type '<set_rob_fun-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<set_rob_fun-response>)))
  "Returns string type for a service object of type '<set_rob_fun-response>"
  "llm_rob_fun/set_rob_funResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_rob_fun-response)))
  "Returns string type for a service object of type 'set_rob_fun-response"
  "llm_rob_fun/set_rob_funResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<set_rob_fun-response>)))
  "Returns md5sum for a message object of type '<set_rob_fun-response>"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'set_rob_fun-response)))
  "Returns md5sum for a message object of type 'set_rob_fun-response"
  "02058b7d55716526fae62eb68abd6f31")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<set_rob_fun-response>)))
  "Returns full string definition for message of type '<set_rob_fun-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'set_rob_fun-response)))
  "Returns full string definition for message of type 'set_rob_fun-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <set_rob_fun-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <set_rob_fun-response>))
  "Converts a ROS message object to a list"
  (cl:list 'set_rob_fun-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'set_rob_fun)))
  'set_rob_fun-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'set_rob_fun)))
  'set_rob_fun-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_rob_fun)))
  "Returns string type for a service object of type '<set_rob_fun>"
  "llm_rob_fun/set_rob_fun")