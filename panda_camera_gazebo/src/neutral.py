#!/usr/bin/env python

import rospy
from franka_interface import ArmInterface


rospy.init_node('neutral_pose')

# https://justagist.github.io/franka_ros_interface/DOC.html#arminterface
panda = ArmInterface()
panda.move_to_neutral()
