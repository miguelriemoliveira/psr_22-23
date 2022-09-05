#!/usr/bin/env python3
import argparse
from functools import partial

import colorama
import rospy
from psr_parte09_preparation.msg import Dog
from psr_parte09_preparation.srv import SetDogName, SetDogNameRequest, SetDogNameResponse


def serviceRequestedCallback(request, dog):
    rospy.loginfo('Received request to change dog name to ' + request.new_name)

    dog.name = request.new_name  # change dog name

    # Prepare response and send
    response = SetDogNameResponse()
    response.result = True
    return response


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    dog = Dog()  # create a dog message to send
    dog.name, dog.age, dog.color = 'max', 18, 'black'
    dog.brothers.append('lily')
    dog.brothers.append('boby')

    highlight_text_color = rospy.get_param("/highlight_text_color")  # get color parameter
    print(highlight_text_color)

    server = rospy.Service('~set_dog_name', SetDogName, partial(serviceRequestedCallback, dog=dog))

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():

        rospy.loginfo('Publishing dog named ' + getattr(colorama.Fore, highlight_text_color) +
                      dog.name + colorama.Style.RESET_ALL)
        pub.publish(dog)
        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
