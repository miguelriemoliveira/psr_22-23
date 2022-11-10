#!/usr/bin/env python3

import argparse

import rospy
from std_msgs.msg import String


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--topic', type=str, required=False, default='chatter')
    parser.add_argument('-m', '--msg', type=str, required=False, default='Hello world!')
    parser.add_argument('-f', '--frequency', type=int, required=False, default=1)

    args = vars(parser.parse_args())

    # Initialization of a ros node
    rospy.init_node('publisher', anonymous=True)

    # Create the publisher
    publisher = rospy.Publisher(args['topic'], String, queue_size=10)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rate = rospy.Rate(args['frequency']) 

    while not rospy.is_shutdown():
        msg = args['msg'] + ' ' + str(rospy.get_time())

        rospy.loginfo('Publishing ' + msg)
        publisher.publish(msg)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()