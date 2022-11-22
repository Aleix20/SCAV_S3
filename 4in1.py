import os


def mosaic_video(topL, topR, botL, botR):
    command = 'ffmpeg -i ' + str(topL) + ' -i ' + str(topR) + ' -i ' + str(botL) + ' -i ' + str(botR) + ' -filter_complex \
"[0:v][1:v]hstack[t];[2:v][3:v]hstack[b];[t][b]vstack[v]; \
 [0:a][1:a][2:a][3:a]amerge=inputs=4[a]" \
-map "[v]" -map "[a]" -ac 2 -shortest 4in1.mp4'

    # Call the command line from terminal
    os.system(command)


topL = "vp8_480p.webm"
topR = "vp9_480p.webm"
botL = "h265_480p.mp4"
botR = "av1_480p.mkv"

mosaic_video(topL, topR, botL, botR)
