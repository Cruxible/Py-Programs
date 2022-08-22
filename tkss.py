# Import the required libraries
from tkinter import *
import pyautogui
from PIL import ImageTk, Image

# Create an instance of tknter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")


# Define a function to take the screenshot
def take_screenshot():
   x = 500
   y = 500
   # Take the screenshot in the given corrds
   im1 = pyautogui.screenshot(region=(x, y, 700, 300))

   # Create a toplevel window
   top = Toplevel(win)
   im1 = ImageTk.PhotoImage(im1)

   # Add the image in the label widget
   image1 = Label(top, image=im1)
   image1.image = im1
   image1.place(x=0, y=0)

Button(win, text='Take ScreenShot', command=take_screenshot).pack(padx=10, pady=10)

win.mainloop()