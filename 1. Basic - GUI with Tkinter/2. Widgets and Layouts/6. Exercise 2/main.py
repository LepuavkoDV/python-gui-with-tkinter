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
button1 = Button(middleFrame1, text='button1', fg='black')
button2 = Button(middleFrame1, text='button2', fg='black')
button3 = Button(middleFrame1, text='button3', fg='black')
button4 = Button(middleFrame2, text='button4', fg='black')
button5 = Button(middleFrame2, text='button5', fg='black')
button6 = Button(middleFrame2, text='button6', fg='black')
button7 = Button(bottomFrame, text='button7', fg='black')
button8 = Button(bottomFrame, text='button8', fg='black')
button9 = Button(bottomFrame, text='button9', fg='black')

text1.pack()
# TODO pack your buttons into the window here
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='right')
button4.pack(side='left')
button5.pack(side='left')
button6.pack(side='right')
button7.pack(side='left')
button8.pack(side='left')
button9.pack(side='right')

window.mainloop()
