#!/usr/bin/env python

import rospy
import tf
import math

from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header

class AToMany:
    dangerous_obstacles = []

    def __init__(self):
        rospy.init_node("a_to_many", anonymous=True)
        rospy.Subscriber("/base_pose_ground_truth", Odometry, self.odometry_callback)
        rospy.Subscriber("/base_scan", LaserScan, self.laser_scanner_callback)

        self.rate = rospy.Rate(5)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.tf_listener = tf.TransformListener()

    def odometry_callback(self, odometry_data):
        self.pose = odometry_data.pose.pose

    def laser_scanner_callback(self, laser_scan):
        current_angle = laser_scan.angle_min
        for laser_range in laser_scan.ranges:
            if laser_range < laser_scan.range_max:
                if not hasattr(self, "pose"):
                    return False

                obstacle = self.convert_laser_range_to_point(laser_range, current_angle)

                if self.euclidean_distance(obstacle.point) < 0.5:
                    self.dangerous_obstacles.append(self.convert_to_frame("/odom", obstacle))
            current_angle += laser_scan.angle_increment;

    def convert_laser_range_to_point(self, laser_range, current_angle):
        x = laser_range*math.cos(current_angle)
        y = laser_range*math.sin(current_angle)
        return PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/base_link"), point=Point(x, y, 0))

    def euclidean_distance(self, a, b=Point(0,0,0)):
        return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

    def angular_velocity(self, local_frame_goal):
        return math.atan2(local_frame_goal.y, local_frame_goal.x)

    def convert_to_frame(self, frame, stamped_point):
        try:
            self.tf_listener.waitForTransform(frame, stamped_point.header.frame_id, rospy.Time(), rospy.Duration(4))
            return self.tf_listener.transformPoint(frame, stamped_point)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            return False

    def check_if_safe(self):
        if len(self.dangerous_obstacles) > 0:
            closest_obstacle = min(self.dangerous_obstacles, key=lambda x: self.euclidean_distance(x.point))
            error_message = f"Obstacle at: {closest_obstacle.point.x}, {closest_obstacle.point.y}"
            rospy.logerr(error_message)
            rospy.signal_shutdown(error_message)
            return False
        else:
            return True

    def go_to(self, destination):
        local_frame_goal = self.convert_to_frame("/base_link", destination).point

        while self.euclidean_distance(local_frame_goal) > 0.05:
            self.check_if_safe()

            local_frame_goal = self.convert_to_frame("/base_link", destination)

            if not local_frame_goal:
                continue

            local_frame_goal = local_frame_goal.point


            vel_msg = Twist()
            vel_msg.linear.x = self.euclidean_distance(local_frame_goal)
            vel_msg.angular.z = self.angular_velocity(local_frame_goal)
            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

    def go_to_many(self, destinations):
        destinations.sort(key=lambda x: self.euclidean_distance(self.convert_to_frame("/base_link", x).point))
        for destination in destinations:
            self.go_to(destination)
            rospy.loginfo(f"Made it to {destination.point.x}, {destination.point.y}")

if __name__ == "__main__":
    try:
        robot = AToMany()
        x_y_points = [[14.49, 21.47], [20.33, 36.43], [20.95, 25.91], [27.15, 29.86]]
        stamped_points = [PointStamped(header=Header(stamp=rospy.Time(),frame_id="/odom"), point=Point(point[0], point[1], 0)) for point in x_y_points]
        robot.go_to_many(stamped_points)
    except rospy.ROSInterruptException:
        pass
