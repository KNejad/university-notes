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

    def __init__(self):
        rospy.init_node("follow_wall", anonymous=True)

        rospy.Subscriber("/base_scan", LaserScan, self.laser_scanner_callback)

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.tf_listener = tf.TransformListener()

        self.obstacle_positions = { "left": math.inf, "ahead": math.inf, "all": math.inf }

        self.rate = rospy.Rate(5)

    def laser_scanner_callback(self, laser_scan):
        new_positions = { "left": math.inf, "ahead": math.inf, "all": math.inf }
        current_angle = laser_scan.angle_min
        for laser_range in laser_scan.ranges:
            if laser_scan.range_min < laser_range < laser_scan.range_max:
                obstacle = self.convert_laser_range_to_point(laser_range, current_angle)
                obstacle_distance = self.euclidean_distance(obstacle.point)

                new_positions["all"] = min(new_positions["all"], obstacle_distance)

                if -0.5 < current_angle < 0.5:
                    new_positions["ahead"] = min(new_positions["ahead"], obstacle_distance)

                if 1 < current_angle < 1.5:
                    new_positions["left"] = min(new_positions["left"], obstacle_distance)

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
        while self.obstacle_positions["all"] > 3:
            vel_msg = Twist()
            vel_msg.linear.x = 1
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

    def follow_wall(self):
        while True:
            vel_msg = Twist()
            vel_msg.linear.x = self.obstacle_positions["all"]

            if self.obstacle_positions["left"] < 1.5:
                vel_msg.angular.z = 0
            else:
                vel_msg.angular.z = 0.5

            if self.obstacle_positions["ahead"] < 1.5:
                # Turn right
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
