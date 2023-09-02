from tkinter import *

# create window
window = Tk()
window.title("First ever window")

# create widgets
top_frame = Frame(window)
middle_frame = Frame(window)
middle_frame_left = Frame(middle_frame)
middle_frame_right = Frame(middle_frame)
bottom_frame = Frame(window)

top_frame.pack(side=TOP)
middle_frame.pack()
middle_frame_left.pack(side=LEFT)
middle_frame_right.pack(side=RIGHT)
bottom_frame.pack()

text1 = Label(top_frame, text='This is the top')
button1 = Button(middle_frame_left, text='Button 1', fg='green')
button2 = Button(middle_frame_left, text='Button 2', fg='red')
button3 = Button(bottom_frame, text='Button 3', fg='blue')
button4 = Button(bottom_frame, text='Button 4', fg='red')
text2 = Label(middle_frame_right, text='This is the middle')

# place widgets into window container using the pack layout
text1.pack(side=TOP)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
text2.pack()

# open window
window.mainloop()
