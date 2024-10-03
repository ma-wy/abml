;; Auto-generated. Do not edit!


(when (boundp 'gelsight_mini_ros::ResetMarkerTracker)
  (if (not (find-package "GELSIGHT_MINI_ROS"))
    (make-package "GELSIGHT_MINI_ROS"))
  (shadow 'ResetMarkerTracker (find-package "GELSIGHT_MINI_ROS")))
(unless (find-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKER")
  (make-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKER"))
(unless (find-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKERREQUEST")
  (make-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKERREQUEST"))
(unless (find-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKERRESPONSE")
  (make-package "GELSIGHT_MINI_ROS::RESETMARKERTRACKERRESPONSE"))

(in-package "ROS")





(defclass gelsight_mini_ros::ResetMarkerTrackerRequest
  :super ros::object
  :slots (_flag ))

(defmethod gelsight_mini_ros::ResetMarkerTrackerRequest
  (:init
   (&key
    ((:flag __flag) nil)
    )
   (send-super :init)
   (setq _flag __flag)
   self)
  (:flag
   (&optional (__flag :null))
   (if (not (eq __flag :null)) (setq _flag __flag)) _flag)
  (:serialization-length
   ()
   (+
    ;; bool _flag
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _flag
       (if _flag (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _flag
     (setq _flag (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass gelsight_mini_ros::ResetMarkerTrackerResponse
  :super ros::object
  :slots (_success ))

(defmethod gelsight_mini_ros::ResetMarkerTrackerResponse
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

(defclass gelsight_mini_ros::ResetMarkerTracker
  :super ros::object
  :slots ())

(setf (get gelsight_mini_ros::ResetMarkerTracker :md5sum-) "652fe242855f56226caf0d487b3cf6bf")
(setf (get gelsight_mini_ros::ResetMarkerTracker :datatype-) "gelsight_mini_ros/ResetMarkerTracker")
(setf (get gelsight_mini_ros::ResetMarkerTracker :request) gelsight_mini_ros::ResetMarkerTrackerRequest)
(setf (get gelsight_mini_ros::ResetMarkerTracker :response) gelsight_mini_ros::ResetMarkerTrackerResponse)

(defmethod gelsight_mini_ros::ResetMarkerTrackerRequest
  (:response () (instance gelsight_mini_ros::ResetMarkerTrackerResponse :init)))

(setf (get gelsight_mini_ros::ResetMarkerTrackerRequest :md5sum-) "652fe242855f56226caf0d487b3cf6bf")
(setf (get gelsight_mini_ros::ResetMarkerTrackerRequest :datatype-) "gelsight_mini_ros/ResetMarkerTrackerRequest")
(setf (get gelsight_mini_ros::ResetMarkerTrackerRequest :definition-)
      "bool flag
---
bool success

")

(setf (get gelsight_mini_ros::ResetMarkerTrackerResponse :md5sum-) "652fe242855f56226caf0d487b3cf6bf")
(setf (get gelsight_mini_ros::ResetMarkerTrackerResponse :datatype-) "gelsight_mini_ros/ResetMarkerTrackerResponse")
(setf (get gelsight_mini_ros::ResetMarkerTrackerResponse :definition-)
      "bool flag
---
bool success

")



(provide :gelsight_mini_ros/ResetMarkerTracker "652fe242855f56226caf0d487b3cf6bf")


