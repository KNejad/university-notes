#!/usr/bin/env python

import rospy

from nav_msgs.msg import OccupancyGrid

class MapListener:
    def __init__(self):
        rospy.init_node("map_listener", anonymous=True)

    def output_map(self):
        rospy.loginfo(rospy.wait_for_message("/map",OccupancyGrid,timeout=None))

if __name__ == "__main__":
    try:
        robot = MapListener()
        robot.output_map()
    except rospy.ROSInterruptException:
        pass
