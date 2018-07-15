import time
import serial
ser = serial.Serial(

    port='/dev/serial0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    
    timeout=1
)
while True:
    f = open ('Thermo.txt', 'a')
    ser.write('ATAK\r')
    time.sleep(.02)
    ser.write('AUAF\r')
    time.sleep(.02)
    ser.write('ARA\r')
    #time.sleep(.02)
    x=ser.readline()
    outstring = str(x)+" "+"\n"
    f.write(outstring)
    f.close
##    print str(x)
##ser.write("ATAK\r")
##time.sleep(.020)
##ser.write("AUAC\r")
##time.sleep(.020)
##ser.write("ARA\r")
##
##time.sleep(.10)
##x=ser.readline()
##print x
###counter += 1
