#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def parrot():
    rospy.init_node('parrot', anonymous=True)
    rospy.loginfo(rospy.get_param("parrot_phrase"))
    rospy.spin()

if __name__ == '__main__':
    parrot()
