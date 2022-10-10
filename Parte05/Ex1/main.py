#!/usr/bin/env python
# --------------------------------------------------
# OpenCV tutorial
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='OpenCV tutorial')
    parser.add_argument('-p','--path', type=str, help='Path to the image', required=False)

    args = parser.parse_args()

    image_filename = '/home/filipeg/Desktop/psr_22-23/Parte05/docs/atlascar2_multichannel_thresholded.png' if args.path != "" else args.path

    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    # cv2.imshow("window",image)
    # cv2.waitKey(0)

    img1 = cv2.imread('/home/filipeg/Desktop/psr_22-23/Parte05/docs/atlascar2_multichannel_thresholded.png', cv2.IMREAD_COLOR) # Load an image
    img2 = cv2.imread('/home/filipeg/Desktop/psr_22-23/Parte05/docs/atlascar2_thresholded.png', cv2.IMREAD_COLOR)

    while True:
        cv2.imshow("window",img1)
        cv2.waitKey(3000)

        cv2.imshow("window",img2)
        cv2.waitKey(3000)


if __name__ == '__main__':
    main()