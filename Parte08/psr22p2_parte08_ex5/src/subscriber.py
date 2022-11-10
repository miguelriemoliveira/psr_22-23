#!/usr/bin/env python3
import argparse
import math

import rospy
from psr22p2_parte08_ex5.msg import Dog
from std_msgs.msg import String
from colorama import Fore, Style


def msgReceivedCallback(msg):

    # Get the highlight text color global parameter
    highlight_text_color = rospy.get_param("/highlight_text_color")

    print('Starting to compute stupid stuff')
    for i in range(0, 10000):
        _ = math.sqrt(i)
    print('Finished computing stupid stuff')

    rospy.loginfo("I received " + getattr(Fore, highlight_text_color) + str(msg) + Style.RESET_ALL)
    
def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('subscriber', anonymous=True)

    # Init the subscriber
    subscriber = rospy.Subscriber('chatter', Dog, msgReceivedCallback)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()