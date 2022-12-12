# import modules
from tkinter import *


# define all functions
def clicked():
    name = name_entry.get()
    surname = surname_entry.get()
    # TODO create the welcome message and configure the text attribute of the message_label
    message_label.config(text=f"Hello, {name} {surname}")


# create window
window = Tk()
window.title("Exercise 5")
window.geometry("300x150")

# create widgets
# TODO Create your widgets
top_frame = Frame(window)
middle_frame = Frame(window)
bottom_frame = Frame(window)
name_label = Label(top_frame, text="Name")
surname_label = Label(middle_frame, text="Surname")
name_entry = Entry(top_frame, text="Enter your name")
surname_entry = Entry(middle_frame, text="Enter your surname")
register_button = Button(bottom_frame, text="Register", command=clicked)
message_label = Label(bottom_frame, text="")

# pack widgets into window container
top_frame.pack(fill="both")
middle_frame.pack(fill="both")
bottom_frame.pack(fill="both")
name_label.pack(side=LEFT)
name_entry.pack(side=RIGHT, fill="both", expand=True)
surname_label.pack(side=LEFT)
surname_entry.pack(side=LEFT, fill="both", expand=True)
register_button.pack(side=TOP)
message_label.pack(side=BOTTOM)

# open window
window.mainloop()
