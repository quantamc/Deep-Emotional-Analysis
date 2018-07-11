#!/usr/bin/env python

#Ros imports
import roslib
import rospy

from static_bot_control.msg import EmoMSG
from std_msgs.msg import Header
from std_msgs.msg import UInt32

# Sensor channels.
channels = [
    'F3',
    'FC6',
    'P7',
    'T8',
    'F7',
    'F8',
    'T7',
    'P8',
    'AF4',
    'F4',
    'AF3',
    'O2',
    'O1',
    'FC5',
    'X',
    'Y'
]

def epoc_publish_channels():
    
