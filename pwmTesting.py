from tkinter import *
import _thread
import time
import numpy as np
import RPi.GPIO as IO

#Default colors for filter, later to be changed by GUI
pwmOne = 100;
pwmTwo = 100;

top = Tk()
texts = ["S1","S2"]
labels = []
inputs = []
for i in range(2):
	label = Label(top, text = texts[i])
	label.grid(row = i)
	labels.append(label)
	input_ = Scale(top, from_=0, to=100,orient = HORIZONTAL)
	input_.grid(row = i, column = 1)
	inputs.append(input_)
IO.setwarnings(False);
IO.setmode(IO.BCM);
IO.setup(19,IO.OUT);
pOne = IO.PWM(19,100);
pOne.start(0);
pTwo = IO.PWM(19,100);
pTwo.start(0);

def updateValues():
	pwmOne = inputs[0].get();
	pwmTwo = inputs[1].get();
	pOne.ChangeDutyCycle(pwmOne);
	pTwo.ChangeDutyCycle(pwmTwo);

	print(pwmOne);
	print(pwmTwo);

button = Button(top, text ="Update", command = updateValues)
button.grid(row = len(labels), column = 1)

top.mainloop()


