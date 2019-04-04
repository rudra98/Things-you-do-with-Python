import vlc
import time
import os

downloadsFolder = open("C:/Users/dubek/Desktop/Gaana_bajao/aaaaa.txt","r")

f =[]
if f in downloadsFolder == []:
    print("Empty")
else: 
    t_end = time.time() + 60 * 0.5
    while time.time() < t_end:
        p = vlc.MediaPLayer("C:/Users/dubek/Desktop/song/sunflower.mp3")
        p.play()

p.stop()
    