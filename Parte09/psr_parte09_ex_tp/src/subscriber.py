#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_parte09_ex_tp.msg import Dog


def callbackMsgReceived(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter', Dog, callbackMsgReceived) # configure the subscriber
    pub = rospy.Publisher('chatter', Dog, queue_size=10) # configure the publisher

    # create a dog message to send
    dog = Dog()
    dog.name = 'dog3'
    dog.age = 1
    dog.color = 'black'

    rate = rospy.Rate(2)  # 1hz
    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        pub.publish(dog)
        rate.sleep()


if __name__ == '__main__':
    main()
