from pysabertooth import Sabertooth

saber = Sabertooth('/dev/serial0',baudrate=115200,address=125,timeout=0.1)

saber.drive(1,50)
saber.drive(2,-75)
