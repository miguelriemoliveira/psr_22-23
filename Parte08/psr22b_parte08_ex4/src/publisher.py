#!/usr/bin/env python3

import argparse

import rospy
from std_msgs.msg import String
from psr22_parte08_ex4.msg import Dog


def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--topic', type=str, required=False, default='chatter')
    parser.add_argument('-m', '--msg', type=str, required=False, default='Hello world!')
    parser.add_argument('-f', '--frequency', type=int, required=False, default=1)

    args = vars(parser.parse_args())

    dog = Dog() # instantiating the dog class
    dog.name = 'Dalila'
    dog.color = 'brown'
    dog.age = 5
    dog.brothers.append('Zeus')
    dog.brothers.append('Rex')
    
    # Initialization of a ros node
    rospy.init_node('publisher', anonymous=True)

    # Create the publisher
    publisher = rospy.Publisher(args['topic'], Dog, queue_size=10)

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rate = rospy.Rate(args['frequency']) 

    while not rospy.is_shutdown():

        rospy.loginfo('Publishing ' + str(dog))
        publisher.publish(dog)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()