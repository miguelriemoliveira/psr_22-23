#!/usr/bin/env python3
import math

import rospy
from std_msgs.msg import Header, ColorRGBA
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3

def main():

    rospy.init_node('ex7', anonymous=True)
    pub = rospy.Publisher('drawings', MarkerArray, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    rotation_z = -1
    scale = 0.1
    while not rospy.is_shutdown():

        marker_array = MarkerArray()

        # Red cube
        marker = Marker(header=Header(frame_id='world', stamp=rospy.Time.now()),
                        ns='cube', id=0, action=Marker.ADD, type=Marker.CUBE,
                        pose=Pose(position=Point(x=0, y=0, z=0), orientation=Quaternion(x=0, y=0, z=rotation_z, w=1)),
                        scale=Vector3(x=0.4, y=0.4, z=0.4),
                        color=ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0))

        #1 = sqrt( z**2 + w**2)
        # 1**2 = z**2 + w**2
        # sqrt(1-z**2) = w

        w = math.sqrt(1- rotation_z**2)
        marker.pose.orientation.w = w

        # pub.publish(marker)
        marker_array.markers.append(marker)
        rotation_z +=0.01
        if rotation_z > 1:
            rotation_z=1


        # Green sphere
        marker = Marker(header=Header(frame_id='world', stamp=rospy.Time.now()),
                        ns='sphere', id=0, action=Marker.ADD, type=Marker.SPHERE,
                        pose=Pose(position=Point(x=1, y=0, z=0), orientation=Quaternion(x=0, y=0, z=0, w=1)),
                        scale=Vector3(x=scale, y=scale, z=scale),
                        color=ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3))

        marker_array.markers.append(marker)
        # pub.publish(marker)
        scale += 0.1
        if scale > 2:
            scale = 0.1

        # Text
        marker = Marker(header=Header(frame_id='world', stamp=rospy.Time.now()),
                        ns='sphere', id=1, action=Marker.ADD, type=Marker.TEXT_VIEW_FACING,
                        pose=Pose(position=Point(x=1, y=0, z=0), orientation=Quaternion(x=0, y=0, z=0, w=1)),
                        scale=Vector3(x=0.4, y=0.4, z=0.4),
                        color=ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3))
        marker.text = 'Já tou a escrever ...'

        marker_array.markers.append(marker)
        # pub.publish(marker)


        pub.publish(marker_array)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass