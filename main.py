import os.path

import pytube.query
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from os import system
from pathlib import Path


def progress(downloading_stream: pytube.Stream , __, bytes_remaining):
    initial_size = downloading_stream.filesize
    percent = round((100-(bytes_remaining/initial_size)*100), 1)
    system("cls")
    print(f"{percent}%", end="")
    print(f"[{'■'*int((round(percent, -1)/10))}{'☐'*int(10-(round(percent, -1)/10))}]")


while True:
    print("Welcome to the Video Downloader made by Jackstar-Git")
    print("-"*50)
    link = input("Enter the link to the video you would like to download: ")
    try:
        yt = YouTube(link, on_progress_callback=progress)
    except RegexMatchError:
        system("cls")
        print("This video/playlist does not exist!\n")

    else:
        break

while True:
    streams = yt.streams

    resolution = input("Please enter the resolution the video should have (\"Enter\" to skip): ")

    if resolution == "":
        filtered = streams.get_highest_resolution()
    else:
        filtered = streams.filter(resolution=f"{resolution}p", progressive=True)

    if type(filtered) == pytube.query.StreamQuery:
        if len(filtered) < 1:
            system("cls")
            print("The desired resolution doesn't exist for the selected video!\n")
        else:
            stream = filtered.first()
            break
    else:
        stream = filtered
        break

while True:
    path = input("Please enter the path the video should be downloaded to (Enter to skip): ")
    if path == "":
        path = str(Path.home() / "Desktop")
        stream.download(path)
        break
    else:
        if os.path.exists(path):
            stream.download(path)
            break
        else:
            system("cls")
            print("The entered path was not found, please try again!\n")

