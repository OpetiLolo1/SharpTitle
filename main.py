from tkinter import *

class OpeningWindow:

   def __init__(self, parent):

    background_color = 'gold2'

    self.opening_frame = Frame(parent, bg=background_color, padx=50, pady=130) 
    self.opening_frame.grid()

    self.title_label = Label(self.opening_frame, text='MRGS Booking', fg='Dodgerblue4', font=('Helvetica', '30', 'bold'), bg=background_color) 
    self.title_label.grid(row=0, padx=5, pady=5)

    self.title_label = Label
     
    self.start_button = Button(self.opening_frame, text='START',fg='white', bg='green', font=('Helvetica', '10', 'bold'), command=self.start)
    self.start_button.grid(row=2, padx=5, pady=10)

    self.exit_button = Button(self.opening_frame, text='EXIT', fg='white', bg='red', font=('Helvetica', '10', 'bold'), command=self.opening_frame.destroy)
    self.exit_button.grid(row=4, padx=5, pady=10)    
     
   def start(self): 
       self.opening_frame.destroy()
       RegisterWindow(food)

class RegisterWindow:
    def __init__(self, parent):

      background_color = 'deep sky blue'

      self.secondary_frame = Frame(parent, bg=background_colour, padx=100, pady=100)
     

if __name__ == '__main__': 
    food = Tk()
    food.geometry("440x400")
    food.title('MRGS Chromebook Booking')
    openingWindow_object = OpeningWindow(food)
    food.mainloop()