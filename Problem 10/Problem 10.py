# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time


def Schedule(f, delay):
    time.sleep(delay / 1000)
    f()


def StrOut(string):
    def printStr():
        print(string)
    return printStr


Schedule(StrOut("lol"), 1000)
