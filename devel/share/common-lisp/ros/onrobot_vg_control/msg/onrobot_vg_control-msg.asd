
(cl:in-package :asdf)

(defsystem "onrobot_vg_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "OnRobotVGInput" :depends-on ("_package_OnRobotVGInput"))
    (:file "_package_OnRobotVGInput" :depends-on ("_package"))
    (:file "OnRobotVGOutput" :depends-on ("_package_OnRobotVGOutput"))
    (:file "_package_OnRobotVGOutput" :depends-on ("_package"))
  ))