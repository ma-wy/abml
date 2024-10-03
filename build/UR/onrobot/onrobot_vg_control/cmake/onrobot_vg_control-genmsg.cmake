# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "onrobot_vg_control: 2 messages, 1 services")

set(MSG_I_FLAGS "-Ionrobot_vg_control:/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(onrobot_vg_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_custom_target(_onrobot_vg_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "onrobot_vg_control" "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" ""
)

get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_custom_target(_onrobot_vg_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "onrobot_vg_control" "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" ""
)

get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_custom_target(_onrobot_vg_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "onrobot_vg_control" "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control
)
_generate_msg_cpp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control
)

### Generating Services
_generate_srv_cpp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control
)

### Generating Module File
_generate_module_cpp(onrobot_vg_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(onrobot_vg_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(onrobot_vg_control_generate_messages onrobot_vg_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_cpp _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_cpp _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_cpp _onrobot_vg_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(onrobot_vg_control_gencpp)
add_dependencies(onrobot_vg_control_gencpp onrobot_vg_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS onrobot_vg_control_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control
)
_generate_msg_eus(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control
)

### Generating Services
_generate_srv_eus(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control
)

### Generating Module File
_generate_module_eus(onrobot_vg_control
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(onrobot_vg_control_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(onrobot_vg_control_generate_messages onrobot_vg_control_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_eus _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_eus _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_eus _onrobot_vg_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(onrobot_vg_control_geneus)
add_dependencies(onrobot_vg_control_geneus onrobot_vg_control_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS onrobot_vg_control_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control
)
_generate_msg_lisp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control
)

### Generating Services
_generate_srv_lisp(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control
)

### Generating Module File
_generate_module_lisp(onrobot_vg_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(onrobot_vg_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(onrobot_vg_control_generate_messages onrobot_vg_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_lisp _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_lisp _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_lisp _onrobot_vg_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(onrobot_vg_control_genlisp)
add_dependencies(onrobot_vg_control_genlisp onrobot_vg_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS onrobot_vg_control_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control
)
_generate_msg_nodejs(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control
)

### Generating Services
_generate_srv_nodejs(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control
)

### Generating Module File
_generate_module_nodejs(onrobot_vg_control
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(onrobot_vg_control_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(onrobot_vg_control_generate_messages onrobot_vg_control_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_nodejs _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_nodejs _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_nodejs _onrobot_vg_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(onrobot_vg_control_gennodejs)
add_dependencies(onrobot_vg_control_gennodejs onrobot_vg_control_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS onrobot_vg_control_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
)
_generate_msg_py(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
)

### Generating Services
_generate_srv_py(onrobot_vg_control
  "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
)

### Generating Module File
_generate_module_py(onrobot_vg_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(onrobot_vg_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(onrobot_vg_control_generate_messages onrobot_vg_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGInput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_py _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/msg/OnRobotVGOutput.msg" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_py _onrobot_vg_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abml/zoe_ws/src/UR/onrobot/onrobot_vg_control/srv/SetCommand.srv" NAME_WE)
add_dependencies(onrobot_vg_control_generate_messages_py _onrobot_vg_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(onrobot_vg_control_genpy)
add_dependencies(onrobot_vg_control_genpy onrobot_vg_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS onrobot_vg_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  string(REGEX REPLACE "([][+.*()^])" "\\\\\\1" ESCAPED_PATH "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control")
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/onrobot_vg_control
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${ESCAPED_PATH}/.+/__init__.pyc?$"
  )
endif()
