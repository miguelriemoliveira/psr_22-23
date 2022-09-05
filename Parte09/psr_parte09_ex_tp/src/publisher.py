#!/usr/bin/env python3
import argparse

import colorama
import rospy
from std_msgs.msg import String
from psr_parte09_ex_tp.msg import Dog


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)

    # read private parameter

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        # read global parameter
        highlight_text_color = rospy.get_param("/highlight_text_color")

        # create a dog message to sent
        dog = Dog()
        dog.name = 'max'
        dog.age = 18
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('boby')

        rospy.loginfo('Publishing dog message with name ' +
                      getattr(colorama.Fore, highlight_text_color) +
                      str(dog.name) + colorama.Style.RESET_ALL)
        pub.publish(dog)

        frequency = rospy.get_param("~frequency", default=1)
        rate = rospy.Rate(frequency)  # 1hz
        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
