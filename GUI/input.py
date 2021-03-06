from fileinput import filename
from pathlib import Path
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import filedialog
from turtle import clear
from tkvideo import tkvideo
import sys
sys.path.append('Subtitle Emotions')
from OneSubtitleEmotions import OneSubtitleEmotions
from matching_uploaded_pre import match
sys.path.append('Video Emotions')
from BlurScene import *
# from win10toast import ToastNotifier
from plyer import notification
from moviepy.editor import *
MovieName=""
SubtitlesName=""
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./input_assets")
test = 'z'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PlayVideo(VidName):
    window.destroy()
    root = Tk()
    # set window title
    root.title('Video Player')
    # create label
    video_label = Label(root)
    video_label.pack()
    # read video to display on label
    player = tkvideo(VidName, video_label,
                     loop = 1, size = (700, 500))
    player.play()
    root.mainloop()

def divide_chunks(l, n):
    count = 0
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def browseMovie():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("video files",
                                                        ".mp4"),
                                                       ("all files",
                                                        ".")))
    if filename != "":
        canvas.itemconfig(MovieLabel, text=filename)
        global MovieName
        MovieName = filename
        # clip = VideoFileClip(filename) 
        # clip = clip.subclip(1, 3)
        # clip.preview()
        return filename

def browseSubtitles():
    SFileName = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        ".txt"),
                                                       ("all files",
                                                        ".")))
    if SFileName != "":
        canvas.itemconfig(SubtitleLabel, text=SFileName)
        global SubtitlesName
        SubtitlesName = SFileName
        return SFileName

def Start():
    if MovieName == "":
        canvas.itemconfig(MovieLabel, text="Please upload a Movie")
    if SubtitlesName == "":
        canvas.itemconfig(SubtitleLabel, text="Please upload Subtitles")
    else:
        result = OneSubtitleEmotions(SubtitlesName)
        Sequence_emotions= result[0]
        Time_emotions = result[1]
        print("Subtitles Emotions",Sequence_emotions)
        print("Subtitles Times",Time_emotions)

        n = 30
        Subsequences = list(divide_chunks(Sequence_emotions, n))
        SubTime = list(divide_chunks(Time_emotions, n))
        for (subE, subT) in zip(Subsequences, SubTime):
            match(Sequence_emotions,subE,subT,MovieName)
        # Violence_CSV(MovieName)


    notification.notify(title='Pruney', message='Movie is ready',app_icon=None,timeout=50)
        
 
window = Tk()

window.geometry("1440x689")
window.configure(bg = "#FFFFFF")



label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
label_file_explorer_2 = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    344.0,
    image=image_image_1
)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    195.0,
    75.0,
    image=image_image_2
)

canvas.create_rectangle(
    66.0,
    63.0,
    92.0,
    67.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    66.0,
    70.0,
    92.0,
    74.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    66.0,
    77.0,
    92.0,
    81.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1262.0,
    67.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1325.0,
    65.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    441.0,
    391.0,
    image=image_image_5
)
#hena 



canvas.create_rectangle(
    824.0,
    453.0,
    1267.0,
    510.0,
    fill="#FFFFFF",
    outline="")

#Upload Button
button_image_1 = PhotoImage(
    file=relative_to_assets("image_6.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    text="button_1 clicked",
    command=browseMovie,
    relief="flat"
)
button_1.place(
    x=1177.0,
    y=460.0,
    width=88.0,
    height=50.0
)



canvas.create_rectangle(
    824.0,
    453.0,
    1267.0,
    610.0,
    fill="#FFFFFF",
    outline="")    
button_image_2 = PhotoImage(
    file=relative_to_assets("image_6.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    text="button_2 clicked",
    command=browseSubtitles,
    relief="flat"
)
button_2.place(
    x=1177.0,
    y=550.0,
    width=88.0,
    height=50.0
)

MovieLabel = canvas.create_text(
    950.0,
    490.0,
    anchor="nw",
    text="Upload Movie File\n",
    fill="#10105E",
    font=("Roboto Thin", 14 * -1)
)

SubtitleLabel = canvas.create_text(
    950.0,
    570.0,
    anchor="nw",
    text="Upload Subtitles File\n",
    fill="#10105E",
    font=("Roboto Thin", 14 * -1)
)

button_s = Button(
    
    text="Start Filtering",
    fg="#000000",
    bg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    command= Start,
    relief="flat",
    activebackground='#6079BD'
    
)
button_s.place(
    x=960.0,
    y=630.0,
     width=200.0,
    height=20.0
 
)


window.mainloop()