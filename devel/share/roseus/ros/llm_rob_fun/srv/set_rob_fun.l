;; Auto-generated. Do not edit!


(when (boundp 'llm_rob_fun::set_rob_fun)
  (if (not (find-package "LLM_ROB_FUN"))
    (make-package "LLM_ROB_FUN"))
  (shadow 'set_rob_fun (find-package "LLM_ROB_FUN")))
(unless (find-package "LLM_ROB_FUN::SET_ROB_FUN")
  (make-package "LLM_ROB_FUN::SET_ROB_FUN"))
(unless (find-package "LLM_ROB_FUN::SET_ROB_FUNREQUEST")
  (make-package "LLM_ROB_FUN::SET_ROB_FUNREQUEST"))
(unless (find-package "LLM_ROB_FUN::SET_ROB_FUNRESPONSE")
  (make-package "LLM_ROB_FUN::SET_ROB_FUNRESPONSE"))

(in-package "ROS")





(defclass llm_rob_fun::set_rob_funRequest
  :super ros::object
  :slots (_action ))

(defmethod llm_rob_fun::set_rob_funRequest
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

(defclass llm_rob_fun::set_rob_funResponse
  :super ros::object
  :slots (_success ))

(defmethod llm_rob_fun::set_rob_funResponse
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

(defclass llm_rob_fun::set_rob_fun
  :super ros::object
  :slots ())

(setf (get llm_rob_fun::set_rob_fun :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_rob_fun::set_rob_fun :datatype-) "llm_rob_fun/set_rob_fun")
(setf (get llm_rob_fun::set_rob_fun :request) llm_rob_fun::set_rob_funRequest)
(setf (get llm_rob_fun::set_rob_fun :response) llm_rob_fun::set_rob_funResponse)

(defmethod llm_rob_fun::set_rob_funRequest
  (:response () (instance llm_rob_fun::set_rob_funResponse :init)))

(setf (get llm_rob_fun::set_rob_funRequest :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_rob_fun::set_rob_funRequest :datatype-) "llm_rob_fun/set_rob_funRequest")
(setf (get llm_rob_fun::set_rob_funRequest :definition-)
      "string action
---
bool success

")

(setf (get llm_rob_fun::set_rob_funResponse :md5sum-) "02058b7d55716526fae62eb68abd6f31")
(setf (get llm_rob_fun::set_rob_funResponse :datatype-) "llm_rob_fun/set_rob_funResponse")
(setf (get llm_rob_fun::set_rob_funResponse :definition-)
      "string action
---
bool success

")



(provide :llm_rob_fun/set_rob_fun "02058b7d55716526fae62eb68abd6f31")


