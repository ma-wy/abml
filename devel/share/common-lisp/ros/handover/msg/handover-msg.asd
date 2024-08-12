
(cl:in-package :asdf)

(defsystem "handover-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "hand_mp" :depends-on ("_package_hand_mp"))
    (:file "_package_hand_mp" :depends-on ("_package"))
  ))