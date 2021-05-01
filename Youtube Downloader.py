from tkinter import *
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog, messagebox, ttk
from pytube import exceptions
import os



root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("700x500")
root.configure(bg="#fc1c1c") #fc3c3c
root.iconbitmap('ico.ico')
root.resizable(0,0)
def mp4():
        link = url.get()
        direct = filedialog.askdirectory()
        try : 
                yt = YouTube(link)
                streams = yt.streams
                stream = streams.get_highest_resolution()
                fn = yt.title+'.mp4'
                fs = stream.filesize
                stream.download(direct)
                messagebox.showinfo('Downloaded','Download Completed')        
        except exceptions.RegexMatchError :
                messagebox.showerror("Error","Invalid URL")
                
def mp3():
        link = url.get()
        direct = filedialog.askdirectory()        
        try:
                yt = YouTube(link)
                streams = yt.streams.filter(only_audio=True)
                stream = streams.first()
                stream.download(direct)
                messagebox.showinfo('Downloaded','Download Completed')
        except Exception:
                messagebox.showerror('Error','Invalid URL')
        


url = tk.Entry(root,font=("Helvetica",17),width=270,bg="#fc7c7c")

url.place(x=0,y=100)

mp4_button = tk.Button(root,text="Download MP4",font=("Helvetica",17),borderwidth=3,command=mp4)
mp4_button.place(x=250,y=190)
mp3_button = tk.Button(root,text="Download MP3",font=("Helvetica",17),borderwidth=3,command=mp3)
mp3_button.place(x=250,y=270)
 
root.mainloop()
