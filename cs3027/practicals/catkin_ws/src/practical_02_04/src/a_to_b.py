#!/usr/bin/env python

import rospy
import tf
import math

from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from nav_msgs.msg import Odometry

from laser_scanner import LaserScanner

class AToB:
    def __init__(self):
        rospy.init_node("a_to_b", anonymous=True)
        rate = rospy.Rate(5)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.pose = Pose()
        rospy.Subscriber('/base_pose_ground_truth', Odometry, self.odometry_callback)

    def odometry_callback(self, odometry_info):
        self.pose = odometry_info.pose.pose

    def euclidean_distance(self, goal_point):
        current_point = self.pose.position

        return math.sqrt(pow(goal_point.x - current_point.x, 2) + pow(goal_point.y - current_point.y, 2))

    def angular_velocity(self, goal_point):
        current_point = self.pose.position
        co = self.pose.orientation
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([co.x,co.y,co.z,co.w])
        return math.atan2(goal_point.y - current_point.y, goal_point.x - current_point.x) - yaw

    def go_to(self, destination):
        rate = rospy.Rate(5)

        while self.euclidean_distance(destination.point) > 0.05:
            vel_msg = Twist()
            vel_msg.angular.z = self.angular_velocity(destination.point) * 2
            vel_msg.linear.x = self.euclidean_distance(destination.point) * 1.5

            self.velocity_publisher.publish(vel_msg)

            rate.sleep()

if __name__ == "__main__":
    robot = AToB()

    destination = PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/base_pose_ground_truth"), point=Point(-12.9481, 22.9615,0.0))
    robot.go_to(destination)
