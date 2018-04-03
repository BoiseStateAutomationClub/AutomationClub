from Tkinter import *
import time
import numpy as np
import serial

top = Tk()
texts = ["S1"]
labels = []
inputs = []
for i in range(1):
  label = Label(top, text = texts[i])
  label.grid(row = i)
  labels.append(label)
  input_ = Scale(top, from_=0, to=100,orient = HORIZONTAL)
  input_.grid(row = i, column = 1)
  inputs.append(input_)

ser = serial.Serial(
  
   port='/dev/ttyAMA0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0

def updateValues():
  byte = inputs[0].get();
  ser.write(byte);
  print(byte);

button = Button(top, text ="Update", command = updateValues)
button.grid(row = len(labels), column = 1)

top.mainloop()