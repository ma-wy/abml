;; Auto-generated. Do not edit!


(when (boundp 'onrobot_vg_control::OnRobotVGOutput)
  (if (not (find-package "ONROBOT_VG_CONTROL"))
    (make-package "ONROBOT_VG_CONTROL"))
  (shadow 'OnRobotVGOutput (find-package "ONROBOT_VG_CONTROL")))
(unless (find-package "ONROBOT_VG_CONTROL::ONROBOTVGOUTPUT")
  (make-package "ONROBOT_VG_CONTROL::ONROBOTVGOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude OnRobotVGOutput.msg.html


(defclass onrobot_vg_control::OnRobotVGOutput
  :super ros::object
  :slots (_rMCA _rVCA _rMCB _rVCB ))

(defmethod onrobot_vg_control::OnRobotVGOutput
  (:init
   (&key
    ((:rMCA __rMCA) 0)
    ((:rVCA __rVCA) 0)
    ((:rMCB __rMCB) 0)
    ((:rVCB __rVCB) 0)
    )
   (send-super :init)
   (setq _rMCA (round __rMCA))
   (setq _rVCA (round __rVCA))
   (setq _rMCB (round __rMCB))
   (setq _rVCB (round __rVCB))
   self)
  (:rMCA
   (&optional __rMCA)
   (if __rMCA (setq _rMCA __rMCA)) _rMCA)
  (:rVCA
   (&optional __rVCA)
   (if __rVCA (setq _rVCA __rVCA)) _rVCA)
  (:rMCB
   (&optional __rMCB)
   (if __rMCB (setq _rMCB __rMCB)) _rMCB)
  (:rVCB
   (&optional __rVCB)
   (if __rVCB (setq _rVCB __rVCB)) _rVCB)
  (:serialization-length
   ()
   (+
    ;; uint16 _rMCA
    2
    ;; uint16 _rVCA
    2
    ;; uint16 _rMCB
    2
    ;; uint16 _rVCB
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _rMCA
       (write-word _rMCA s)
     ;; uint16 _rVCA
       (write-word _rVCA s)
     ;; uint16 _rMCB
       (write-word _rMCB s)
     ;; uint16 _rVCB
       (write-word _rVCB s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _rMCA
     (setq _rMCA (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _rVCA
     (setq _rVCA (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _rMCB
     (setq _rMCB (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _rVCB
     (setq _rVCB (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get onrobot_vg_control::OnRobotVGOutput :md5sum-) "4d69df47809c592e1c34e330d53678dd")
(setf (get onrobot_vg_control::OnRobotVGOutput :datatype-) "onrobot_vg_control/OnRobotVGOutput")
(setf (get onrobot_vg_control::OnRobotVGOutput :definition-)
      "# rMCA : The Control mode
# rVCA : The Target vacuume field
#
#        The register allows for control of channel A.
#        The register is split into two 8-bit fields:
#        Bits 15-8        Bits 7-0
#        Control mode     Target vacuum
#
#        The Control mode field must contain one of these three values:
#
#        Value    Name    Description
#        0 (0x00) Release Commands the channel to release
#                         any work item and stop the pump,
#                         if not required by the other channel.
#        1 (0x01) Grip    Commands the channel to build up
#                         and maintain vacuum on this channel.
#        2 (0x02) Idle    Commands the channel to neither release nor grip.
#                         Workpieces may \"stick\" to the channel
#                         if physically pressed towards its vacuum cups,
#                         but the VG will use slightly less power.
#
#        The Target vacuum field sets the level of vacuum
#        to be build up and maintained by the chann el.
#        It is used only when the control mode is 1 (0x01) / Grip.
#        The target vacuum should be provided in % vacuum.
#        It should never exceed 80.
#
#        Examples:
#        Setting the register value 0 (0x0000)
#            will command the VG to release the work item.
#        Setting the register value 276 (0x0114)
#            will command the VG to grip at 20 % vacuum.
#        Setting the register value 296 (0x0128)
#            will command the VG to grip at 40 % vacuum.
#        Setting the register value 331 (0x014B)
#            will command the VG to grip at 75 % vacuum.
#        Setting the register value 512 (0x0200)
#            will command the VG to idle the channel.

uint16 rMCA
uint16 rVCA

# rVCB : Same as the one of channel A.

uint16 rMCB
uint16 rVCB

")



(provide :onrobot_vg_control/OnRobotVGOutput "4d69df47809c592e1c34e330d53678dd")


