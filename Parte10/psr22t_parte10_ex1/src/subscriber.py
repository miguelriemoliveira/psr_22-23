#!/usr/bin/env python3
import argparse
import math
from functools import partial

import rospy
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from std_msgs.msg import String, Header
from colorama import Fore, Style
from sensor_msgs import point_cloud2


def msgReceivedCallback(msg, publisher):

    rospy.loginfo("I received a new laser scan msg")

    # inspiration from https://gist.github.com/lucasw/ea04dcd65bc944daea07612314d114bb
    # sensor_msgs.msg PointCloud2 is the actual serialized message, but to manipulate we use the sensor_msgs
    # point_cloud2 data structure.
    header = Header(seq=msg.header.seq, stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)]

    # Create a list of xyz coords
    points = []
    for idx in range(0, len(msg.ranges)):
        alpha = msg.angle_min + idx * msg.angle_increment
        r = msg.ranges[idx]

        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        z = 0
        points.append([x,y,z])

    pc2 = point_cloud2.create_cloud(header, fields, points)  # create point_cloud2 data structure

    publisher.publish(pc2)


    
def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('lidar_subscriber', anonymous=False)

    publisher = rospy.Publisher('~point_cloud', PointCloud2, queue_size=1)

    # Init the subscriber
    subscriber = rospy.Subscriber('/left_laser/laserscan', LaserScan, partial(msgReceivedCallback, publisher=publisher))

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()