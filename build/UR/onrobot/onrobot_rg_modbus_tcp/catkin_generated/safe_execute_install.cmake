execute_process(COMMAND "/home/abml/zoe_ws/build/UR/onrobot/onrobot_rg_modbus_tcp/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/abml/zoe_ws/build/UR/onrobot/onrobot_rg_modbus_tcp/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
