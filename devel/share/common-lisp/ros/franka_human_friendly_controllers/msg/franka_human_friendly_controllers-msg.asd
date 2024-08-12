
(cl:in-package :asdf)

(defsystem "franka_human_friendly_controllers-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "JointTorqueComparison" :depends-on ("_package_JointTorqueComparison"))
    (:file "_package_JointTorqueComparison" :depends-on ("_package"))
    (:file "JointTorqueState" :depends-on ("_package_JointTorqueState"))
    (:file "_package_JointTorqueState" :depends-on ("_package"))
  ))