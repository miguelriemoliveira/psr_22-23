#!/usr/bin/env python3

import cv2


def main():


    # --------------------
    # Initialization
    # -------------------
    image_filename = '../images/atlascar2.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    threshold_level = 128

        # --------------------
    # Execution
    # -------------------


    # -----------
    # Processing
    # -----------
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    _, image_thresholded = cv2.threshold(image_gray, threshold_level, 255, cv2.THRESH_BINARY)


    # -----------
    # Visualization
    # -----------
    print(image_rgb.shape)
    print(image_gray.shape)
    print(image_thresholded.shape)



    cv2.imshow('RGB Image', image_rgb)  # Display the image
    cv2.imshow('GRAY Image', image_gray)  # Display the image
    cv2.imshow('THRES Image', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # --------------------
    # Termination
    # -------------------

    # typically has very little here



if __name__ == "__main__":
    main()
