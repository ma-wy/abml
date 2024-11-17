
(cl:in-package :asdf)

(defsystem "llm_rob_fun-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "set_rob_fun" :depends-on ("_package_set_rob_fun"))
    (:file "_package_set_rob_fun" :depends-on ("_package"))
  ))