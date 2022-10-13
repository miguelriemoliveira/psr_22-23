#!/usr/bin/env python3

import argparse

import cv2


def main():


    # -------------------------------------------------------
    # Initialization
    # -------------------------------------------------------
    parser = argparse.ArgumentParser(description='Reading and displaying two images.')
    parser.add_argument('-i1', '--image1', type=str, required=False, default='../images/atlascar.png')
    parser.add_argument('-i2', '--image2', type=str, required=False, default='../images/atlascar2.png')


    args_as_obj = parser.parse_args()
    print(args_as_obj)

    print(args_as_obj.image1)


    args_as_dict = vars(parser.parse_args())
    print(args_as_dict)

    print(args_as_dict['image1'])



    exit(0)
    image_rgb1 = cv2.imread(args['image1'], cv2.IMREAD_COLOR) # Load an image
    image_rgb2 = cv2.imread(args['image2'], cv2.IMREAD_COLOR) # Load an image

    # -------------------------------------------------------
    # Execution
    # -------------------------------------------------------
    flip_flop = True
    while True:

        # -----------
        # Processing
        # -----------
        flip_flop = not flip_flop
        
        # -----------
        # Visualization
        # -----------
        if flip_flop:
            cv2.imshow('RGB Image', image_rgb1)  # Display the image
        else:
            cv2.imshow('RGB Image', image_rgb2)  # Display the image

        cv2.waitKey(3000) # wait for a key press before proceeding

    # --------------------
    # Termination
    # -------------------

    # typically has very little here



if __name__ == "__main__":
    main()
