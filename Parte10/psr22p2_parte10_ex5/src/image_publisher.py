#!/usr/bin/env python3


import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('image_publisher', anonymous=False)

    # Create the publisher
    publisher = rospy.Publisher('~image', Image, queue_size=1)

    bridge = CvBridge()
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    # ------------------------------------
    # Execution 
    # ------------------------------------

    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        _, image_opencv = capture.read()  # get an image from the camera

        cv2.imshow(window_name, image_opencv)
        cv2.waitKey(30)

        # convert from image opencv to image ros msg
        image_msg = bridge.cv2_to_imgmsg(image_opencv, encoding="passthrough")

        publisher.publish(image_msg)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()