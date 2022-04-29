import os
print("enter the name of the sound file. it is case sensitive on linux.")
filename = str(input(">> "))
os.system("ffmpeg -i outputvideo.avi -i {} -map 0:v -map 1:a -filter:v fps=60 -shortest videowithsound.mp4".format(filename))

