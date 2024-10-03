
(cl:in-package :asdf)

(defsystem "gelsight_mini_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "judging_msg" :depends-on ("_package_judging_msg"))
    (:file "_package_judging_msg" :depends-on ("_package"))
    (:file "tracking_msg" :depends-on ("_package_tracking_msg"))
    (:file "_package_tracking_msg" :depends-on ("_package"))
  ))