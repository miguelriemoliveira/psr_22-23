#!/usr/bin/env python3

import argparse
from functools import partial

import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker
from colorama import Fore, Style


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    # Initialization of a ros node
    rospy.init_node('rviz_publisher', anonymous=False)

    # Create the publisher
    publisher = rospy.Publisher('~marker', Marker, queue_size=10)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():

        # Step 1: Define the sphere marker 
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 0
        marker.type = Marker.SPHERE
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 2
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 0

        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 4

        marker.color.r = 0.2
        marker.color.g = 0.2
        marker.color.b = 0.2
        marker.color.a = 0.3

        #geometry_msgs/Point[] points
        #std_msgs/ColorRGBA[] colors
        #string text

        publisher.publish(marker)

        # Step 2: Define the cube marker 
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 1
        marker.type = Marker.CUBE
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 2
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 0

        marker.scale.x = 0.3
        marker.scale.y = 0.3
        marker.scale.z = 0.3

        marker.color.r = 1
        marker.color.g = 0
        marker.color.b = 0
        marker.color.a = 1

        #geometry_msgs/Point[] points
        #std_msgs/ColorRGBA[] colors
        #string text

        publisher.publish(marker)

        # Step 3: Define the cube marker 
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 2
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 4
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 0

        marker.scale.z = 0.5

        marker.color.r = 1
        marker.color.g = 0
        marker.color.b = 1
        marker.color.a = 1

        marker.text = 'Hello from space'
        #geometry_msgs/Point[] points
        #std_msgs/ColorRGBA[] colors
        #string text

        publisher.publish(marker)

        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()