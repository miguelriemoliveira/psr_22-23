#!/usr/bin/env python3
import audioop

import colorama
import cv2
import pyaudio
import wave
def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 0.5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    while True:
        # frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            # frames.append(data)

        # print("* done recording")
        # print(data)

        rms = audioop.rms(data, 2)  # width=2 for format=paInt16
        print(rms)
        if rms > 1000:
            print(colorama.Fore.RED + 'Something is making noise' + colorama.Style.RESET_ALL)
        else:
            print('Its so quiet around here ...')


    stream.stop_stream()
    stream.close()
    p.terminate()

    # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b''.join(frames))
    # wf.close()

if __name__ == '__main__':
    main()