
(cl:in-package :asdf)

(defsystem "gelsight_mini_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ResetMarkerTracker" :depends-on ("_package_ResetMarkerTracker"))
    (:file "_package_ResetMarkerTracker" :depends-on ("_package"))
  ))