import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)
def binary(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]
try:
    while (True):
        a = input()
        if a == 'q':
            sys.exit()
        elif (a.isdigit()) and (int(a)%1 == 0) and (0 <= int(a) <= 255):
            GPIO.output(dac, binary(int(a)))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            print('cringe')
except ValueError():
    print('0-255')
except KeyboardInterrupt():
    print('done')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup