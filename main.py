from tkinter import *

from tkinter import messagebox



class OpeningWindow: #first window

   def __init__(self, parent):

      background_color = 'gold2'

      self.opening_frame = Frame(parent, bg=background_color, padx=50, pady=130)

      self.opening_frame.grid()

      self.title_label = Label(self.opening_frame, text='MRGS Booking', fg='Dodgerblue4', font=('Helvetica', '30', 'bold'), bg=background_color)

      self.title_label.grid(row=0, padx=5, pady=5)

      self.start_button = Button(self.opening_frame, text='START',fg='white', bg='green', font=('Helvetica', '10', 'bold'), command=self.start)

      self.start_button.grid(row=2, padx=5, pady=10)
      self.exit_button = Button(self.opening_frame, text='EXIT', fg='white', bg='red', font=('Helvetica', '10', 'bold'), command=self.opening_frame.destroy)

      self.exit_button.grid(row=4, padx=5, pady=10)   

   def start(self):

      food.destroy()#destroy all window not just the frame
      #RegisterWindow(food)
      MainAppWindow() #now because we are using frames, we need a controller to control them, and the Applicatoin is the starting point

 

#I moved it from the bottom to here so you know this is the point to control all frames to follow

class MainAppWindow(Tk): #main window opens second

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


class RegisterFrame(Frame):# this frame sits on the Application window

      def __init__(self, parent, controller):

         Frame.__init__(self, parent)

         self.border = LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))

         self.border.pack(fill="both", expand="yes", padx = 150, pady=150)

         self.user_label = Label(self.border, text="Username", font=("Arial Bold", 15), bg='ivory')

         self.user_label.place(x=50, y=20)

         self.user_entry = Entry(self.border, width = 30, bd = 5)

         self.user_entry.place(x=180, y=20)

         self.password_label = Label(self.border, text="Password", font=("Arial Bold", 15), bg='ivory')

         self.password_label.place(x=50, y=80)

         self.password_entry = Entry(self.border, width = 30, show='*', bd = 5)

         self.password_entry.place(x=180, y=80)

         def verify():

            try:

               with open("users.txt", "r") as f:

                  info = f.readlines()

                  i  = 0

                  for e in info:

                     self.user_name, self.user_password =e.split(",")

                     if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():

                        controller.show_frame(Second)

                        i = 1

                        break

                  if i==0:

                     messagebox.showinfo("Error", "Please provide correct username and password!!")

            except:

               messagebox.showinfo("Error", "Couldnt open file")

 

 

         self.submitbutton = Button(self.border, text="Submit", font=("Arial", 15), command=verify)

         self.submitbutton.place(x=320, y=115)

 

         def register():

            register_window = Tk()

            register_window.resizable(0,0)

            register_window.configure(bg="ivory")

            register_window.title("Register")

            reg_name_label = Label(register_window, text="Username:", font=("Arial",15), bg="deep sky blue")

            reg_name_label.place(x=10, y=10)

            reg_name_entry = Entry(register_window, width=30, bd=5)

            reg_name_entry.place(x = 200, y=10)

 

            reg_password_label = Label(register_window, text="Password:", font=("Arial",15), bg="deep sky blue")

            reg_password_label.place(x=10, y=60)

            reg_password_entry = Entry(register_window, width=30, show="*", bd=5)

            reg_password_entry.place(x = 200, y=60)

 

            confirm_password_label = Label(register_window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")

            confirm_password_label.place(x=10, y=110)

            confirm_password_entry = Entry(register_window, width=30, show="*", bd=5)

            confirm_password_entry.place(x = 200, y=110)

 

            def check():

               if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":

                  if reg_password_entry.get()==confirm_password_entry.get():

                     with open("users.txt", "a") as f:

                        f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")

                        messagebox.showinfo("Welcome","You are registered successfully!!")

                        register_window.destroy()

                  else:

                     messagebox.showinfo("Error","Your password didn't get match!!")

               else:

                  messagebox.showinfo("Error", "Please fill the complete field!!")

 

            self.register_button = Button(register_window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)

            self.register_button.place(x=170, y=150)

 

            register_window.geometry("470x220")

            register_window.mainloop()

 

         self.register_button = Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)

         self.register_button.place(x=650, y=20)

 

class Second(Frame):

   def __init__(self, parent, controller):

      Frame.__init__(self, parent)

 

      self.title_label = Label(self, text="Start of Appliction, Welocme to my program....", bg = "ivory", font=("Arial Bold", 25))

      self.title_label.place(x=40, y=150)       

      self.next_button = Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(Third))

      self.next_button.place(x=650, y=450)

 

      self.back_button = Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Start))

      self.back_button.place(x=100, y=450)

 

#A lambda function is a small anonymous function(usually we dont need to reuse it)

#A lambda function can take any number of arguments, but can only have one expression

 

class Third(Frame):

   def __init__(self, parent, controller):

      Frame.__init__(self, parent)

 

      self.configure(bg='ivory')

 

      self.app_label = Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))

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