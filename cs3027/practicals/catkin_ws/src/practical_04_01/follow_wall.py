#!/usr/bin/env python

import rospy
import tf
import math

from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header


class FollowWall:
    obstacle_positions = { "right": True, "ahead": True }

    def __init__(self):
        rospy.init_node("follow_wall", anonymous=True)

        rospy.Subscriber("/base_scan", LaserScan, self.laser_scanner_callback)

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.tf_listener = tf.TransformListener()

        self.rate = rospy.Rate(5)

    def laser_scanner_callback(self, laser_scan):
        new_positions = { "right": False, "ahead": False }
        current_angle = laser_scan.angle_min
        for laser_range in laser_scan.ranges:
            if laser_scan.range_min < laser_range < laser_scan.range_max:
                obstacle = self.convert_laser_range_to_point(laser_range, current_angle)

                if  0 < obstacle.point.x < 2 and 0.5 < obstacle.point.y < 1:
                    new_positions["ahead"] = True

                if  obstacle.point.y < 2:
                    new_positions["right"] = True

            current_angle += laser_scan.angle_increment;

        self.obstacle_positions = new_positions

    def convert_laser_range_to_point(self, laser_range, current_angle):
        x = laser_range*math.cos(current_angle)
        y = laser_range*math.sin(current_angle)
        return PointStamped(
                header=Header(stamp=rospy.Time.now(), frame_id="/base_link"),
                point=Point(x, y, 0))

    def euclidean_distance(self, a, b=Point(0,0,0)):
        return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

    def forward_till_wall(self):
        while not self.obstacle_positions["ahead"]:
            vel_msg = Twist()
            vel_msg.linear.x = 1
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

    def follow_wall(self):
        while True:
            vel_msg = Twist()

            if self.obstacle_positions["right"]:
                # Go forwards
                vel_msg.linear.x = 1
                vel_msg.angular.z = 0
            else:
                # Turn right and forwards
                vel_msg.linear.x = 1
                vel_msg.angular.z = 0.5

            if self.obstacle_positions["ahead"]:
                # Turn left
                vel_msg.linear.x = 0
                vel_msg.angular.z = -1


            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


if __name__ == "__main__":
    try:
        robot = FollowWall()
        robot.forward_till_wall()
        robot.follow_wall()
    except rospy.ROSInterruptException:
        pass
