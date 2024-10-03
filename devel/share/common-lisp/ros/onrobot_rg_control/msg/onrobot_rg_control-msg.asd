
(cl:in-package :asdf)

(defsystem "onrobot_rg_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "OnRobotRGInput" :depends-on ("_package_OnRobotRGInput"))
    (:file "_package_OnRobotRGInput" :depends-on ("_package"))
    (:file "OnRobotRGOutput" :depends-on ("_package_OnRobotRGOutput"))
    (:file "_package_OnRobotRGOutput" :depends-on ("_package"))
  ))