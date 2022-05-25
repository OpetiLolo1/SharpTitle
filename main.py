from tkinter import *

class OpeningWindow:

   def __init__(self, parent):
  
    background_color = 'deep sky blue'

    self.opening_frame = Frame(parent, bg=background_color, padx=10, pady=10) 
    self.opening_frame.grid()

    self.title_label = Label(self.opening_frame, text='MRGS Booking', fg='white', font=('Helvetica', '30', 'bold'), bg=background_color) 
    self.title_label.grid(row=0, padx=5, pady=5)

    self.start_button = Button(self.opening_frame, text='START',fg='white', bg='green', font=('Helvetica', '10', 'bold'), command=self.start)
    self.start_button.grid(row=2, padx=5, pady=5)

    self.exit_button = Button(self.opening_frame, text='EXIT', fg='white', bg='red', font=('Helvetica', '10', 'bold'), command=self.opening_frame.destroy)
    self.exit_button.grid(row=4, padx=5, pady=5)    

   def start(self): 
      self.opening_frame.destroy
      RegisterWindow(food)

class RegisterWindow:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        self.border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        self.border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        self.user_label = tk.Label(self.border, text="Username", font=("Arial Bold", 15), bg='ivory')
        self.user_label.place(x=50, y=20)
        self.user_entry = tk.Entry(self.border, width = 30, bd = 5)
        self.user_entry.place(x=180, y=20)
        
        self.password_label = tk.Label(self.border, text="Password", font=("Arial Bold", 15), bg='ivory')
        self.password_label.place(x=50, y=80)
        self.password_entry = tk.Entry(self.border, width = 30, show='*', bd = 5)
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
     
         
        self.submitbutton = tk.Button(self.border, text="Submit", font=("Arial", 15), command=verify)
        self.submitbutton.place(x=320, y=115)
        
        def register():
            register_window = tk.Tk()
            register_window.resizable(0,0)
            register_window.configure(bg="ivory")
            register_window.title("Register")
            reg_name_label = tk.Label(register_window, text="Username:", font=("Arial",15), bg="ivory")
            reg_name_label.place(x=10, y=10)
            reg_name_entry = tk.Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x = 200, y=10)
            
            reg_password_label = tk.Label(register_window, text="Password:", font=("Arial",15), bg="ivory")
            reg_password_label.place(x=10, y=60)
            reg_password_entry = tk.Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 200, y=60)
            
            confirm_password_label = tk.Label(register_window, text="Confirm Password:", font=("Arial",15), bg="ivory")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(register_window, width=30, show="*", bd=5)
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
                    
            self.register_button = tk.Button(register_window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        self.register_button.place(x=650, y=20)
        
class Second:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.title_label = tk.Label(self, text="Start of Appliction, Welocme to my program....", bg = "ivory", font=("Arial Bold", 25))
        self.title_label.place(x=40, y=150)        
        self.next_button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(Third))
        self.next_button.place(x=650, y=450)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.back_button.place(x=100, y=450)
        
#A lambda function is a small anonymous function(usually we dont need to reuse it)
#A lambda function can take any number of arguments, but can only have one expression 

class Third:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='ivory')
        
        self.app_label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "ivory", font=("Arial Bold", 25))
        self.app_label.place(x=40, y=150)
        
        self.home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.home_button.place(x=650, y=450)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Second))
        self.back_button.place(x=100, y=450)
        
'''https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/
above link explains the new *args,**kwargs arguments used below
Like "self," actually typing out "args" and "kwargs" is not necessary, the asterisks to the trick. It is just common to add the "args" and "kwargs." 
So what are these? These are used to pass a variable, unknown, amount of arguments through the method. The difference between them is that args are used to pass non-keyworded arguments, 
where kwargs are keyword arguments (hence the meshing in the name to make it kwargs). Args are your typical parameters. Kwargs, will basically be dictionaries.
You can get by just thinking of kwargs as dictionaries that are being passed.
'''
        
class Application:
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
      
        self.window = tk.Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (Start, Second, Third):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")



if __name__ == '__main__': 
    food = Tk()
    food.title('MRGS Chromebook Booking')
    openingWindow_object = OpeningWindow(food)
    food.mainloop()