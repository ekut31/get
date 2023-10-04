import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)
def binary(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]
try:
    while (True):
        T = input()
        if not T.isdigit():
            print("Введите число")
        t = int(T)/510
        for i in range (0,256):
            GPIO.output(dac, binary(i))
            print(i)
            sleep(t)
        for i in range(254, -1, -1):
            GPIO.output(dac, binary(i))
            print(i)
            sleep(t)

finally:
    GPIO.output(dac,1)
    GPIO.cleanup()