from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
from pytube import YouTube
from threading import *
from tkinter.messagebox import askyesno

# video size container
file_size = 0

# thread for downloading video
def downThread():
    thread = Thread(target=downloader)
    thread.start()

# monitor the process of downloading
def progress(chunk, file_handle, remaining):
    global download_status
    file_downloaded = file_size - remaining
    per = (file_downloaded / file_size) * 100
    download_status.config(text='{:00.0f} downloaded'.format(per))

def downloader():
    global file_size, download_status
    download_button.config(state=DISABLED)
    download_status.place( x=230, y=250)
    try:
        url1 = url.get()
        path = askdirectory()
        yt = YouTube(url1, on_progress_callback=progress)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        file_size = video.filesize
        video.download(path)
        download_status.config(text='Download Finish...')
        res = askyesno("YouTube Video Downloader", "Do you want to Download another video ?")
        if res == 1:
            url.delete(0, END)
            download_button.config(state=NORMAL)
            download_status.config(text=' ')
        else:
            root.destroy()
    except Exception as e :
        download_status.config(text='Failed! There is an Error')

root = Tk() # main window handler
root.geometry('600x400') # size of the window
root.iconbitmap('logo.ico') # logo of the window

root.title("YouTube Video Downloader") # title of window
root['bg'] = 'white' # color of window
root.resizable(0, 0) # disable maximize button

img = Image.open('logo.ico') # logo image
img = img.resize((80, 80), Image.ANTIALIAS) # resize the logo image
img = ImageTk.PhotoImage(img) # load the image for tkinter
head = Label(root, image=img) # main image or icon as a heading
head.pack()

enter_url = Label(root, text='Enter Url: ', bg='white')
enter_url.config(font=('Verdana', 15))
enter_url.place(x=5, y=120)

url = Entry(root, width=35, border=1, relief=SUNKEN, font=('Verdana', 15))
url.place(x=125, y=123)

download_button_img = Image.open('download.png')
download_button_img = download_button_img.resize((200, 150), Image.ANTIALIAS)
download_button_img = ImageTk.PhotoImage(download_button_img)

download_button = Button(root, width=150, height=150, bg='white', relief=FLAT,
activebackground='red', command=downThread)
download_button.config(image=download_button_img)
download_button.place(x=250, y=170)
download_status = Label(root, text="Please wait...", font=('Verdana', 15), bg = 'white')
root.mainloop()