#!/usr/bin/env python3
import argparse

import rospy
from psr22p1_parte08_ex5.msg import Dog
from std_msgs.msg import String
from colorama import Fore, Style


def msgReceivedCallback(msg):

    color = rospy.get_param("/color")
    rospy.loginfo("I received " +  getattr(Fore, color) + str(msg) + Style.RESET_ALL)
    
def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    # Initialization of a ros node
    rospy.init_node('subscriber', anonymous=True)

    # Init the subscriber
    rospy.Subscriber('chatter', Dog, msgReceivedCallback)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()