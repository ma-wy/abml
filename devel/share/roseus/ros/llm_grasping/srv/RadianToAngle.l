;; Auto-generated. Do not edit!


(when (boundp 'llm_grasping::RadianToAngle)
  (if (not (find-package "LLM_GRASPING"))
    (make-package "LLM_GRASPING"))
  (shadow 'RadianToAngle (find-package "LLM_GRASPING")))
(unless (find-package "LLM_GRASPING::RADIANTOANGLE")
  (make-package "LLM_GRASPING::RADIANTOANGLE"))
(unless (find-package "LLM_GRASPING::RADIANTOANGLEREQUEST")
  (make-package "LLM_GRASPING::RADIANTOANGLEREQUEST"))
(unless (find-package "LLM_GRASPING::RADIANTOANGLERESPONSE")
  (make-package "LLM_GRASPING::RADIANTOANGLERESPONSE"))

(in-package "ROS")





(defclass llm_grasping::RadianToAngleRequest
  :super ros::object
  :slots (_radian ))

(defmethod llm_grasping::RadianToAngleRequest
  (:init
   (&key
    ((:radian __radian) 0.0)
    )
   (send-super :init)
   (setq _radian (float __radian))
   self)
  (:radian
   (&optional __radian)
   (if __radian (setq _radian __radian)) _radian)
  (:serialization-length
   ()
   (+
    ;; float64 _radian
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _radian
       (sys::poke _radian (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _radian
     (setq _radian (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass llm_grasping::RadianToAngleResponse
  :super ros::object
  :slots (_angle _success ))

(defmethod llm_grasping::RadianToAngleResponse
  (:init
   (&key
    ((:angle __angle) 0.0)
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _angle (float __angle))
   (setq _success __success)
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; float64 _angle
    8
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _angle
     (setq _angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass llm_grasping::RadianToAngle
  :super ros::object
  :slots ())

(setf (get llm_grasping::RadianToAngle :md5sum-) "8dd47fc5494973709ed579a85c77ce44")
(setf (get llm_grasping::RadianToAngle :datatype-) "llm_grasping/RadianToAngle")
(setf (get llm_grasping::RadianToAngle :request) llm_grasping::RadianToAngleRequest)
(setf (get llm_grasping::RadianToAngle :response) llm_grasping::RadianToAngleResponse)

(defmethod llm_grasping::RadianToAngleRequest
  (:response () (instance llm_grasping::RadianToAngleResponse :init)))

(setf (get llm_grasping::RadianToAngleRequest :md5sum-) "8dd47fc5494973709ed579a85c77ce44")
(setf (get llm_grasping::RadianToAngleRequest :datatype-) "llm_grasping/RadianToAngleRequest")
(setf (get llm_grasping::RadianToAngleRequest :definition-)
      "float64 radian
---
float64 angle
bool success

")

(setf (get llm_grasping::RadianToAngleResponse :md5sum-) "8dd47fc5494973709ed579a85c77ce44")
(setf (get llm_grasping::RadianToAngleResponse :datatype-) "llm_grasping/RadianToAngleResponse")
(setf (get llm_grasping::RadianToAngleResponse :definition-)
      "float64 radian
---
float64 angle
bool success

")



(provide :llm_grasping/RadianToAngle "8dd47fc5494973709ed579a85c77ce44")


