from tkinter import *

window = Tk()
window.title("Exercise 2")

topFrame = Frame(window)
middleFrame1 = Frame(window)
middleFrame2 = Frame(window)
bottomFrame = Frame(window)
topFrame.pack()
middleFrame1.pack()
middleFrame2.pack()
bottomFrame.pack()

text1 = Label(topFrame, text="This application demonstrates frame layout")
# TODO make your button objects here (all 9 of them!)

text1.pack()
# TODO pack your buttons into the window here


window.mainloop()
