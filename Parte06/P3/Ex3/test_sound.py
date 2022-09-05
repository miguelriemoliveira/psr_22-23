#!/usr/bin/python3
import audioop

import colorama
import cv2
import pyaudio
import wave


def main():
    # -----------------------------------
    # Initialize
    # -----------------------------------

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    capture = cv2.VideoCapture(0)  # setup video capture for webcam
    # capture = cv2.VideoCapture('test2.mp4')  # setup video capture from video file

    # configure opencv window
    window_name = 'Ex3'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # -----------------------------------
    # Execution
    # -----------------------------------
    while True:
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        if rms > 20000:
            print(colorama.Fore.RED + 'Someone is shouting!!!' + colorama.Style.RESET_ALL)
            color = (0,0,255)
        elif rms > 2000:
            print(colorama.Fore.GREEN + 'Someone is speaking' + colorama.Style.RESET_ALL)
            color = (0,255,0)
        else:
            print(colorama.Fore.BLUE + 'I am all alone ...' + colorama.Style.RESET_ALL)
            color = (255,0,0)

        _, image = capture.read()  # get an image from the camera
        radius = int(round(min(rms,20000)/20000 * (100-10) + 10))
        cv2.circle(image, (100, 50), radius, color, -1)

        cv2.imshow(window_name, image)
        cv2.waitKey(5)

    # -----------------------------------
    # Termination
    # -----------------------------------
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()


if __name__ == '__main__':
    main()
