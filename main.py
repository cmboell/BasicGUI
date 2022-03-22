"""
Assignment: Basic GUI Assignment
Program: main.py
Author: Colby Boell
Last date modified: 03/22/2022

The purpose of this program is to create a basic gui project with python that allows the user to check boxes
and display a message accordingly.
"""
# importing
import tkinter


# defining functions/methods here
def pick_breakfast():
    label.config(text="Start the day off right!")


def pick_second_breakfast():
    label.config(text="Better than first breakfast")


def pick_lunch():
    label.config(text="Can't skip lunch")


def pick_dinner():
    label.config(text="Everyone loves dinner")


# creating  main window
m = tkinter.Tk()

# module code below here
# Main window title displayed in bar
m.title('Favorite Meal')

# Insert most main button code below
# label displays text which is placed second from bottom row
label = tkinter.Label(m, text="Waiting")
label.grid(row=4)

# Create Check buttons / creating integer variables
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast)
check.grid(row=0)

var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast)
check.grid(row=1)

var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch)
check.grid(row=2)

var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner",variable = var4,command= pick_dinner)
check.grid(row=3)


# main window exit/destroy function
exit_button = tkinter.Button(m, text='Exit', width=40, command=m.destroy)
exit_button.grid(row=5)

# infinite loop that waits for events to happen
m.mainloop()
