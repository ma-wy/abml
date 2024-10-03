;; Auto-generated. Do not edit!


(when (boundp 'onrobot_vg_control::OnRobotVGInput)
  (if (not (find-package "ONROBOT_VG_CONTROL"))
    (make-package "ONROBOT_VG_CONTROL"))
  (shadow 'OnRobotVGInput (find-package "ONROBOT_VG_CONTROL")))
(unless (find-package "ONROBOT_VG_CONTROL::ONROBOTVGINPUT")
  (make-package "ONROBOT_VG_CONTROL::ONROBOTVGINPUT"))

(in-package "ROS")
;;//! \htmlinclude OnRobotVGInput.msg.html


(defclass onrobot_vg_control::OnRobotVGInput
  :super ros::object
  :slots (_gVCA _gVCB ))

(defmethod onrobot_vg_control::OnRobotVGInput
  (:init
   (&key
    ((:gVCA __gVCA) 0)
    ((:gVCB __gVCB) 0)
    )
   (send-super :init)
   (setq _gVCA (round __gVCA))
   (setq _gVCB (round __gVCB))
   self)
  (:gVCA
   (&optional __gVCA)
   (if __gVCA (setq _gVCA __gVCA)) _gVCA)
  (:gVCB
   (&optional __gVCB)
   (if __gVCB (setq _gVCB __gVCB)) _gVCB)
  (:serialization-length
   ()
   (+
    ;; uint16 _gVCA
    2
    ;; uint16 _gVCB
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _gVCA
       (write-word _gVCA s)
     ;; uint16 _gVCB
       (write-word _gVCB s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _gVCA
     (setq _gVCA (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _gVCB
     (setq _gVCB (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get onrobot_vg_control::OnRobotVGInput :md5sum-) "3b28006a7c1a9b8e6a658a70e5ab4a0d")
(setf (get onrobot_vg_control::OnRobotVGInput :datatype-) "onrobot_vg_control/OnRobotVGInput")
(setf (get onrobot_vg_control::OnRobotVGInput :definition-)
      "# gVCA : Current vacuum value on Channel A.
#        The vacuum is provided in 1/1000 of relative vacuum.
#        Please note that this differs from the setpoint given in percent,
#        as extra accuracy is desirable on the actual vacuum.

uint16 gVCA

# gVCB : Same as the one of channel A.

uint16 gVCB

")



(provide :onrobot_vg_control/OnRobotVGInput "3b28006a7c1a9b8e6a658a70e5ab4a0d")


