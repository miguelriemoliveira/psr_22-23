#!/usr/bin/env python3

import argparse
import math
import random
from functools import partial

import rospy
from std_msgs.msg import String, ColorRGBA
from visualization_msgs.msg import Marker, MarkerArray
from colorama import Fore, Style


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    # Initialization of a ros node
    rospy.init_node('rviz_publisher', anonymous=False)

    # Create the publisher
    publisher = rospy.Publisher('~marker_array', MarkerArray, queue_size=10)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    angle = -1
    alpha = 0
    rate = rospy.Rate(10) 

    # define the initial color
    color = ColorRGBA()
    color.r = random.random() 
    color.g = random.random() 
    color.b = random.random() 
    color.a = 1
    color_tic = rospy.Time.now()

    while not rospy.is_shutdown():

        # create the marker array
        marker_array = MarkerArray()

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

        angle += 0.1
        if angle > 1:
            angle = -1

        marker.pose.orientation.x = angle
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 1 - angle**2

        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 4

        marker.color.r = 0.2
        marker.color.g = 0.2
        marker.color.b = 0.2
        marker.color.a = 0.3

        marker_array.markers.append(marker)

        # Step 2: Define the cube marker 
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 1
        marker.type = Marker.CUBE
        marker.action = Marker.MODIFY

        radius = 2
        alpha += 0.1
        # if alpha > 2*math.pi:
            # alpha = 0

        marker.pose.position.x = radius * math.cos(alpha)
        marker.pose.position.y = radius * math.sin(alpha)
        marker.pose.position.z = 0
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

        marker_array.markers.append(marker)

        # Step 3: Define the text marker 
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

        duration_to_change_color = 2
        duration = (rospy.Time.now() - color_tic).to_sec()
        if duration > duration_to_change_color:
            color.r = random.random() 
            color.g = random.random() 
            color.b = random.random() 
            color_tic = rospy.Time.now()

        marker.color = color
        marker.text = 'Hello from space'
        #geometry_msgs/Point[] points
        #std_msgs/ColorRGBA[] colors
        #string text

        marker_array.markers.append(marker)

        # publish the marker array 
        publisher.publish(marker_array)

        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()