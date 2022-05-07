# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from cgitb import text
from email import message
import tkinter.font as font
from numpy import size
from regex import E, P
import pyrebase
import json
from tkinter import messagebox
from tkinter.ttk import *
from urllib3.exceptions import HTTPError as BaseHTTPError
from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import bgcolor, color

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./signin_assets")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
config = {'apiKey': "AIzaSyD3SaqfyUcu1Xnjkeaqw3ILpn_w4v5s4Fo",
  'authDomain': "pruney-4e073.firebaseapp.com",
  'databaseURL':"https://pruney-4e073.firebaseapp.com",
  'projectId': "pruney-4e073",
  'storageBucket': "pruney-4e073.appspot.com",
  'messagingSenderId': "969307424804",
  'appId': "1:969307424804:web:f6706080c47108567430b1",
  'measurementId': "G-FQRT3VDG5B"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
global my_text
global my_text_2

def login():
  
    global my_text
    global my_text_2
    email = entry_1.get()
    password = entry_2.get()
    if not email:
        print("Mail is empty")
        my_text = "Please Enter An Email"
        EmailErr()
    elif not password:
        print("Password is empty")
        my_text = ""
        EmailErr()
        my_text_2 = "Please Enter Yout Password"
        PassErr()
    else:
        try:
            signin = auth.sign_in_with_email_and_password(email, password)
            print("Sign In Was Successfull")
            on_Click()
            window.destroy()
            import input

        except Exception as e:
        #    print(e)
           error_json = e.args[1]
           error = json.loads(error_json)['error']['message']
           Err=""
           if error == "INVALID_EMAIL":
            # Err="Email invalid"
            my_text = "Invalid Email Format (@example.com)"
            EmailErr()
           elif error == "EMAIL_NOT_FOUND":
            # Err="Wrong Email"  
             my_text = "Email deosn't exist"
             EmailErr()
           elif error == "INVALID_PASSWORD":
            # Err="Wrong Password"
            my_text = ""
            EmailErr()
            my_text_2 = "Wrong Password"
            PassErr()
              
           if Err!="":
            messagebox.showerror('Sign Up Error', Err)  

def ResetPass():
 global my_text
 global my_text_2
 email = entry_1.get()
 if not email:
    my_text = "Please Enter An Email"
    EmailErr()
 else: 
    try:
      
      auth.send_password_reset_email(email)
      print("We have sent an email, check your inbox ")
      on_Click()  
  
    except Exception as e:
           print(e)
           error_json = e.args[1]
           error = json.loads(error_json)['error']['message']
           Err=""
           if error == "MISSING_EMAIL":
            # Err="Email invalid"
            my_text = "Please Enter Your Email"
            EmailErr()
           elif error == "EMAIL_NOT_FOUND":
            # Err="Wrong Email"  
             my_text = "Email deosn't exist"
             EmailErr()
           elif error == "INVALID_EMAIL":
            # Err="Email invalid"
            my_text = "Invalid Email Format (@example.com)"
            EmailErr()
           

def HomePage():
    window.destroy()
    import Home

def on_Click():
	messagebox.showinfo("Done", "Email Has Sent")


def EmailErr():
    global my_text
    my_label.config(text = my_text)

def PassErr():
    global my_text_2
    my_label_2.config(text = my_text_2)

def SignUp():
    window.destroy()
    import signup

window = Tk()

window.geometry("1440x689")
window.configure(bg = "#FFFFFF")
myFont = font.Font(family='Roboto Thin', size=10)
myFont_2 = font.Font(family='Roboto Thin', size=9)
myFontS = font.Font(family='Roboto Thin', size=13)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 689,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    689.0,
    fill="#6079BD",
    outline="")


button_image_H = PhotoImage(
    file=relative_to_assets("image_1.png"))
button_H = Button(
    image=button_image_H,
    borderwidth=0,
    highlightthickness=0,
    command=HomePage,
    relief="flat",
    bg="#6079BD",
    activebackground='#6079BD'
)
button_H.place(
    x=50.0,
    y=75.0,
    width=217.0,
    height=45.0
)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1112.0,
    443.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    376.0,
    313.0,
    image=image_image_3
)

button_s = Button(
    
    text="Sign Up",
    
    fg="#FFFFFF",
    bg="#6079BD",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=SignUp,
    activebackground='#6079BD'
    
)
button_s.place(
    x=1169.0,
    y=61.0,
    width=200.0,
    height=50.0
)
button_s['font'] = myFontS

canvas.create_rectangle(
    513.0,
    123.0,
    959.0,
    655.0,
    fill="#F7FFFF",
    outline="")

canvas.create_text(
    652.0,
    183.0,
    anchor="nw",
    text="Sign In",
    fill="#000000",
    font=("Roboto Bold", 48 * -1)
)
image_image_1 = PhotoImage(
    file=relative_to_assets("email.png"))
image_1 = canvas.create_image(
    580.0,
    295,
    image=image_image_1
)
canvas.create_text(
    601.0,
    285.0,
    anchor="nw",
    text="Email (@example.com)",
    fill="#868686",
    font=("Roboto Thin", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    736.0,
    345.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F9F8F8",
    highlightthickness=0
)
entry_1.place(
    x=565.0,
    y=313.0,
    width=342.0,
    height=47.0
)
my_label = Label( text = "",
bg="#FFFFFF",
fg="red")

my_label.place(
     x=565.0,
     y=382.0
)

image_image_p = PhotoImage(
    file=relative_to_assets("pass.png"))
image_p = canvas.create_image(
    580.0,
    415,
    image=image_image_p
)
canvas.create_text(
    601.0,
    405.0,
    anchor="nw",
    text="Password",
    fill="#868686",
    font=("Roboto Thin", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_2 = canvas.create_image(
    736.0,
    455.5,
    image=entry_image_2
)

e1_str=StringVar()
entry_2 = Entry(
    bd=0,
    bg="#F9F8F8",
    highlightthickness=0,
    show='*',
    textvariable=e1_str
)
entry_2.place(
    x=565.0,
    y=430.0,
    width=342.0,
    height=47.0
)
c_v1=IntVar(value=0)

def my_show():
    
    if(c_v1.get()==1):
        entry_2.config(show='')
    else:
        entry_2.config(show='*')

c1 = Checkbutton(text='Show Password',variable=c_v1,
	onvalue=1,offvalue=0,command=my_show,bg="#FFFFFF", activebackground='#FFFFFF')

c1.place(
    x=775.0,
    y=485.0,
    width=150.0,
    height=25.0
)

c1['font'] = myFont_2
my_label_2 = Label( 
 text = "",
 bg="#FFFFFF",
 fg="red")

my_label_2.place(
     x=565.0,
     y=490.0
)



# canvas.create_text(
#     621.0,
#     411.0,
#     anchor="nw",
#     text="Password",
#     fill="#868686",
#     font=("Roboto Thin", 14 * -1)
# )

# canvas.create_text(
#     858.0,
#     411.0,
#     anchor="nw",
#     text="Show",
#     fill="#10105E",
#     font=("Roboto", 14 * -1)
# )

button_for = Button(
    # image=button_image_1,
    text="Forget Password?",
    fg="#A31E85",
    borderwidth=0,
    highlightthickness=0,
    command=ResetPass,
    relief="flat",
    bg="#FFFFFF",
    activebackground='#FFFFFF'
)
button_for.place(
    x=678.0,
    y=510.0,
    width=117.0,
    height=45.0
)
button_for['font'] = myFont

button_image_1 = PhotoImage(
    file=relative_to_assets("Group.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat",
    bg="#FFFFFF"
)
button_1.place(
    x=628.0,
    y=557.0,
    width=217.0,
    height=55.0
)

canvas.create_text(
    709.0,
    509.0,
    anchor="nw",
    text="Sign In",
    fill="#FFFFFF",
    font=("Roboto Medium", 18 * -1)
)


canvas.create_rectangle(
    1283.0,
    91.0,
    1329.0,
    91.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()