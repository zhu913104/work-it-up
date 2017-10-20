import serial

ser = serial.Serial('COM3')  # open COM4 port
while True:
    x=input()
    ser.write(x.encode("utf-8"))      # write a string
    ser.read()