#!/usr/bin/env python3
import argparse

import rospy
from psr22_parte08_ex4.msg import Dog
from std_msgs.msg import String


def msgReceivedCallback(msg):
    rospy.loginfo("I received\n" + str(msg) + '\n')
    
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
    rospy.Subscriber(args['topic'], Dog, msgReceivedCallback)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()