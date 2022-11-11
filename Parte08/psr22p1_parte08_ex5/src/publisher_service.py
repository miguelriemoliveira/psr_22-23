#!/usr/bin/env python3

import argparse
from functools import partial

import rospy
from std_msgs.msg import String
from psr22p1_parte08_ex5.msg import Dog
from psr22p1_parte08_ex5.srv import SetDogName, SetDogNameResponse
from colorama import Fore, Style


def serviceRequestCallback(request, dog):
    print('Received request for set dog name to ' + request.new_name)

    # Change the dog's name
    dog.name = request.new_name

    # Respond to the service
    response = SetDogNameResponse()
    response.result = 0
    return response

def main():
    # ------------------------------------
    # Initialization 
    # ------------------------------------
    dog = Dog() # instantiating the dog class
    dog.name = 'Dalila'
    dog.color = 'brown'
    dog.age = 5
    dog.brothers.append('Zeus')
    dog.brothers.append('Rex')
    
    # Initialization of a ros node
    rospy.init_node('publisher', anonymous=True)

    # Create the publisher
    publisher = rospy.Publisher('chatter', Dog, queue_size=10)

    # Create teh service
    service = rospy.Service('set_dog_name', SetDogName, partial(serviceRequestCallback, dog=dog))


    # ------------------------------------
    # Execution 
    # ------------------------------------
    frequency = rospy.get_param('~frequency', 1)
    rate = rospy.Rate(frequency) 

    while not rospy.is_shutdown():
        # Get the color for printing
        color = rospy.get_param("/color", 'RED')

        rospy.loginfo('Publishing ' + getattr(Fore, color) + str(dog) + Style.RESET_ALL)
        publisher.publish(dog)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()