#!/usr/bin/env python3

import cv2
import numpy as np


def main():


    # --------------------
    # Initialization
    # -------------------
    image_filename = '../images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    threshold_level_b = 50
    threshold_level_g = 100
    threshold_level_r = 150

    # --------------------
    # Execution
    # -------------------
    # -----------
    # Processing
    # -----------
    lower_bound = np.array([0,60, 0])
    upper_bound = np.array([50,256,50])

    image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # -----------
    # Visualization
    # -----------
    cv2.imshow('RGB Image', image_rgb)  # Display the image
    # cv2.imshow('GRAY Image', image_gray)  # Display the image
    cv2.imshow('Mask Image', image_mask)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # --------------------
    # Termination
    # -------------------

    # typically has very little here



if __name__ == "__main__":
    main()
