#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/abml/zoe_ws/src/franka_ros_interface/franka_tools"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/abml/zoe_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/abml/zoe_ws/install/lib/python3/dist-packages:/home/abml/zoe_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/abml/zoe_ws/build" \
    "/usr/bin/python3" \
    "/home/abml/zoe_ws/src/franka_ros_interface/franka_tools/setup.py" \
     \
    build --build-base "/home/abml/zoe_ws/build/franka_ros_interface/franka_tools" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/abml/zoe_ws/install" --install-scripts="/home/abml/zoe_ws/install/bin"
