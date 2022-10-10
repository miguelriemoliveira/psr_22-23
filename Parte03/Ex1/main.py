#!/usr/bin/env python
# --------------------------------------------------
# Time - Tic and Toc
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

from cmath import sqrt
from time import time, ctime

max_num = 50000000

TIME = 0

def tic():
    global TIME
    TIME = time()

def toc():
    global TIME
    TIME = time() - TIME

def main():
    global TIME
    
    tic()
    print(f"Start: {ctime()}")
    for i in range(max_num):
        result = sqrt(i)
    toc()
    print(f"End: {ctime()}")
    print(f"Time spent: {TIME}")

if __name__ == "__main__":
    main()