#!/usr/bin/env python

import rospy

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

rospy.init_node("add_marker", anonymous=True)
pub = rospy.Publisher("/marker_maker", MarkerArray, queue_size=200)
rate = rospy.Rate(5)


markers = ["blue", "brown"]

def add(x,y,r,g,b,frame, id_name):
    mr=Marker()
    mr.header.frame_id=frame
    mr.ns="basic"
    mr.type=mr.SPHERE
    mr.id=markers.index(id_name)
    mr.action=mr.ADD
    mr.pose.position.x=x
    mr.pose.position.y=y
    mr.pose.orientation.w=1
    mr.scale.x=1.5
    mr.scale.y=1.5
    mr.scale.z=1.5
    mr.color.r=r
    mr.color.g=g
    mr.color.b=b
    mr.color.a=1.0

    ma=MarkerArray()
    ma.markers.append(mr)
    pub.publish(ma)


while not rospy.is_shutdown():
    add(1,1,0.1,0.6,0.9,"/base_link","blue")
    add(4,4,0.4,0.2,0.1,"/base_link","brown")
    rate.sleep()
