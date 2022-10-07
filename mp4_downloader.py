from pytube import YouTube
import os

url = YouTube(input("Enter video URL : "))
video = url.streams.f