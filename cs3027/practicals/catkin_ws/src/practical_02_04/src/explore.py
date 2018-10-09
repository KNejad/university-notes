#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

from laser_scanner import LaserScanner

def explore():
    rospy.init_node('explore', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    scanner = LaserScanner()
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        tw=Twist()

        if scanner.safe:
            tw.linear.x=1
            tw.angular.z=0
        else:
            tw.linear.x=0
            tw.angular.z=1

        pub.publish(tw)
        rate.sleep()

if __name__ == '__main__':
    explore()
