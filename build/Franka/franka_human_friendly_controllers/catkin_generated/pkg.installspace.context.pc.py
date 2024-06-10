# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/home/abml/libfranka/include".split(';') if "${prefix}/include;/home/abml/libfranka/include" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;dynamic_reconfigure;eigen_conversions;franka_hw;franka_gripper;geometry_msgs;hardware_interface;tf;tf_conversions;message_runtime;pluginlib;realtime_tools;roscpp".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lfranka_human_friendly_controllers;/home/abml/libfranka/build/libfranka.so.0.9.2".split(';') if "-lfranka_human_friendly_controllers;/home/abml/libfranka/build/libfranka.so.0.9.2" != "" else []
PROJECT_NAME = "franka_human_friendly_controllers"
PROJECT_SPACE_DIR = "/home/abml/zoe_ws/install"
PROJECT_VERSION = "0.8.1"
