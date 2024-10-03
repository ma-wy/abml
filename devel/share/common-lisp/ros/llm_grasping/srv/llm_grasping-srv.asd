
(cl:in-package :asdf)

(defsystem "llm_grasping-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RadianToAngle" :depends-on ("_package_RadianToAngle"))
    (:file "_package_RadianToAngle" :depends-on ("_package"))
    (:file "SetRobFun" :depends-on ("_package_SetRobFun"))
    (:file "_package_SetRobFun" :depends-on ("_package"))
  ))