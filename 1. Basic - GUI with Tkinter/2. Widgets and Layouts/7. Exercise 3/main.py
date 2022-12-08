from tkinter import *

window = Tk()
window.title("Exercise 3")

top_frame = Frame(window)
left_frame = Frame(window)
left_top_frame = Frame(left_frame)
left_bottom_frame = Frame(left_frame)
right_frame = Frame(window)
top_frame.pack()
left_frame.pack(side='left')
left_top_frame.pack(side='top')
left_bottom_frame.pack(side='bottom')
right_frame.pack(side='right')
text1 = Label(top_frame, text="This application demonstrates frame layout")
text2 = Label(right_frame, text='text 2')
button1 = Button(left_top_frame, text='button 1', fg='black')
button2 = Button(left_top_frame, text='button 2', fg='black')
button3 = Button(left_bottom_frame, text='button 3', fg='black')
button4 = Button(left_bottom_frame, text='button 4', fg='black')
text1.pack()
button1.pack(side='left')
button2.pack(side='right')
button3.pack(side='left')
button4.pack(side='right')
text2.pack(side='top')

window.mainloop()
