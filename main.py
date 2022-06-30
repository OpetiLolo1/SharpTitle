from tkinter import *
from tkinter import messagebox


class OpeningWindow: #first window

   def __init__(self, parent):

      background_color = 'gold2'

      self.opening_frame = Frame(parent, bg=background_color, padx=50, pady=130)
      self.opening_frame.grid()

      self.title_label = Label(self.opening_frame, text='MRGS Booking', fg='white', font=('Helvetica', '30', 'bold'), bg=background_color)
      self.title_label.grid(row=0, padx=5, pady=5)

      self.start_button = Button(self.opening_frame, text='Next',fg='white', bg='green', font=('Helvetica', '15'), command=self.start)
      self.start_button.grid(row=2, padx=5, pady=10)
     
      self.exit_button = Button(self.opening_frame, text='Exit', fg='white', bg='red', font=('Helvetica', '15'), command=self.opening_frame.destroy)
      self.exit_button.grid(row=4, padx=5, pady=10)   

   def start(self):

      food.destroy()#destroy all window not just the frame
      #RegisterWindow(food)
      MainAppWindow() #now because we are using frames, we need a controller to control them, and the Applicatoin is the starting point

 

#I moved it from the bottom to here so you know this is the point to control all frames to follow




class MainAppWindow(Tk): #main window conrols all frames, opens second 

   def __init__(self, *args, **kwargs):

      Tk.__init__(self, *args, **kwargs)

      self.window = Frame(self)
      self.window.pack()
      self.window.grid_rowconfigure(0, minsize = 500)
      self.window.grid_columnconfigure(0, minsize = 800)

      self.frames = {}
      for F in (RegisterFrame, Second, Third):
         frame = F(self.window, self)     
         self.frames[F] = frame
         frame.grid(row = 0, column=0, sticky="nsew")
        
      self.show_frame(RegisterFrame)

   def show_frame(self, page):

      frame = self.frames[page]
      frame.tkraise()
      self.title("MRGS Chromebook Booking")




class RegisterFrame(Frame):# this frame sits on the Main App window

      def __init__(self, parent, controller):

         Frame.__init__(self, parent)

         self.configure(bg='gold2')

         self.border = LabelFrame(self, text='Login', fg='white', bg='red3', bd = 10, font=('Helvetica', '25', 'bold'))
         self.border.pack(fill="both", expand="yes", padx = 0, pady= 100)

         self.user_label = Label(self.border, text="Student ID", fg='white', font=('Helvetica Bold', 18), bg='red3')
         self.user_label.place(x=200, y=80)

         self.user_entry = Entry(self.border, width = 30, bd = 5)
         self.user_entry.place(x=340, y=80)

         self.password_label = Label(self.border, text="Password", fg='white', font=('Helvetica Bold', 18), bg='red3')
         self.password_label.place(x=200, y=125)

         self.password_entry = Entry(self.border, width = 30, show='*', bd = 5)
         self.password_entry.place(x=340, y=125)

         def verify():

            try:
               with open("UsersIDandPassword.txt", "r") as f:
                  info = f.readlines()
                  i  = 0
                  for e in info:
                     self.user_name, self.user_password =e.split(",")
                     if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                        controller.show_frame(Second)
                        i = 1
                        break
                  if i==0:
                     messagebox.showinfo("Error", "Please provide correct student ID and password!!")
            except:
               messagebox.showinfo("Error", "Incorrect details")

         self.submitbutton = Button(self.border, text="Submit", fg='white', bg='green', font=('Helvetica', 15), command=verify)
         self.submitbutton.place(x=660, y=200)

         def register():

            register_window = Tk()
            register_window.resizable(0,0)
            register_window.configure(bg="red3")
            register_window.title("Register")

            reg_name_label = Label(register_window, text="Student ID:", fg='white', font=('Helvetica',15), bg="red3")
            reg_name_label.place(x=10, y=10)
            reg_name_entry = Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x = 220, y=10)
            
            reg_password_label = Label(register_window, text="Password:", fg='white', font=('Helvetica',15), bg="red3")
            reg_password_label.place(x=10, y=60)
            reg_password_entry = Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 220, y=60)

            confirm_password_label = Label(register_window, text="Confirm Password:", fg='white', font=('Helvetica',15), bg="red3")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = Entry(register_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 220, y=110)
 
            def check():

               if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                  if reg_password_entry.get()==confirm_password_entry.get():
                     with open("UsersIDandPassword.txt", "a") as f:
                        f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                        messagebox.showinfo("Welcome","You are registered successfully!!")
                        register_window.destroy()
                  else:
                     messagebox.showinfo("Error","Your password didn't get match!!")
               else:
                  messagebox.showinfo("Error", "Please fill the complete field!!")

            self.register_button = Button(register_window, text="Sign in", fg='white', font=("Arial",15), bg="orange", command=check)

            self.register_button.place(x=375, y=160)
            
            register_window.geometry("500x220")
            register_window.mainloop()

         self.register_button = Button(self, text="Register", fg='white', bg = "orange", font=("Helvetica",15), command=register)
         self.register_button.place(x=650, y=20) 




class Second(Frame):

   def __init__(self, parent, controller):
      Frame.__init__(self, parent)

      self.configure(bg='gold2')

      self.border = LabelFrame(self, fg='white', bg='red3', bd = 10, font=('Helvetica', '25', 'bold'))
      self.border.pack(fill="both", expand="yes", padx = 0, pady= 100)

      self.title_label = Label(self, text="Please type which periods you need a chromebook for", fg = 'white', bg = "red3", font=("Helvetcia Bold", 20))
      self.title_label.place(x=40, y=150)

      self.title_label = Label(self, text="E.g. 1,2,3,4,5", fg='white', bg = "red3", font=("Helvetica Bold", 20))
      self.title_label.place(x=40, y=200)

      self.password_entry = Entry(self, width = 30, bd = 5)
      self.password_entry.place(x=310, y=250)

      self.next_button = Button(self, text="Next", fg='white', bg='green', font=("Arial", 15), command=lambda: controller.show_frame(Third))
      self.next_button.place(x=650, y=450)

      self.back_button = Button(self, text="Back", fg='white', bg='red', font=("Arial", 15), command=lambda: controller.show_frame(RegisterFrame))
      self.back_button.place(x=100, y=450)

        

#A lambda function is a small anonymous function(usually we dont need to reuse it)

#A lambda function can take any number of arguments, but can only have one expression

class Third(Frame):

   def __init__(self, parent, controller):
      Frame.__init__(self, parent)

      self.configure(bg='gold2')
 
      self.app_label = Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "gold2", font=("Arial Bold", 25))
      self.app_label.place(x=40, y=150)

      self.home_button = Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Start))
      self.home_button.place(x=650, y=450) 

      self.back_button = Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Second))
      self.back_button.place(x=100, y=450)

 

if __name__ == '__main__':

   food = Tk()
   food.geometry("440x400")
   food.title('MRGS Chromebook Booking')
   openingWindow_object = OpeningWindow(food)
   food.mainloop()
  