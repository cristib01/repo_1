# 1. import required modules
from tkinter import *

# 2. define window
window = Tk()
window.title('Click and salute')
window.geometry("250x250")

# define original_title
original_title = 'Click and salute'


# 3. define functions
def hello():
    print('I am learning')


def clicked():
    text = entry_text.get()
    display_text = 'Hello,' + text + '! How are you?'
    text1.config(text=display_text)


def clicked1():
    actual_fg = c_button.cget("fg")
    actual_bg = c_button.cget("bg")

    # Toggle the foreground and background colors
    new_fg = 'red' if actual_fg == 'red' else 'blue'
    new_bg = 'blue' if actual_bg == 'blue' else 'red'

    # Update the Button configuration with the new colors
    c_button.config(fg=new_fg, bg=new_bg)


def reseted():
    window.title(original_title)  # Reset the title to the original value
    text1.config(text='This is a two button window')  # Reset the label text
    entry_text.delete(0, END)  # Clear the entry text


def quit():
    window.destroy()


text1 = Label(text='This is a multi-buttoned window')
button1 = Button(window, fg='black', bg='white', text='Click me!', command=hello)
button2 = Button(window, text='Input me!', command=clicked)
r_button3 = Button(window, text='Reset', command=reseted)
q_button4 = Button(window, text='Quit', command=quit)
c_button = Button(window, fg='white', bg='black', text='Check me', command=clicked1)
entry_text = Entry(window)

text1.pack()
button1.pack()
button2.pack()
r_button3.pack()
entry_text.pack()
r_button3.pack()
c_button.pack()
q_button4.pack()

window.mainloop()
