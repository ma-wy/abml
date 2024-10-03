;; Auto-generated. Do not edit!


(when (boundp 'onrobot_vg_control::SetCommand)
  (if (not (find-package "ONROBOT_VG_CONTROL"))
    (make-package "ONROBOT_VG_CONTROL"))
  (shadow 'SetCommand (find-package "ONROBOT_VG_CONTROL")))
(unless (find-package "ONROBOT_VG_CONTROL::SETCOMMAND")
  (make-package "ONROBOT_VG_CONTROL::SETCOMMAND"))
(unless (find-package "ONROBOT_VG_CONTROL::SETCOMMANDREQUEST")
  (make-package "ONROBOT_VG_CONTROL::SETCOMMANDREQUEST"))
(unless (find-package "ONROBOT_VG_CONTROL::SETCOMMANDRESPONSE")
  (make-package "ONROBOT_VG_CONTROL::SETCOMMANDRESPONSE"))

(in-package "ROS")





(defclass onrobot_vg_control::SetCommandRequest
  :super ros::object
  :slots (_command ))

(defmethod onrobot_vg_control::SetCommandRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass onrobot_vg_control::SetCommandResponse
  :super ros::object
  :slots (_success _message ))

(defmethod onrobot_vg_control::SetCommandResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass onrobot_vg_control::SetCommand
  :super ros::object
  :slots ())

(setf (get onrobot_vg_control::SetCommand :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get onrobot_vg_control::SetCommand :datatype-) "onrobot_vg_control/SetCommand")
(setf (get onrobot_vg_control::SetCommand :request) onrobot_vg_control::SetCommandRequest)
(setf (get onrobot_vg_control::SetCommand :response) onrobot_vg_control::SetCommandResponse)

(defmethod onrobot_vg_control::SetCommandRequest
  (:response () (instance onrobot_vg_control::SetCommandResponse :init)))

(setf (get onrobot_vg_control::SetCommandRequest :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get onrobot_vg_control::SetCommandRequest :datatype-) "onrobot_vg_control/SetCommandRequest")
(setf (get onrobot_vg_control::SetCommandRequest :definition-)
      "string command
---
bool success
string message
")

(setf (get onrobot_vg_control::SetCommandResponse :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get onrobot_vg_control::SetCommandResponse :datatype-) "onrobot_vg_control/SetCommandResponse")
(setf (get onrobot_vg_control::SetCommandResponse :definition-)
      "string command
---
bool success
string message
")



(provide :onrobot_vg_control/SetCommand "c348f8d8cd3a80f54328aa4159009109")


