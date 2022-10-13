#!/usr/bin/env python3

import cv2


def main():


    # --------------------
    # Initialization
    # -------------------
    image_filename = '../images/atlascar2.png'
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
    image_b,image_g,image_r = cv2.split(image_rgb)

    _, image_thresholded_b = cv2.threshold(image_b, threshold_level_b, 255, cv2.THRESH_BINARY)
    _, image_thresholded_g = cv2.threshold(image_g, threshold_level_g, 255, cv2.THRESH_BINARY)
    _, image_thresholded_r = cv2.threshold(image_r, threshold_level_r, 255, cv2.THRESH_BINARY)

    image_thresholded_rgb = cv2.merge((image_thresholded_b, image_thresholded_g, image_thresholded_r))

    # -----------
    # Visualization
    # -----------
    cv2.imshow('RGB Image', image_rgb)  # Display the image
    # cv2.imshow('GRAY Image', image_gray)  # Display the image
    cv2.imshow('THRES Image', image_thresholded_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # --------------------
    # Termination
    # -------------------

    # typically has very little here



if __name__ == "__main__":
    main()
