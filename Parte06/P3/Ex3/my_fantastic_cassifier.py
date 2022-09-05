#!/usr/bin/python3
import audioop

import colorama
import cv2
import numpy as np
import pyaudio
import wave


def main():

    while True:
        value = np.random.uniform(-1, 1)
        value2 = 1000*value + 500
        if value2 > 1000:
            print('this is right')
        else:
            print('this is left')


if __name__ == '__main__':
    main()
