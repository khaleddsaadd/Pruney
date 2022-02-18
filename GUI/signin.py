
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./signin_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x689")
window.configure(bg = "#FFFFFF")


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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    190.0,
    75.0,
    image=image_image_1
)

canvas.create_rectangle(
    60.0,
    73.0,
    95.0,
    74.0,
    fill="#000000",
    outline="")

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

canvas.create_text(
    1276.0,
    65.0,
    anchor="nw",
    text="Sign Up",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

canvas.create_rectangle(
    513.0,
    123.0,
    959.0,
    605.0,
    fill="#F7FFFF",
    outline="")

canvas.create_text(
    652.0,
    193.0,
    anchor="nw",
    text="Sign In",
    fill="#000000",
    font=("Roboto Bold", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    736.0,
    337.5,
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

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    736.0,
    418.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F9F8F8",
    highlightthickness=0
)
entry_2.place(
    x=565.0,
    y=394.0,
    width=342.0,
    height=47.0
)

canvas.create_text(
    621.0,
    329.0,
    anchor="nw",
    text="Email",
    fill="#868686",
    font=("Roboto Thin", 14 * -1)
)

canvas.create_text(
    621.0,
    411.0,
    anchor="nw",
    text="Password",
    fill="#868686",
    font=("Roboto Thin", 14 * -1)
)

canvas.create_text(
    858.0,
    411.0,
    anchor="nw",
    text="Show",
    fill="#10105E",
    font=("Roboto", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=628.0,
    y=497.0,
    width=217.0,
    height=45.0
)

canvas.create_text(
    709.0,
    509.0,
    anchor="nw",
    text="Sign In",
    fill="#FFFFFF",
    font=("Roboto Medium", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    597.0,
    337.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    597.0,
    421.0,
    image=image_image_5
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