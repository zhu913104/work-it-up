import serial
import time
from msvcrt import getch

ser=serial.Serial("COM3",9600,timeout=10)
while True:
    x = input()
    if (x):
        ser.write(x.encode())
