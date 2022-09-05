#!/usr/bin/python3
import audioop

import colorama
import pyaudio
import wave

def main():
    # -----------------------------------
    # Initialize
    # -----------------------------------
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    # -----------------------------------
    # Execution
    # -----------------------------------
    print("* recording")

    while True:
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        # print('rms = ' + str(rms))

        if rms > 1500:
            print(colorama.Fore.RED + 'Someone is speaking!            ' + colorama.Style.RESET_ALL, end='\r')
        else:
            print(colorama.Fore.BLUE + 'I am all alone!               ' + colorama.Style.RESET_ALL, end='\r')


    # -----------------------------------
    # Termination
    # -----------------------------------
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == '__main__':
    main()