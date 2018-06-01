import serial
import time

ser=serial.Serial("COM3",9600,timeout=100)
while (ser.is_open):
    # x=int(input())
    # print(ser.in_waiting)
    # print(chr(x))
    # ser.write(chr(x).encode())
    # print(chr(x).encode())
    x=input()
    ser.write(x.encode())
    if(ser.in_waiting>0):
        data = str(ser.read(200))
        data = data.split('\\r\\n')
        print(data[20])
        ser.flushInput()
        ser.flushOutput()
