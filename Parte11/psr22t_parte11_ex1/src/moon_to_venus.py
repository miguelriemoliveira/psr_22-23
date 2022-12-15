#!/usr/bin/env python3
import math

import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import tf
import turtlesim.srv


def main():
    rospy.init_node('listener_moon_to_venus')

    listener = tf.TransformListener()

   
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('moon', 'venus', rospy.Time(0))
            # (trans,rot) = listener.lookupTransform('moon', 'venus', rospy.Time.now())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print('Could not get get the transformation')
            continue

        distance = math.sqrt(trans[0]**2 + trans[1]**2)
        print('Distance from moon to venus is ' + str(distance))

        rate.sleep()

if __name__ == '__main__':
    main()