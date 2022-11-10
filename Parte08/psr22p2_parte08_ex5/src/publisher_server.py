#!/usr/bin/env python3

import argparse
from functools import partial

import rospy
from std_msgs.msg import String
from psr22p2_parte08_ex5.msg import Dog
from psr22p2_parte08_ex5.srv import SetDogName, SetDogNameResponse
from colorama import Fore, Style


def serviceRequestCallback(request, dog):
    print('Received a request to change dog name to ' + request.new_name)
    dog.name = request.new_name # actually change dog name

    response = SetDogNameResponse()
    response.result = 1
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
    publisher = rospy.Publisher('~chatter', Dog, queue_size=10)


    # Create my service
    service = rospy.Service('set_dog_name', SetDogName, partial(serviceRequestCallback, dog=dog))

    # ------------------------------------
    # Execution 
    # ------------------------------------
    frequency = rospy.get_param("/frequency")
    rate = rospy.Rate(frequency) 
    while not rospy.is_shutdown():
        # Get the highlight text color global parameter
        highlight_text_color = rospy.get_param("/highlight_text_color", 'RED')

        rospy.loginfo('Publishing ' + getattr(Fore, highlight_text_color) + str(dog) + Style.RESET_ALL)
        publisher.publish(dog)
        rate.sleep()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()