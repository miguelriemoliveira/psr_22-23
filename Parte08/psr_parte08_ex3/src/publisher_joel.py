#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--message', type=str,
                        default='Do not know what to say ',
                        help='print stuff to the screen or not.')
    parser.add_argument('--rate', type=float,default=1)
    parser.add_argument('--topic', type=str, default='chatter')
    args = vars(parser.parse_args())

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher(args['topic'], String, queue_size=10)
    rate = rospy.Rate(args['rate'])  # 10hz

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        text_to_send = args['message'] + str(rospy.get_time())
        rospy.loginfo(text_to_send)
        pub.publish(text_to_send)

        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
