;; Auto-generated. Do not edit!


(when (boundp 'onrobot_rg_control::OnRobotRGInput)
  (if (not (find-package "ONROBOT_RG_CONTROL"))
    (make-package "ONROBOT_RG_CONTROL"))
  (shadow 'OnRobotRGInput (find-package "ONROBOT_RG_CONTROL")))
(unless (find-package "ONROBOT_RG_CONTROL::ONROBOTRGINPUT")
  (make-package "ONROBOT_RG_CONTROL::ONROBOTRGINPUT"))

(in-package "ROS")
;;//! \htmlinclude OnRobotRGInput.msg.html


(defclass onrobot_rg_control::OnRobotRGInput
  :super ros::object
  :slots (_gFOF _gGWD _gSTA _gWDF ))

(defmethod onrobot_rg_control::OnRobotRGInput
  (:init
   (&key
    ((:gFOF __gFOF) 0)
    ((:gGWD __gGWD) 0)
    ((:gSTA __gSTA) 0)
    ((:gWDF __gWDF) 0)
    )
   (send-super :init)
   (setq _gFOF (round __gFOF))
   (setq _gGWD (round __gGWD))
   (setq _gSTA (round __gSTA))
   (setq _gWDF (round __gWDF))
   self)
  (:gFOF
   (&optional __gFOF)
   (if __gFOF (setq _gFOF __gFOF)) _gFOF)
  (:gGWD
   (&optional __gGWD)
   (if __gGWD (setq _gGWD __gGWD)) _gGWD)
  (:gSTA
   (&optional __gSTA)
   (if __gSTA (setq _gSTA __gSTA)) _gSTA)
  (:gWDF
   (&optional __gWDF)
   (if __gWDF (setq _gWDF __gWDF)) _gWDF)
  (:serialization-length
   ()
   (+
    ;; uint16 _gFOF
    2
    ;; uint16 _gGWD
    2
    ;; uint8 _gSTA
    1
    ;; uint16 _gWDF
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _gFOF
       (write-word _gFOF s)
     ;; uint16 _gGWD
       (write-word _gGWD s)
     ;; uint8 _gSTA
       (write-byte _gSTA s)
     ;; uint16 _gWDF
       (write-word _gWDF s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _gFOF
     (setq _gFOF (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _gGWD
     (setq _gGWD (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _gSTA
     (setq _gSTA (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint16 _gWDF
     (setq _gWDF (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get onrobot_rg_control::OnRobotRGInput :md5sum-) "94435113a24b6809371af29f68843bdb")
(setf (get onrobot_rg_control::OnRobotRGInput :datatype-) "onrobot_rg_control/OnRobotRGInput")
(setf (get onrobot_rg_control::OnRobotRGInput :definition-)
      "# gFOF : Current fingertip offset in 1/10 millimeters. The value is a signed two's complement number.

uint16 gFOF

# gGWD : Current width between the gripper fingers in 1/10 millimeters.
#        The width is provided without any fingertip offset, as it is measured between the insides of the aluminum fingers.

uint16 gGWD

# gSTA : Current device status, which indicates the status of the gripper and its motion.
# Bit       - Name              - Description
# 0 (LSB)   - Busy              - High (1) when a motion is ongoing, low (0) when not. The gripper will only accept new commands when this flag is low.
# 1         - Grip detected     - High (1) when an internal- or external grip is detected.
# 2         - S1 pushed         - High (1) when safety switch 1 is pushed.
# 3         - S1 trigged        - High (1) when safety circuit 1 is activated. The gripper will not move while this flag is high.
# 4         - S2 pushed         - High (1) when safety switch 2 is pushed.
# 5         - S2 trigged        - High (1) when safety circuit 2 is activated. The gripper will not move while this flag is high.
# 6         - Safety error      - High (1) when on power on any of the safety switch is pushed.
# 7 - 15    - Reserved          - Not used.

uint8 gSTA

# gWDF : Current width between the gripper fingers in 1/10 millimeters.
#        The set fingertip offset is considered.

uint16 gWDF

")



(provide :onrobot_rg_control/OnRobotRGInput "94435113a24b6809371af29f68843bdb")


