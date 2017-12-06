import serial

ser = serial.Serial('COM4')  # open COM4 port
while ser.is_open:
    y=ser.read(8)
    print(y.decode("utf-8"))