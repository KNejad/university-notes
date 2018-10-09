#!/usr/bin/env python

import rospy
import numpy

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class LaserScanner:
    safe = False

    def __init__(self):
        rospy.Subscriber('/base_scan', LaserScan, self.callback)

    def callback(self, laser_scan):
        self.safe = self.determine_if_safe(laser_scan)

    def determine_if_safe(self, laser_scan):
        current_angle = laser_scan.angle_min
        increment = laser_scan.angle_increment
        for laser_range in laser_scan.ranges:
            x = laser_range*numpy.cos(current_angle);
            y = laser_range*numpy.sin(current_angle);
            current_angle += increment;

            robot_width = 0.35 #rospy.get_param("/robot_width")
            danger_zone_padding = 0.2

            if (abs(y) < robot_width/2 + danger_zone_padding) and (x < (robot_width*1.42)/2 + danger_zone_padding):
                return False;

        return True;

