import tkinter as tk
import customtkinter
import psycopg2
from sql import store_password, delet_password, connect, tablecheck
from sql2 import store_password2, check_email, check_password

customtkinter.set_appearance_mode("Dark")
B_email = None

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Manager")
        self.geometry(f"{400}x{550}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)
        
        self.label = customtkinter.CTkLabel(self, text="Sign-Up", font = ("Helvetica",20))
        self.label.grid(row=0, column = 1 ,padx=20, pady=20)
        
        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Email: ", width = 200, border_color="yellow")
        self.email_entry.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        self.email_entry.bind("<Return>",lambda funct1:self.pass_entry.focus())
        
        self.pass_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Password:  ", width = 200, border_color="yellow")
        self.pass_entry.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.pass_entry.bind("<Return>",lambda funct1:self.passc_entry.focus())
        
        self.passc_entry = customtkinter.CTkEntry(self, placeholder_text="Confirm Your Password:  ", width = 200,border_color="yellow")
        self.passc_entry.grid(row=3, column=1, padx=20, pady=10, sticky="n")
        self.passc_entry.bind(self.on_enter_pressed)
        
        self.button = customtkinter.CTkButton(self, text="Create Account", command=self.on_enter_pressed, width = 200, fg_color="yellow",text_color="black")
        self.button.grid(row=5, column=1, padx=20, pady=10, sticky="n")
        
        self.label = customtkinter.CTkLabel(self, text="This is the only password you will need to remember!", font = ("Helvetica",14))
        self.label.grid(row=6, column = 1 ,padx=20, pady=20)
    
    def on_enter_pressed(self):
        email  = self.email_entry.get()
        password = self.pass_entry.get()
        cpassword  = self.passc_entry.get()
        if email == "" or email == " ":
            self.label = customtkinter.CTkLabel(self, text="Please enter your email!", font = ("Helvetica",14), text_color= "red")
            self.label.grid(row=7, column = 1 ,padx=20, pady=20)
        if password != cpassword:
            self.label = customtkinter.CTkLabel(self, text="Both passwords does not match!", font = ("Helvetica",14), text_color= "red")
            self.label.grid(row=7, column = 1 ,padx=20, pady=20)
        else:
            store_password2(email,cpassword)
            self.label = customtkinter.CTkLabel(self, text="Account created Successfully", font = ("Helvetica",14), text_color= "green")
            self.label.grid(row=7, column = 1 ,padx=20, pady=20)        
            
class ToplevelWindow2(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Manager")
        self.geometry(f"{400}x{550}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)
        
        self.label = customtkinter.CTkLabel(self, text="Welcome!", font = ("Helvetica",20))
        self.label.grid(row=0, column = 1 ,padx=20, pady=20)
        
        self.button00 = customtkinter.CTkButton(self, text="Show Passwords", command=self.show_pass_button, width = 200, fg_color="yellow", text_color="black")
        self.button00.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        
        self.button000 = customtkinter.CTkButton(self, text="Delete Passwords", command=self.open_toplevel4, width = 200, fg_color="yellow", text_color="black")
        self.button000.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.toplevel_window4 = None
        
        self.button0000 = customtkinter.CTkButton(self, text="Add Password", command=self.open_toplevel3, width = 200, fg_color="yellow", text_color="black")
        self.button0000.grid(row=3, column=1, padx=20, pady=10, sticky="n")
        self.toplevel_window3 = None
        
        self.textbox = customtkinter.CTkTextbox(self,height=300, width=300,state="disabled")
        self.textbox.grid(row=4, column=1, padx=20, pady=20, sticky="n")
           
    def show_pass_button(self):
            data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
            try:
                connection = connect()
                cursor = connection.cursor()
                tablecheck()
                select_query = """SELECT * FROM accounts1 WHERE user_email = %s"""
                record_to_insert = (B_email,)
                cursor.execute(select_query, record_to_insert)
                result = cursor.fetchall()
                if cursor.rowcount == 0 :
                    self.insert("no passwords to show! ")
                    self.insert("\n\n") 
                for row in result:
                    for i in range(0,len(row)):
                        text = str(data[i] + row[i])
                        self.insert(text)
                        self.insert("\n\n")
                    self.insert("____________________________________________\n\n") 
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                print(error)
    
    def insert(self,text):
        self.textbox.configure(state="normal")
        self.textbox.insert(tk.INSERT,text)
        self.textbox.configure(state="disabled")
    
    def open_toplevel3(self):
        if self.toplevel_window3 is None or not self.toplevel_window3.winfo_exists():
            self.toplevel_window3 = ToplevelWindow3(self)
            self.toplevel_window3.attributes('-top', True)
        else:
            self.toplevel_window3.focus()
    
    def open_toplevel4(self):
        if self.toplevel_window4 is None or not self.toplevel_window3.winfo_exists():
            self.toplevel_window4 = ToplevelWindow4(self)
            self.toplevel_window4.lift()
            self.toplevel_window4.attributes('-top', True)
        else:
            self.toplevel_window4.focus()            

class ToplevelWindow3(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Manager")
        self.geometry(f"{400}x{600}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)
        
        self.label = customtkinter.CTkLabel(self, text="Add Password", font = ("Helvetica",20))
        self.label.grid(row=0, column = 1 ,padx=20, pady=20)
        
        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Email: ", width = 200,border_color="yellow")
        self.email_entry.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        self.email_entry.bind("<Return>",lambda funct1:self.pass_entry.focus())
        
        self.pass_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Password:  ", width = 200,border_color="yellow")
        self.pass_entry.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.pass_entry.bind("<Return>",lambda funct1:self.passc_entry.focus())
        
        self.Un_entry = customtkinter.CTkEntry(self, placeholder_text="Enter your username:  ", width = 200,border_color="yellow")
        self.Un_entry.grid(row=3, column=1, padx=20, pady=10, sticky="n")
        self.Un_entry.bind("<Return>",lambda funct1:self.passc_entry.focus())
        
        self.link_entry = customtkinter.CTkEntry(self, placeholder_text="Enter the url:  ", width = 200,border_color="yellow")
        self.link_entry.grid(row=4, column=1, padx=20, pady=10, sticky="n")
        self.link_entry.bind("<Return>",lambda funct1:self.passc_entry.focus())
        
        self.ap_entry = customtkinter.CTkEntry(self, placeholder_text="Enter the App Name:  ", width = 200,border_color="yellow")
        self.ap_entry.grid(row=5, column=1, padx=20, pady=10, sticky="n")
        self.ap_entry.bind(self.on_enter_pressed)
        
        self.button = customtkinter.CTkButton(self, text="Save password", command=self.on_enter_pressed, width = 200, fg_color="yellow", text_color="black")
        self.button.grid(row=7, column=1, padx=20, pady=10, sticky="n")
        
    def on_enter_pressed(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        username = self.Un_entry.get()
        url = self.link_entry.get()
        app_name = self.ap_entry.get()
        store_password(password,email,username,url,app_name)
        self.label = customtkinter.CTkLabel(self, text="Password added successfully!", font = ("Helvetica",14))
        self.label.grid(row=6, column = 1 ,padx=20, pady=20)

class ToplevelWindow4(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Manager")
        self.geometry(f"{400}x{550}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)
        
        self.label = customtkinter.CTkLabel(self, text="Delete Password", font = ("Helvetica",20))
        self.label.grid(row=0, column = 1 ,padx=20, pady=20)
        
        self.pass_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Password: ", width = 200,border_color="yellow")
        self.pass_entry.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        self.pass_entry.bind("<Return>",lambda funct1:self.app_entry.focus())
        
        self.app_entry = customtkinter.CTkEntry(self, placeholder_text="Enter the appname:  ", width = 200,border_color="yellow")
        self.app_entry.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.app_entry.bind(self.on_enter_pressed)
        
        self.button = customtkinter.CTkButton(self, text="Delete password", command=self.on_enter_pressed, width = 200, fg_color="yellow", text_color="black")
        self.button.grid(row=3, column=1, padx=20, pady=10, sticky="n")        
           
    def on_enter_pressed(self):
        password = self.pass_entry.get()
        app_name = self.app_entry.get()
        try:
            delet_password(password,app_name)
            self.label = customtkinter.CTkLabel(self, text="Password Deleted successfully!", font = ("Helvetica",14))
            self.label.grid(row=6, column = 1 ,padx=20, pady=20)
        except:
            self.label = customtkinter.CTkLabel(self, text="Invalid Credidentials!", font = ("Helvetica",14))
            self.label.grid(row=6, column = 1 ,padx=20, pady=20)   
        
class Password_Manager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry(f"{400}x{550}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)
        
        self.label1 = customtkinter.CTkLabel(self, text="Password Manager", fg_color="transparent", font = ("Helvetica",24))
        self.label1.grid(row=0, column=1, padx=20, pady=40, sticky="n")
        
        self.label2 = customtkinter.CTkLabel(self, text="Login", fg_color="transparent", font = ("Helvetica",18))
        self.label2.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        
        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Email: ", width = 200,border_color="yellow")
        self.email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.email_entry.bind("<Return>",lambda funct1:self.pass_entry.focus())
        
        self.pass_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your Master Password:  ", width = 200,border_color="yellow")
        self.pass_entry.grid(row=3, column=1, padx=20, pady=10, sticky="n")
        self.pass_entry.bind("<Return>",self.on_enter_pressed)
        
        self.label3 = customtkinter.CTkLabel(self, text="Don't have an account?", fg_color="transparent", font = ("Helvetica",15))
        self.label3.grid(row=4, column=1, padx=20, pady=10, sticky="n")
        
        self.button = customtkinter.CTkButton(self, text="Sign-up", command=self.open_toplevel, width = 200 , fg_color="yellow", text_color="black")
        self.button.grid(row=5, column=1, padx=20, pady=10, sticky="n")
        self.toplevel_window = None
        
        self.switchvalue = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(self, text="Dark Mode", command=self.switchf, variable=self.switchvalue, onvalue="on", offvalue="off",progress_color="yellow")
        self.switch.grid(row=6, column=1, padx=20, pady=10, sticky="n")
        
    def on_enter_pressed(self,event):
        self.email = self.email_entry.get()
        password = self.pass_entry.get()
        f_email = check_password(password)
        global B_email
        B_email = f_email
        try : 
            if self.email == f_email:
                self.label19 = customtkinter.CTkLabel(self, text="You are loged-in", fg_color="grey", font = ("Helvetica",15), text_color="green", width= 200)
                self.buttono = customtkinter.CTkButton(self, text="Proceed", command=self.open_toplevel2, width = 200, fg_color="yellow", text_color="black")
                self.label19.grid(row=7, column=1, padx=20, pady=10, sticky="n")
                self.buttono.grid(row=8, column=1, padx=20, pady=10, sticky="n")
                self.toplevel_window2 = None
            else:
                self.label20 = customtkinter.CTkLabel(self, text="Invalid credidentials !", fg_color="grey", font = ("Helvetica",15), text_color="red", width=200)
                self.label20.grid(row=7, column=1, padx=20, pady=10, sticky="n")
        except:
            pass
        
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.attributes('-topmost', 'true')
        else:
            self.toplevel_window.focus()
    
    def open_toplevel2(self):
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = ToplevelWindow2(self)
            self.toplevel_window2.attributes('-topmost', 'true')
        else:
            self.toplevel_window2.focus()            
        
    def switchf(self):
        state = self.switchvalue.get()
        if state == "off":
            customtkinter.set_appearance_mode("Light")
        elif state== "on":
            customtkinter.set_appearance_mode("Dark") 
            
PM = Password_Manager()
PM.mainloop()                