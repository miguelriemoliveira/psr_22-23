#!/usr/bin/env python3
import argparse
import math
import random
from functools import partial

import rospy
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from std_msgs.msg import String, Header, ColorRGBA
from colorama import Fore, Style
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


def main():

    numbers = [234,243,1,23,2,53,646]

    idx = 0
    for number in numbers:
        print('number ' + str(number) + ' has idx ' + str(idx))
        idx += 1

    # Alternative using enumerate
    for number_idx, number in enumerate(numbers):
    # for number_idx_and_value in enumerate(numbers):
        print('number ' + str(number) + ' has idx ' + str(idx))



if __name__ == '__main__':
    main()