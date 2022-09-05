#!/usr/bin/env python3
import copy

import colorama
import cv2
import numpy as np


def main():
    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------
    capture = cv2.VideoCapture(0)  # setup video capture for webcam
    # capture = cv2.VideoCapture('test2.mp4')  # setup video capture from video file

    # configure opencv window
    window_name = 'Ex3'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # Load the cascade
    # path_to_classifier = '/home/mike/workingcopy/opencv-4.5.4/data/haarcascades/'
    # face_cascade = cv2.CascadeClassifier(path_to_classifier + 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default3.xml')

    # -----------------------------------------------------
    # EXECUTION
    # -----------------------------------------------------
    image_gray_previous = None
    while True:
        _, image = capture.read()  # get an image from the camera


        if image is None:
            print('Video is over, terminating.')
            break  # video is over

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
        if image_gray_previous is None:
            image_gray_previous = copy.deepcopy(image_gray)

        height,width,_ = image.shape
        image_gui = copy.deepcopy(image)
        # -----------------------------------------------------
        # Face detection
        # -----------------------------------------------------
        faces = face_cascade.detectMultiScale(image_gray, 1.1, 4) # Detect the faces

        for (x, y, w, h) in faces: # Draw the rectangle around each face
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2) # draw blue rectangle around face

            mask_face = np.ndarray((height,width), dtype=np.uint8) # create a mask same size as image
            mask_face.fill(0) # set image to all zeros
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)  # draw blue rectangle around face

            # image_gui[mask_face.astype(bool)] = (255,255,0)
            cv2.add(image, (-10, 50, -10, 0), dst=image_gui, mask=mask_face)  # paint face color green

            # Get a mask of the mouht?
            mask_mouth = np.ndarray((height,width), dtype=np.uint8) # create a mask same size as image
            mask_mouth.fill(0) # set image to all zeros
            mask_mouth = cv2.rectangle(mask_mouth, (x, int(y + h - round(h/3))), (x + w, y + h), 255, -1)  # draw blue rectangle around face

            # compute difference between two images
            diff = cv2.absdiff(image_gray, image_gray_previous) * (mask_mouth/255)
            total = np.sum(diff)
            print(total)
            if total > 15000:
                print(colorama.Fore.RED + 'Mouth is moving ' + colorama.Style.RESET_ALL)

            cv2.imshow('mask_face', mask_face)
            cv2.imshow('mask_mouth', mask_mouth)
            cv2.imshow('diff', diff)


        cv2.imshow(window_name, image_gui)
        key = cv2.waitKey(20)

        if key == ord('q'):  # q for quit
            print('You pressed q ... aborting')
            break

        image_gray_previous = copy.deepcopy(image_gray)

    # -----------------------------------------------------
    # TERMINATION
    # -----------------------------------------------------
    # TODO terminate video capture


if __name__ == '__main__':
    main()
