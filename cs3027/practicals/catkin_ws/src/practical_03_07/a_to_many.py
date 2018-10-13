#!/usr/bin/env python

import rospy
import tf
import math

from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point

class AToMany:
    def __init__(self):
        rospy.init_node("a_to_b", anonymous=True)
        self.rate = rospy.Rate(10)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.tf_listener = tf.TransformListener()

    def euclidean_distance(self, local_frame_goal):
        return math.sqrt(pow(local_frame_goal.x, 2) + pow(local_frame_goal.y, 2))

    def angular_velocity(self, local_frame_goal):
        return math.atan2(local_frame_goal.y, local_frame_goal.x)

    def convert_to_local_frame(self, stamped_point):
        self.tf_listener.waitForTransform("/base_link", stamped_point.header.frame_id, rospy.Time(), rospy.Duration(4))
        return self.tf_listener.transformPoint("/base_link", stamped_point)

    def go_to(self, destination):
        local_frame_goal = self.convert_to_local_frame(destination).point
        while self.euclidean_distance(local_frame_goal) > 0.05:
            local_frame_goal = self.convert_to_local_frame(destination).point

            vel_msg = Twist()
            vel_msg.linear.x = self.euclidean_distance(local_frame_goal)
            vel_msg.angular.z = self.angular_velocity(local_frame_goal)
            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

    def go_to_many(self, destinations):
        destinations.sort(key=lambda x: self.euclidean_distance(self.convert_to_local_frame(x).point))
        for destination in destinations:
            self.go_to(destination)
            rospy.loginfo(f"Made it to {destination.point.x}, {destination.point.y}")

if __name__ == "__main__":
    try:
        robot = AToMany()
        x_y_points = [[14.49, 21.47], [20.33, 36.43], [20.95, 25.91], [27.15, 29.86]]
        stamped_points = [PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/odom"), point=Point(point[0], point[1], 0)) for point in x_y_points]
        robot.go_to_many(stamped_points)
    except rospy.ROSInterruptException:
        pass
