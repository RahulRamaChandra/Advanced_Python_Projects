"""
The great part of creating your own GUI apps is that you can customize them however you want.
From text font to background colour, all features are available for customization.

"""

# importing libraries

from tkinter import Label, Tk
import time

# defining title and size of our application

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

# defining font of the time and its color, border width and the backgorund color of the digital clock

text_font       = ("Boulder", 68, 'bold')
background      = "#f2e750"
foreground      = "#363529"
border_width    = 25

# combine all the elements to define label of the clock application

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# main function for digital clock

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()