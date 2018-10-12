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



    def turn_towards_goal(self):
        vel_msg = Twist()
        turn_amount = math.atan2(self.destination_in_local_frame.point.y, self.destination_in_local_frame.point.x)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = turn_amount

        return vel_msg

    def robot_is_pointing_towards_goal(self):
        turn_amount = math.atan2(self.destination_in_local_frame.point.y, self.destination_in_local_frame.point.x)
        if abs(turn_amount) < 0.05:
            return True
        else:
            return False

    def go_to(self, destination):
        rate = rospy.Rate(5)

        listener = tf.TransformListener()


        while self.euclidean_distance(destination.point) > 0.05:
            vel_msg = Twist()

            try:
                self.destination_in_local_frame = listener.transformPoint("/base_link", destination)
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue

            if not self.robot_is_pointing_towards_goal():
                vel_msg = self.turn_towards_goal()

            vel_msg.linear.x = self.euclidean_distance(destination.point) * 1.5

            self.velocity_publisher.publish(vel_msg)

            rate.sleep()

if __name__ == "__main__":
    robot = AToB()

    destination = PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/odom"), point=Point(-12.9481, 22.9615,0.0))
    robot.go_to(destination)
