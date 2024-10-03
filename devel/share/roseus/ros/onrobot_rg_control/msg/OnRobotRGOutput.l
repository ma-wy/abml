;; Auto-generated. Do not edit!


(when (boundp 'onrobot_rg_control::OnRobotRGOutput)
  (if (not (find-package "ONROBOT_RG_CONTROL"))
    (make-package "ONROBOT_RG_CONTROL"))
  (shadow 'OnRobotRGOutput (find-package "ONROBOT_RG_CONTROL")))
(unless (find-package "ONROBOT_RG_CONTROL::ONROBOTRGOUTPUT")
  (make-package "ONROBOT_RG_CONTROL::ONROBOTRGOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude OnRobotRGOutput.msg.html


(defclass onrobot_rg_control::OnRobotRGOutput
  :super ros::object
  :slots (_rGFR _rGWD _rCTR ))

(defmethod onrobot_rg_control::OnRobotRGOutput
  (:init
   (&key
    ((:rGFR __rGFR) 0)
    ((:rGWD __rGWD) 0)
    ((:rCTR __rCTR) 0)
    )
   (send-super :init)
   (setq _rGFR (round __rGFR))
   (setq _rGWD (round __rGWD))
   (setq _rCTR (round __rCTR))
   self)
  (:rGFR
   (&optional __rGFR)
   (if __rGFR (setq _rGFR __rGFR)) _rGFR)
  (:rGWD
   (&optional __rGWD)
   (if __rGWD (setq _rGWD __rGWD)) _rGWD)
  (:rCTR
   (&optional __rCTR)
   (if __rCTR (setq _rCTR __rCTR)) _rCTR)
  (:serialization-length
   ()
   (+
    ;; uint16 _rGFR
    2
    ;; uint16 _rGWD
    2
    ;; uint8 _rCTR
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _rGFR
       (write-word _rGFR s)
     ;; uint16 _rGWD
       (write-word _rGWD s)
     ;; uint8 _rCTR
       (write-byte _rCTR s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _rGFR
     (setq _rGFR (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _rGWD
     (setq _rGWD (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _rCTR
     (setq _rCTR (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get onrobot_rg_control::OnRobotRGOutput :md5sum-) "d99680fed3cb1854614e74f47d8e8f52")
(setf (get onrobot_rg_control::OnRobotRGOutput :datatype-) "onrobot_rg_control/OnRobotRGOutput")
(setf (get onrobot_rg_control::OnRobotRGOutput :definition-)
      "# rGFR : The target force to be reached when gripping and holding a workpiece.
#        It must be provided in 1/10th Newtons.
#        The valid range is 0 to 400 for the RG2 and 0 to 1200 for the RG6.

uint16 rGFR

# rGWD : The target width between the finger to be moved to and maintained.
#        It must be provided in 1/10th millimeters.
#        The valid range is 0 to 1100 for the RG2 and 0 to 1600 for the RG6.
#        Please note that the target width should be provided corrected for any fingertip offset,
#        as it is measured between the insides of the aluminum fingers.

uint16 rGWD

# rCTR : The control field is used to start and stop gripper motion.
#        Only one option should be set at a time.
#        Please note that the gripper will not start a new motion
#        before the one currently being executed is done (see busy flag in the Status field).
# 0x0001 - grip
#          Start the motion, with the preset target force and width.
#          Width is calculated without the fingertip offset.
#          Please note that the gripper will ignore this command
#          if the busy flag is set in the status field.
# 0x0008 - stop
#          Stop the current motion.
# 0x0010 - grip_w_offset
#          Same as grip, but width is calculated with the set fingertip offset.

uint8 rCTR
")



(provide :onrobot_rg_control/OnRobotRGOutput "d99680fed3cb1854614e74f47d8e8f52")


