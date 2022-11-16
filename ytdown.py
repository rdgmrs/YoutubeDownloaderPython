from unittest import result
from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()
ROOT.withdraw()

def imput_data(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result

video_link = imput_data("Video Link", "INSIRA O LINK DO VÍDEO: ")
yt = YouTube(video_link)

print(f'Título: {yt.title}')
print(f'Views: {yt.views}')

yd = yt.streams.get_highest_resolution()

download_path = imput_data("Downloads", "INSIRA O CAMINHO DO DOWNLOAD: ")

yd.download(download_path)

messagebox.showinfo("Mensagem", "Download concluído com SUSSESSO")