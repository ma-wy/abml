; Auto-generated. Do not edit!


(cl:in-package gelsight_mini_ros-srv)


;//! \htmlinclude ResetMarkerTracker-request.msg.html

(cl:defclass <ResetMarkerTracker-request> (roslisp-msg-protocol:ros-message)
  ((flag
    :reader flag
    :initarg :flag
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ResetMarkerTracker-request (<ResetMarkerTracker-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ResetMarkerTracker-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ResetMarkerTracker-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gelsight_mini_ros-srv:<ResetMarkerTracker-request> is deprecated: use gelsight_mini_ros-srv:ResetMarkerTracker-request instead.")))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <ResetMarkerTracker-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-srv:flag-val is deprecated.  Use gelsight_mini_ros-srv:flag instead.")
  (flag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ResetMarkerTracker-request>) ostream)
  "Serializes a message object of type '<ResetMarkerTracker-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flag) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ResetMarkerTracker-request>) istream)
  "Deserializes a message object of type '<ResetMarkerTracker-request>"
    (cl:setf (cl:slot-value msg 'flag) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ResetMarkerTracker-request>)))
  "Returns string type for a service object of type '<ResetMarkerTracker-request>"
  "gelsight_mini_ros/ResetMarkerTrackerRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResetMarkerTracker-request)))
  "Returns string type for a service object of type 'ResetMarkerTracker-request"
  "gelsight_mini_ros/ResetMarkerTrackerRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ResetMarkerTracker-request>)))
  "Returns md5sum for a message object of type '<ResetMarkerTracker-request>"
  "652fe242855f56226caf0d487b3cf6bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ResetMarkerTracker-request)))
  "Returns md5sum for a message object of type 'ResetMarkerTracker-request"
  "652fe242855f56226caf0d487b3cf6bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ResetMarkerTracker-request>)))
  "Returns full string definition for message of type '<ResetMarkerTracker-request>"
  (cl:format cl:nil "bool flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ResetMarkerTracker-request)))
  "Returns full string definition for message of type 'ResetMarkerTracker-request"
  (cl:format cl:nil "bool flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ResetMarkerTracker-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ResetMarkerTracker-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ResetMarkerTracker-request
    (cl:cons ':flag (flag msg))
))
;//! \htmlinclude ResetMarkerTracker-response.msg.html

(cl:defclass <ResetMarkerTracker-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ResetMarkerTracker-response (<ResetMarkerTracker-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ResetMarkerTracker-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ResetMarkerTracker-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gelsight_mini_ros-srv:<ResetMarkerTracker-response> is deprecated: use gelsight_mini_ros-srv:ResetMarkerTracker-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ResetMarkerTracker-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-srv:success-val is deprecated.  Use gelsight_mini_ros-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ResetMarkerTracker-response>) ostream)
  "Serializes a message object of type '<ResetMarkerTracker-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ResetMarkerTracker-response>) istream)
  "Deserializes a message object of type '<ResetMarkerTracker-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ResetMarkerTracker-response>)))
  "Returns string type for a service object of type '<ResetMarkerTracker-response>"
  "gelsight_mini_ros/ResetMarkerTrackerResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResetMarkerTracker-response)))
  "Returns string type for a service object of type 'ResetMarkerTracker-response"
  "gelsight_mini_ros/ResetMarkerTrackerResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ResetMarkerTracker-response>)))
  "Returns md5sum for a message object of type '<ResetMarkerTracker-response>"
  "652fe242855f56226caf0d487b3cf6bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ResetMarkerTracker-response)))
  "Returns md5sum for a message object of type 'ResetMarkerTracker-response"
  "652fe242855f56226caf0d487b3cf6bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ResetMarkerTracker-response>)))
  "Returns full string definition for message of type '<ResetMarkerTracker-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ResetMarkerTracker-response)))
  "Returns full string definition for message of type 'ResetMarkerTracker-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ResetMarkerTracker-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ResetMarkerTracker-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ResetMarkerTracker-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ResetMarkerTracker)))
  'ResetMarkerTracker-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ResetMarkerTracker)))
  'ResetMarkerTracker-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResetMarkerTracker)))
  "Returns string type for a service object of type '<ResetMarkerTracker>"
  "gelsight_mini_ros/ResetMarkerTracker")