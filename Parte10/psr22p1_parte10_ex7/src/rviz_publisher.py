#!/usr/bin/env python3


import cv2
import rospy
from cv_bridge import CvBridge
from visualization_msgs.msg import Marker


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('rviz_publisher', anonymous=False)

    # Create the publisher
    publisher = rospy.Publisher('~markers', Marker, queue_size=1)

    # ------------------------------------
    # Execution 
    # ------------------------------------

    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():

        # Create a Sphere marker
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 0
        marker.type = Marker.SPHERE
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0

        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 1
        marker.pose.orientation.w = 0

        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 3

        marker.color.r = 0
        marker.color.g = 1
        marker.color.b = 0
        marker.color.a = 0.3

        marker.text = 'Not used'
        publisher.publish(marker)
        
        # Create a Cube marker
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 1
        marker.type = Marker.CUBE
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0

        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 1
        marker.pose.orientation.w = 0

        marker.scale.x = 0.3
        marker.scale.y = 0.3
        marker.scale.z = 0.3

        marker.color.r = 1
        marker.color.g = 0
        marker.color.b = 0
        marker.color.a = 1

        marker.text = 'Not used'
        publisher.publish(marker)
        
        # Create a text marker
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.ns = 'my_drawings'
        marker.id = 2
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.MODIFY

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 2

        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 1
        marker.pose.orientation.w = 0

        marker.scale.x = 0.3
        marker.scale.y = 0.3
        marker.scale.z = 0.3

        marker.color.r = 1
        marker.color.g = 0
        marker.color.b = 1
        marker.color.a = 1

        marker.text = 'Arrival'

        # Publish the marker
        publisher.publish(marker)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()