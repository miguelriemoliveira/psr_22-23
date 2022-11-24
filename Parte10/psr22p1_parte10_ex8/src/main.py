#!/usr/bin/env python3
import argparse
import math
import random
from copy import deepcopy
from functools import partial

import rospy
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from std_msgs.msg import String, Header, ColorRGBA
from colorama import Fore, Style
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


def msgReceivedCallback(msg, publisher):

    rospy.loginfo("I received a new laser scan msg")

    threshold_r = 0.5
    clusters = []
    cluster_idxs = [0]
    clusters.append(cluster_idxs)

    # Clustering
    for idx in range(1, len(msg.ranges)):
        r_idx = msg.ranges[idx]
        r_idx_prev = msg.ranges[idx-1]

        if abs(r_idx - r_idx_prev) >  threshold_r:
            clusters.append([idx])
        else:
            clusters[-1].append(idx)

    # Create a Sphere marker
    marker = Marker()
    marker.header.frame_id = 'left_laser'
    marker.ns = 'clusters'
    marker.id = 0
    marker.type = Marker.CUBE_LIST
    marker.action = Marker.MODIFY

    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0

    marker.pose.orientation.x = 0
    marker.pose.orientation.y = 0
    marker.pose.orientation.z = 0
    marker.pose.orientation.w = 1

    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2

    marker.color.r = 0
    marker.color.g = 0
    marker.color.b = 1
    marker.color.a = 0.2


    prev_cluster = 0
    color = ColorRGBA()
    color.r = random.random()
    color.g = random.random()
    color.b = random.random()
    color.a = 0.3

    for idx in range(1, len(msg.ranges)):
        alpha = msg.angle_min + idx * msg.angle_increment
        r = msg.ranges[idx]

        point = Point()
        point.x = r * math.cos(alpha)
        point.y = r * math.sin(alpha)
        point.z = 0
        marker.points.append(point)

        # find the cluster to which this point belongs
        for cluster_idx, cluster in enumerate(clusters):
            if idx in cluster:
                current_cluster = cluster_idx
                print()
                break

        if prev_cluster != current_cluster: # change cluster, change color
            print(Fore.RED + 'idx = ' + str(idx) + ' New color!!!' + Style.RESET_ALL)
            color.r = random.random()
            color.g = random.random()
            color.b = random.random()
 
        prev_cluster = current_cluster # update to test on the next iteration

        marker.colors.append(deepcopy(color))

    publisher.publish(marker)

def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('lidar_subscriber', anonymous=False)

    publisher = rospy.Publisher('~clusters', Marker, queue_size=1)

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