#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from psr_aula8_ex3_p3.msg import Dog


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('politics', Dog, queue_size=10)
    rate = rospy.Rate(1)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        dog = Dog()
        dog.name = 'boby'
        dog.age = 77
        dog.color = 'brown'
        dog.brothers.append('rosita')

        rospy.loginfo('Sending dog ...')  # same as print ... for now

        pub.publish(dog)  # finally, publish the message
        rate.sleep()

    # ------------------------------------------------
    # Termination
    # ------------------------------------------------


if __name__ == '__main__':
    main()
