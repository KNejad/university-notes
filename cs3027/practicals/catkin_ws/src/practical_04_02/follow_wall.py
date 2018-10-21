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

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class FollowWall:
    obstacles = { "left": False, "ahead": False, "all": False }
    markers= ["current_location"]

    def __init__(self):
        rospy.init_node("follow_wall", anonymous=True)

        rospy.Subscriber("/base_scan", LaserScan, self.laser_scanner_callback)
        rospy.Subscriber("/base_pose_ground_truth", Odometry, self.odometry_callback)

        self.tf_listener = tf.TransformListener()

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.marker_publisher = rospy.Publisher('/follow_wall_markers', MarkerArray, queue_size=10)

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
        pose = odometry_data.pose.pose
        self.add_marker(pose, 0.1,0.6,0.9, "/map","current_location")

    def forward_till_wall(self):
        while euclidean_distance(self.obstacles["all"]) > 1:
            vel_msg = Twist()
            vel_msg.linear.x = 1
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

    def follow_wall(self):
        while True:
            vel_msg = Twist()
            vel_msg.linear.x = euclidean_distance(self.obstacles["all"])
            vel_msg.angular.z = euclidean_distance(self.obstacles["left"]) - 1

            # If there is an obstacle, stop and turn right
            if euclidean_distance(self.obstacles["ahead"]) < 1:
                vel_msg.linear.x = 0
                vel_msg.angular.z = -1

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

    def add_marker(self, pose, r, g, b, frame, id_name):
        mr=Marker()
        mr.header.frame_id=frame
        mr.ns="basic"
        mr.type=mr.ARROW
        mr.id=self.markers.index(id_name)
        mr.action=mr.ADD
        mr.pose=pose
        mr.scale.x=0.6
        mr.scale.y=0.2
        mr.scale.z=0.2
        mr.color.r=r
        mr.color.g=g
        mr.color.b=b
        mr.color.a=1.0

        ma=MarkerArray()
        ma.markers.append(mr)
        self.marker_publisher.publish(ma)

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


if __name__ == "__main__":
    try:
        robot = FollowWall()
        robot.forward_till_wall()
        robot.follow_wall()
    except rospy.ROSInterruptException:
        pass
