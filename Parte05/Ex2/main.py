#!/usr/bin/env python
# --------------------------------------------------
# OpenCV tutorial 2
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2
import numpy as np
import copy

def main():

    image_filename = '/home/filipeg/Desktop/psr_22-23/Parte05/docs/atlascar2_multichannel_thresholded.png'

    # b)

    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

    retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    image_thresholded_2 = (image_gray > 128) * (np.ones(image_gray.shape) * 255)

    # cv2.imshow('original', image_original)  # Display the image
    # cv2.imshow('gray', image_gray)  # Display the image
    # cv2.imshow('processed', image_thresholded)  # Display the image
    # cv2.imshow('processed_cv2', image_thresholded_2)



    # c)

    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image_rgb)

    # Process image
    _, image_b_processed = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    _, image_g_processed = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    _, image_r_processed = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)

    new_image_rgb = cv2.merge((image_b_processed, image_g_processed, image_r_processed))

    # cv2.imshow('original', image_rgb)  # Display the image
    # cv2.imshow('processed b', image_b_processed)  # Display the image
    # cv2.imshow('processed g', image_g_processed)  # Display the image
    # cv2.imshow('processed r', image_r_processed)  # Display the image
    # cv2.imshow('new_image_rgb' , new_image_rgb)  # Display the image



    # d)

    ranges = {'b': {'min': 0, 'max': 100},
              'g': {'min': 80, 'max': 256},
              'r': {'min': 0, 'max': 100}}

    # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image_rgb, mins, maxs)
    # conversion from numpy from uint8 to bool
    mask = mask.astype(np.bool)

    image_processed = (copy.deepcopy(image_rgb))
    image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)] * 0.4).astype(np.uint8)
    image_processed[mask] = (0,255,0)

    # Visualization
    # cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('original', image_rgb)  # Display the image
    # cv2.imshow('mask', mask.astype(np.uint8)*255)  # Display the image
    # cv2.imshow('image_processed' , image_processed)  # Display the image



    # e) -------- DUNNO STILL --------

    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

    # conversion from numpy from uint8 to bool
    mask = mask.astype(np.bool)

    image_processed = (copy.deepcopy(image_hsv))
    image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)] * 0.4).astype(np.uint8)
    image_processed[mask] = (0,255,0)

    # Visualization
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', image_hsv)  # Display the image
    cv2.imshow('mask', mask.astype(np.uint8)*255)  # Display the image
    cv2.imshow('image_processed' , image_processed)  # Display the image



    # f)
    mask = cv2.inRange(image_rgb, mins, maxs)
    # conversion from numpy from uint8 to bool
    mask = mask.astype(np.bool)

    image_processed = (copy.deepcopy(image_rgb))
    image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)] * 0.4).astype(np.uint8)
    image_processed[mask] = (0,0,255)   

    # Visualization
    # cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('original', image_rgb)  # Display the image
    # cv2.imshow('mask', mask.astype(np.uint8)*255)  # Display the image
    # cv2.imshow('image_processed' , image_processed)  # Display the image

    cv2.waitKey(10000)


if __name__ == '__main__':
    main()