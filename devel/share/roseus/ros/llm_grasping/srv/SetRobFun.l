;; Auto-generated. Do not edit!


(when (boundp 'llm_grasping::SetRobFun)
  (if (not (find-package "LLM_GRASPING"))
    (make-package "LLM_GRASPING"))
  (shadow 'SetRobFun (find-package "LLM_GRASPING")))
(unless (find-package "LLM_GRASPING::SETROBFUN")
  (make-package "LLM_GRASPING::SETROBFUN"))
(unless (find-package "LLM_GRASPING::SETROBFUNREQUEST")
  (make-package "LLM_GRASPING::SETROBFUNREQUEST"))
(unless (find-package "LLM_GRASPING::SETROBFUNRESPONSE")
  (make-package "LLM_GRASPING::SETROBFUNRESPONSE"))

(in-package "ROS")





(defclass llm_grasping::SetRobFunRequest
  :super ros::object
  :slots (_action ))

(defmethod llm_grasping::SetRobFunRequest
  (:init
   (&key
    ((:action __action) "")
    )
   (send-super :init)
   (setq _action (string __action))
   self)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:serialization-length
   ()
   (+
    ;; string _action
    4 (length _action)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _action
       (write-long (length _action) s) (princ _action s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _action
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass llm_grasping::SetRobFunResponse
  :super ros::object
  :slots (_success ))

(defmethod llm_grasping::SetRobFunResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass llm_grasping::SetRobFun
  :super ros::object
  :slots ())

(setf (get llm_grasping::SetRobFun :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_grasping::SetRobFun :datatype-) "llm_grasping/SetRobFun")
(setf (get llm_grasping::SetRobFun :request) llm_grasping::SetRobFunRequest)
(setf (get llm_grasping::SetRobFun :response) llm_grasping::SetRobFunResponse)

(defmethod llm_grasping::SetRobFunRequest
  (:response () (instance llm_grasping::SetRobFunResponse :init)))

(setf (get llm_grasping::SetRobFunRequest :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_grasping::SetRobFunRequest :datatype-) "llm_grasping/SetRobFunRequest")
(setf (get llm_grasping::SetRobFunRequest :definition-)
      "string action
---
bool success

")

(setf (get llm_grasping::SetRobFunResponse :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_grasping::SetRobFunResponse :datatype-) "llm_grasping/SetRobFunResponse")
(setf (get llm_grasping::SetRobFunResponse :definition-)
      "string action
---
bool success

")



(provide :llm_grasping/SetRobFun "02058b7d55716526fae62eb68abd6f31")


