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

class AToB:
    yaw = 0
    pose = Pose()

    def __init__(self):
        rospy.init_node("a_to_b", anonymous=True)
        self.rate = rospy.Rate(10)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.Subscriber('/base_pose_ground_truth', Odometry, self.odometry_callback)

    def odometry_callback(self, odometry_info):
        self.pose = odometry_info.pose.pose

        co = self.pose.orientation
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([co.x,co.y,co.z,co.w])

        self.yaw = yaw

    def euclidean_distance(self, goal_point):
        current_point = self.pose.position
        return math.sqrt(pow(goal_point.x - current_point.x, 2) + pow(goal_point.y - current_point.y, 2))

    def angular_velocity(self, local_frame_goal):
        return math.atan2(local_frame_goal.point.y, local_frame_goal.point.x)

    def go_to(self, destination):
        tf_listener = tf.TransformListener()
        while self.euclidean_distance(destination.point) > 0.05:
            vel_msg = Twist()

            try:
                local_frame_goal = tf_listener.transformPoint("/base_link", destination)
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue

            vel_msg.linear.x = self.euclidean_distance(destination.point) * 1.5
            vel_msg.angular.z = self.angular_velocity(local_frame_goal) * 2

            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

if __name__ == "__main__":
    try:
        robot = AToB()
        destination = PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/odom"), point=Point(-12.9481, 22.9615,0.0))
        robot.go_to(destination)
    except rospy.ROSInterruptException:
        pass
