from tkinter import *

class OpeningWindow:

  def __init__(self, parent):



   def start(self): 
      self.quiz_frame.destroy
      RegisterWindow(root)


if __name__ == '__main__': 
    root = Tk()
    root.title('MRGS Chromebook Booking')
    root.mainloop()