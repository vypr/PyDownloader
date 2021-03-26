import wget
from tkinter import *
import subprocess
from pytube import YouTube
#################################################################
subprocess.call("sudo pip install wget" , shell=True)
subprocess.call("sudo pip install pytube" , shell=True)
subprocess.call("yay -S tk" , shell=True)
#################################################################
root = Tk()
root.geometry("200x200")
root.title("Wget Downloader")
###################################################################
def gui_wget():
    wgetgui = Tk()
    wgetgui.title("Wget_GUI_Downloader")
    wgetgui.geometry("200x200")
    url = Entry(root, width=20)
    url.pack()
    btn = Button(wgetgui,text="Download", command=down)
def down():
    text = url.get()
    wget.download(text)
    root2 = Tk()
    root2.title("DONE")
    root2.geometry("100x100")
    my = Label(root2,text="DOWNLOAD IS FINISHED")
    my.pack()
    def exit2():
        exit()
    mybtn = Button(root2,text="exit", command=exit2).pack()
    root2.mainloop()
##################################################################
# Yea sure, there is some weird names,but it gets the job done.
def youtube_download():
    yt = Tk()
    yt.title("YouTube-Video-Downloader")
    ytdd = Entry(yt, width = 30)
    ytdd.pack()
    def ddd():
        infodd = ytdd.get()
        youtube_downloaddd = YouTube(infodd)
        stream = youtube_downloaddd.streams.first()
        stream.download()
    btn = Button(yt,text="Download",command=ddd).pack()    
    yt.mainloop()


###################################################################
button_yt = Button(root,text="Youtube",command=youtube_download).pack()
button_Down = Button(root,text="wget", command=gui_wget).pack()
root.mainloop()
