#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
import audioop
import wave
from copy import deepcopy
from functools import partial

import pyaudio
import numpy as np
import cv2
from colorama import Fore, Style

# partial functionality
# NO GLOBAL VARIABLES



def main():
    # initial setup
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3 # TODO must check later if 3 secs is a good duration
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    rms_threshold = 2000
    while True:
        data = stream.read(chunk)
        rms = audioop.rms(data, 2)  # width=2 for format=paInt16


        # print('Data RMS = ' + str(rms))
        if rms > rms_threshold:
            print(Fore.RED + 'You are speaking!!!' + Style.RESET_ALL)
        else:
            print(Fore.BLUE + 'You are silent!!!' + Style.RESET_ALL)
            # TODO find a better color



if __name__ == '__main__':
    main()
