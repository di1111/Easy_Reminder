# Import modules
from tkinter import *
import eventManager
import datetime

# Setup
tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
now = datetime.datetime.now()

# Define variables
dayWidth = 
dayHight = 

year = now.year
month = now.month
month = month-1

months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'November', 'December']

# Make Calendar Rectangle
canvas.create_rectangle(10, 10, 470, 500)

# Function stuff
class viewManager():
    def listView(self):
        print("list view")

# Make Squares
for x in range(1, 7):
    for x in range(1, 8):
        canvas.create_rectangle(10, 10, dayWidth, dayHight)
        dayWidth = dayWidth + 142.85714286 #NEED TO FIX
    dayHight = dayHight + 166.66666667
    dayWidth = 142.85714286

#Create addeditEvents
addeditEvents = eventManager.addeditEvents()
viewManager = viewManager()

# Make Button
btnNewEvent = Button(tk, text="New event", command=addeditEvents.mknewEvent)
btnListView = Button(tk, text="List", command=viewManager.listView)

# Draw
btnNewEvent.pack()
btnListView.pack()
canvas.pack()

print(year)
print(month)
print(months[month])
