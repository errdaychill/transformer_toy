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

echo_and_run cd "/home/dayclear94/move_turtlebot/src/audio_common/sound_play"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/dayclear94/move_turtlebot/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/dayclear94/move_turtlebot/install/lib/python2.7/dist-packages:/home/dayclear94/move_turtlebot/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/dayclear94/move_turtlebot/build" \
    "/usr/bin/python2" \
    "/home/dayclear94/move_turtlebot/src/audio_common/sound_play/setup.py" \
    build --build-base "/home/dayclear94/move_turtlebot/build/audio_common/sound_play" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/dayclear94/move_turtlebot/install" --install-scripts="/home/dayclear94/move_turtlebot/install/bin"
