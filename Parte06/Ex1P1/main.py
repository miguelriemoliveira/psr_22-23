#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
from copy import deepcopy
from functools import partial

import numpy as np
import cv2
from colorama import Fore, Style


def main():

    face_cascade = cv2.CascadeClassifier("cascade.xml")
    webcam = cv2.VideoCapture(0)
    
    # The program loops until it has 30 images of the face.
    count = 1
    while count < 30:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        print(faces)

        if len(faces)>=1:
            face = faces[0]
            x1 = face[0]
            y1 = face[1]
            w = face[2]
            h = face[3]
            cv2.rectangle(im,(x1,y1),(x1+w,y1+h),(0,255,0),3) 



        cv2.imshow('faces', im)
        cv2.waitKey(30)
if __name__ == '__main__':
    main()
