#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_parte08_ex3.msg import Dog


def callbackMsgReceived(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--topic', type=str, default='chatter')
    args = vars(parser.parse_args())

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(args['topic'], Dog, callbackMsgReceived)

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    main()
