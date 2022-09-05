#!/usr/bin/env python3
import copy
import math
import random

import numpy as np
from matplotlib import cm
import rospy
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Point, Pose, Vector3, Quaternion
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from visualization_msgs.msg import Marker, MarkerArray

publisher = rospy.Publisher('/clusters', MarkerArray, queue_size=10)


def callbackMessageReceived(msg):
    rospy.loginfo('Received laser scan message')

    # The goal is to create a marker array, in which each marker (insider the markaer array) is a cluster
    marker_array = MarkerArray()

    marker = Marker(header=Header(frame_id='left_laser', stamp=rospy.Time.now()),
                    ns='sphere', id=0, action=Marker.ADD, type=Marker.SPHERE_LIST,
                    pose=Pose(position=Point(x=0, y=0, z=0), orientation=Quaternion(x=0, y=0, z=0, w=1)),
                    scale=Vector3(x=0.2, y=0.2, z=0.2),
                    color=ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.5))
    marker_array.markers.append(copy.copy(marker))

    print(len(msg.ranges))
    threshold_distance = 0.5
    range_prev = 1000000
    for idx, range in enumerate(msg.ranges):

        if range < 0.5:  # skip invalid measurements
            continue

        theta = msg.angle_min + msg.angle_increment * idx
        x = range * math.cos(theta)
        y = range * math.sin(theta)

        distance = range - range_prev
        range_prev = range

        if distance > threshold_distance:  # I will change to a new cluster
            id = len(marker_array.markers)
            marker = Marker(header=Header(frame_id='left_laser', stamp=rospy.Time.now()),
                            ns='sphere', id=id, action=Marker.ADD, type=Marker.SPHERE_LIST,
                            pose=Pose(position=Point(x=0, y=0, z=0), orientation=Quaternion(x=0, y=0, z=0, w=1)),
                            scale=Vector3(x=0.2, y=0.2, z=0.2),
                            color=ColorRGBA(r=random.random(), g=random.random(), b=random.random(), a=0.5))
            # marker.lifetime = rospy.Duration(3)
            rospy.loginfo('Created a new cluster')
            marker_array.markers.append(copy.copy(marker))

        last_marker = marker_array.markers[-1]
        last_marker.points.append(Point(x=x, y=y, z=0))

    marker_array.markers.append(marker)

    # Give color to clusters based on the number of points
    # colormap = cm.tab20(range(0, 20))
    colormap = cm.tab20(np.linspace(0, 1, 20))

    clusters = []
    for idx, marker in enumerate(marker_array.markers):
        clusters.append((idx, len(marker.points)))

    clusters_sorted = sorted(clusters, key=lambda tup: tup[1], reverse=True)
    print('clusters_sorted =\n' + str(clusters_sorted))

    idx_color = 0
    for idx, num_points in clusters_sorted:

        if idx_color > 19:
            marker_array.markers[idx].color.r = 0
            marker_array.markers[idx].color.g = 0
            marker_array.markers[idx].color.b = 0
        else:
            marker_array.markers[idx].color.r = colormap[idx_color, 0]
            marker_array.markers[idx].color.g = colormap[idx_color, 1]
            marker_array.markers[idx].color.b = colormap[idx_color, 2]
            idx_color += 1

    # convert from polar coordinates to cartesian and fill the point cloud

    publisher.publish(marker_array)


def main():
    rospy.init_node('ex8', anonymous=False)

    rospy.Subscriber('/left_laser/laserscan', LaserScan, callbackMessageReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
