import os


def formatvideo(input):
    command = "ffmpeg -i " + input + " -c:v libvpx-vp9 -b:v 1M vp9_480p.webm"
    os.system(command)
    command = "ffmpeg -i " + input + " -c:v libvpx -b:v 1M vp8_480p.webm"
    os.system(command)
    command = "ffmpeg -i " + input + " -c:v libx265 -b:v 1M  h265_480p.mp4"
    os.system(command)
    command = "ffmpeg -i " + input + " -c:v libaom-av1 -b:v 1M av1_480p.mkv"
    os.system(command)


formatvideo("output_854:480.mp4")
