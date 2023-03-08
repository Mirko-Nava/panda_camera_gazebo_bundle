#!/bin/sh

rosrun xacro xacro panda_arm_camera.urdf.xacro -o panda_arm_camera.urdf
check_urdf panda_arm_camera.urdf
