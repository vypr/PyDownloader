#!/bin/python

import wget
from tkinter import *
import subprocess
from pytube import YouTube
import webbrowser
from PIL import Image,ImageTk
#################################################################
depnds = input("Do you want to install dependencies?(y/n) ")
if depnds.upper() == "Y":
    subprocess.call("sudo pip install wget" , shell=True)
    subprocess.call("sudo pip install pytube" , shell=True)
    subprocess.call("yay -S tk" , shell=True)
    subprocess.call("sudo pip install pillow" , shell=True)
    subprocess.call("sudo pip install webbrowser" , shell=True)
#################################################################
root = Tk()
root.geometry("172x200")
root.title("Wget Downloader")
root.resizable(0, 0)
load = Image.open('res/2.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x= 0, y= 0)
###################################################################
def gui_wget():
    wgetgui = Tk()
    entry1 = Entry(wgetgui,width=25)
    entry1.pack()
    def wgt():
        txt = entry1.get()
        wget.download(txt)

    btn = Button(wgetgui,text="Download", command=wgt).pack()    
    wgetgui.mainloop()
##################################################################
# Yea sure, there is some weird names,but it gets the job done.
def youtube_download():
    yt = Tk()
    yt.title("YouTube-Video-Downloader")
    ytdd = Entry(yt, width = 30)
    ytdd.pack()
    def ytaudio():
        infodd = ytdd.get()
        youtube_downloaddd = YouTube(infodd)
        stream = youtube_downloaddd.streams.filter(only_audio=True, file_extension="mp3", abr='160kbps').first().download()
    def ddd():
        infodd = ytdd.get()
        youtube_downloaddd = YouTube(infodd).streams.get_highest_resolution().download()
    btn = Button(yt,text="Download-Video",command=ddd).pack()
    btn = Button(yt,text="Download-Audio",command=ytaudio).pack()     
    yt.mainloop()
####################################################################
def youtubeserch():
    yt  = Tk()
    yt.title("YoutubeSearch")

    def ytserch():
        whatlink = bar.get()
        text = ("https://www.youtube.com/results?search_query=" + whatlink)
        webbrowser.open(text)
    bar = Entry(yt, width=30)
    bar.pack()
    btn = Button(yt,text="Search", command=ytserch).pack()    
    yt.mainloop()
##################################################################
def googlesearch():
    gsearch = Tk()
    gsearch.title("GoogleSearch")

    def serch():
        whatlink = bar.get()
        text = ("https://www.google.com/search?q=" + whatlink)
        webbrowser.open(text)
    bar = Entry(gsearch, width=30)
    bar.pack()
    btn = Button(gsearch,text="Search", command=serch).pack()    
    gsearch.mainloop()


###################################################################
button_yt = Button(root,text="Youtube\ndownload",bg="black",command=youtube_download).grid(column=1, row=1)
button_Down = Button(root,text="wget\ndownload",bg="black" ,command=gui_wget).grid(column=2,row=1)
button_Google = Button(root,text="Google\nsearch", bg="black" , command=googlesearch).grid(column=2,row=2, sticky='nesw')
button_YoutubeSearch = Button(root,text="Youtube\nsearch", bg="black" , command=youtubeserch).grid(column=1,row=2 ,sticky='nesw')
root.mainloop()
