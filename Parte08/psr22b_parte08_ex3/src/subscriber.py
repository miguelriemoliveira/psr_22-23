#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String


def msgReceivedCallback(msg):
    rospy.loginfo("I received " + str(msg.data))
    
def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--topic', type=str, required=False, default='chatter')
    args = vars(parser.parse_args())


    # Initialization of a ros node
    rospy.init_node('subscriber', anonymous=True)

    # Init the subscriber
    rospy.Subscriber(args['topic'], String, msgReceivedCallback)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()