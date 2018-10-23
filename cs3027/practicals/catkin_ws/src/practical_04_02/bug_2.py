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

class Bug2:
    obstacles = { "left": False, "ahead": False, "all": False }
    following_wall = False
    origin_point = False

    def __init__(self):
        rospy.init_node("follow_wall", anonymous=True)

        rospy.Subscriber("/base_scan", LaserScan, self.laser_scanner_callback)
        rospy.Subscriber("/base_pose_ground_truth", Odometry, self.odometry_callback)

        self.tf_listener = tf.TransformListener()

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.rate = rospy.Rate(5)

    def laser_scanner_callback(self, laser_scan):
        new_distances = { "left": math.inf, "ahead": math.inf, "all": math.inf }
        new_obstacles = { "left": False, "ahead": False, "all": False }
        current_angle = laser_scan.angle_min

        for laser_range in laser_scan.ranges:
            if laser_scan.range_min < laser_range < laser_scan.range_max:
                obstacle = convert_laser_range_to_point(laser_range, current_angle)
                obstacle_distance = euclidean_distance(obstacle)

                if  obstacle_distance < new_distances["all"]:
                    new_obstacles["all"] = obstacle
                    new_distances["all"] = obstacle_distance

                if -0.5 < current_angle < 0.5 and obstacle_distance < new_distances["ahead"]:
                    new_obstacles["ahead"] = obstacle
                    new_distances["ahead"] = obstacle_distance

                if 1 < current_angle < 1.5 and obstacle_distance < new_distances["left"]:
                    new_obstacles["left"] = obstacle
                    new_distances["left"] = obstacle_distance

            current_angle += laser_scan.angle_increment;

        self.obstacles = new_obstacles

    def odometry_callback(self, odometry_data):
        self.pose = odometry_data.pose.pose

        if self.origin_point == False:
            self.origin_point = self.pose.position

    def follow_wall_vel(self):
        if not self.following_wall:
            self.wall_following_starting_position = self.pose.position

        vel_msg = Twist()
        vel_msg.linear.x = euclidean_distance(self.obstacles["all"])
        vel_msg.angular.z = euclidean_distance(self.obstacles["left"]) - 1

        # If there is an obstacle, stop and turn right
        if euclidean_distance(self.obstacles["ahead"]) < 1:
            vel_msg.linear.x = 0
            vel_msg.angular.z = -1

        self.following_wall = self.should_still_follow_wall()

        return vel_msg

    def should_still_follow_wall(self):
        return ((not is_on_line_towards_point(self.origin_point, self.destination.point, self.pose.position)) and
                euclidean_distance(self.wall_following_starting_position) > 5)


    def go_to(self, destination):
        self.destination = destination

        local_frame_goal = self.convert_to_frame("/base_link", destination)

        while local_frame_goal == False or euclidean_distance(local_frame_goal) > 0.05:
            local_frame_goal = self.convert_to_frame("/base_link", destination)

            if not local_frame_goal:
                continue

            vel_msg = Twist()

            if self.following_wall or euclidean_distance(self.obstacles["ahead"]) < 1:
                vel_msg = self.follow_wall_vel()
            else:
                local_frame_goal = local_frame_goal.point
                vel_msg.linear.x = euclidean_distance(local_frame_goal)
                vel_msg.angular.z = angular_velocity(local_frame_goal)

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

    def convert_to_frame(self, frame, stamped_point):
        try:
            self.tf_listener.waitForTransform(frame, stamped_point.header.frame_id, rospy.Time(), rospy.Duration(4))
            return self.tf_listener.transformPoint(frame, stamped_point)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            return False

def euclidean_distance(a, b=Point(0,0,0)):
    if a == False or b == False:
        return math.inf

    if type(a).__name__ == "PointStamped":
        a = a.point

    return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

def convert_laser_range_to_point(laser_range, current_angle):
    x = laser_range*math.cos(current_angle)
    y = laser_range*math.sin(current_angle)
    return PointStamped(
            header=Header(stamp=rospy.Time.now(), frame_id="/base_link"),
            point=Point(x, y, 0))

def angular_velocity(local_frame_goal):
    return math.atan2(local_frame_goal.y, local_frame_goal.x)

def is_on_line_towards_point(line_point_1, line_point_2, position):
    dxc = position.x - line_point_1.x
    dyc = position.y - line_point_1.y

    dxl = line_point_2.x - line_point_1.x
    dyl = line_point_2.y - line_point_1.y

    cross = dxc * dyl - dyc * dxl
    if cross < 5:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        robot = Bug2()
        destination = PointStamped(header=Header(stamp=rospy.Time.now(),frame_id="/odom"), point=Point(5, 5, 0.0))
        robot.go_to(destination)
    except rospy.ROSInterruptException:
        pass
