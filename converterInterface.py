from tkinter import *
from tkinter.filedialog import askopenfile
import os

path = ''

window = Tk()
# Window
window.title("Codecs converter")
window.geometry("700x400")
window.resizable(False, False)

# Input for the file path
window.filelocation = Entry(window, width=60)
window.filelocation.insert(0, 'Path to the input video file')
window.filelocation.configure(state='disabled', borderwidth=1)
window.filelocation.place(x=20, y=80)

# Button to select mp4 file
window.buttons = Button(window, text="Select mp4 file", command=lambda: mfileOpen())
window.buttons.place(x=500, y=75)


# Method to search for mp4 file and save path
def mfileOpen():
    FILEOPENOPTIONS = dict(defaultextension=".mp4", initialdir="/home",
                           filetypes=[('mp4 file', '*.mp4')])
    window.file1 = askopenfile(**FILEOPENOPTIONS)
    window.filelocation.configure(state='normal')
    window.filelocation.delete(0, 'end')
    window.filelocation.insert(0, window.file1.__getattribute__("name"))
    window.filelocation.configure(state='readonly')
    global path
    path = window.file1.__getattribute__("name")
    disableActivateButtons(path)


def disableActivateButtons(path):
    if path != '':
        window.buttonVP8.configure(state="normal")
        window.buttonVP9.configure(state="normal")
        window.buttonH265.configure(state="normal")
        window.buttonAV1.configure(state="normal")
        window.button240p.configure(state="normal")
        window.button360p.configure(state="normal")
        window.button480p.configure(state="normal")
        window.button720p.configure(state="normal")
    if path == '':
        window.buttonVP8.configure(state="disabled")
        window.buttonVP9.configure(state="disabled")
        window.buttonH265.configure(state="disabled")
        window.buttonAV1.configure(state="disabled")
        window.button240p.configure(state="disabled")
        window.button360p.configure(state="disabled")
        window.button480p.configure(state="disabled")
        window.button720p.configure(state="disabled")

def converter_codec(opt):
    if opt == 1:
        if os.path.exists("vp8_out.webm"):
            os.remove("vp8_out.webm")
        command = "ffmpeg -i " + str(path) + " -c:v libvpx -b:v 1M vp8_out.webm"

    elif opt == 2:
        if os.path.exists("vp9_out.webm"):
            os.remove("vp9_out.webm")
        command = "ffmpeg -i " + str(path) + " -c:v libvpx-vp9 -b:v 1M vp9_out.webm"

    elif opt == 3:
        if os.path.exists("h265_out.mp4"):
            os.remove("h265_out.mp4")
        command = "ffmpeg -i " + str(path) + " -c:v libx265 -b:v 1M  h265_out.mp4"

    else:
        if os.path.exists("av1_out.mkv"):
            os.remove("av1_out.mkv")
        command = "ffmpeg -i " + str(path) + " -c:v libaom-av1 -b:v 1M av1_out.mkv"
    os.system(command)


def scale(input_file, width, height):
    if os.path.exists("output_" + str(width) + ":" + str(height) + ".mp4"):
        os.remove("output_" + str(width) + ":" + str(height) + ".mp4")
    # Command that allow us to scale to any size
    command = 'ffmpeg -i ' + input_file + ' -vf scale=' + str(width) + ':' \
              + str(height) + ',setsar=1:1 output_' + str(width) + ':' + str(height) + '.mp4'
    os.system(command)


def converter_video(opt):
    if opt == 1:
        width = 1280
        height = 720
    elif opt == 2:
        width = 854
        height = 480
    elif opt == 3:
        width = 640
        height = 360
    else:
        width = 320
        height = 240
    scale(path, width, height)

window.label = Label(window, text="Video codecs: ")
window.label.place(x=50, y=305)
window.buttonVP8 = Button(window, text="VP8", width=3, command=lambda: converter_codec(1))
window.buttonVP8.place(x=150, y=300)
window.buttonVP9 = Button(window, text="VP9", width=3, command=lambda: converter_codec(2))
window.buttonVP9.place(x=250, y=300)
window.buttonH265 = Button(window, text="H265", width=3, command=lambda: converter_codec(3))
window.buttonH265.place(x=350, y=300)
window.buttonAV1 = Button(window, text="AV1", width=3, command=lambda: converter_codec(4))
window.buttonAV1.place(x=450, y=300)

window.label = Label(window, text="Video scale: ")
window.label.place(x=50, y=205)
window.button240p = Button(window, text="240p", width=3, command=lambda: converter_video(1))
window.button240p.place(x=150, y=200)
window.button360p = Button(window, text="360p", width=3, command=lambda: converter_video(2))
window.button360p.place(x=250, y=200)
window.button480p = Button(window, text="480p", width=3, command=lambda: converter_video(3))
window.button480p.place(x=350, y=200)
window.button720p = Button(window, text="720p", width=3, command=lambda: converter_video(4))
window.button720p.place(x=450, y=200)
disableActivateButtons(path)

window.mainloop()
