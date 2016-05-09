# Import modules
from tkinter import *
import eventManager

# Setup tkinter
tk = Tk()
canvas = Canvas(tk, width=500, height=500)

#Create addeditEvents
addeditEvents = eventManager.addeditEvents()

# Define variables
dayWidth = 68.571428571
dayHight = 83.333333333

# Make Calendar Rectangle
canvas.create_rectangle(10, 10, 480, 500)

# Make Squares
for x in range(1, 7):
    for x in range(1, 8):
        canvas.create_rectangle(10, 10, dayWidth, dayHight)
        dayWidth = dayWidth + 68.571428571
    dayHight = dayHight + 83.333333333
    dayWidth = 68.571428571

# Make Button
btnNewEvent = Button(tk, text="New event", command=addeditEvents.mknewEvent)

# Draw
btnNewEvent.pack()
canvas.pack()
