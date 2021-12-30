import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import time
import random
import playsound
import webbrowser
import pyjokes
import os
import smtplib
import ecapture
import youtube_dl
import pygame
import mixer
import wolframalpha
import skimage
import requests
import bs4
import urllib
import urllib3
import urllib.request
import sys
import cv2
import numpy as np
import json
from googlesearch.googlesearch import GoogleSearch
import subprocess
import tkinter
import operator
import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.tree import Decision
import winshell
import feedparser
import ctypes
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as dc
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import getpass
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='Enter you Spotify Client ID if you cannot do it contact me i can',
#     client_secret='Contact me if you cannot',))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

n = random.randint(0,15)

# vid = cv2.VideoCapture(0) 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        a = "good morning sir" , "good morning Adityaraj" , "good moring" , "good morning Adityaraj" , "hello sir"
        speak(random.choice(a))

    elif hour>=12 and hour<18:
        b = "good afternoon Adityaraj" , "good afternoon Adityaraj" , "good afternoon" , "good afternoon Adityaraj" , "hi sir"
        speak(random.choice(b))
    
    else:
        
        c = "good evening sir" , "good evining Adityaraj" , "good evening" , "good evening Mam" , "good evening Adityaraj"  
        speak(random.choice(c))

    speak("I am Jarvis . Please tell me how may I help you")

# it take microfone  input from the user and returns string output

def takecommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('Enter your Email ID' , 'Email ID Password')
    server.sendmail('Your Mail', to, content)
    server.close()


def Randommusic():
    path = "D:\\jarvis music random\\"
    file = os.path.join(path, random.choice(os.listdir(path)))
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


app = wolframalpha.Client("Mam Enter your Wolframalpha ID or you can contact me i can give you(alltimeinwork-fiverr)")
print("This is jarvis here!")
speak("This is Jarvis here!")    


if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takecommand().lower()

        # Logic for excecuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('windows-default')
            webbrowser.open_new_tab("https://youtube.com")
           
        elif 'open google' in query:
            webbrowser.get('windows-default')
            webbrowser.open_new_tab("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('windows-default')
            webbrowser.open_new_tab("https://stackoverflow.com")

        elif 'open fiverr' in query:
            webbrowser.get('windows-default')
            webbrowser.open_new_tab("https://www.fiverr.com")

        elif 'open gmail' in query:
            webbrowser.get('windows-default')
            webbrowser.open_new_tab("gmail.com")

        elif 'play music' in query or 'hit song' in query or 'song' or 'music' in query:
            Randommusic()

        elif 'pause music' in query or 'stop music' in query or 'stop song' in query or 'pause song' in query or 'stop the music' in query or 'pause the music' in query or 'stop the song' in query or 'pause the song' in query:
            pygame.mixer.music.pause()

        elif 'who are you' in query or 'give me your introduction' in query:
            speak("wait, i am introducing myself. my name is jarvis, i am assistant made by python programing to help other")

        elif 'who am i' in query:
            jh = "if you are speaking then , definately you are a human", "i think you are adityaraj", "you are the user who is controling me", "why should i tell you", "you don't know your name"
            speak(random.choice(jh))

        elif 'hello' in query or 'hi' in query:
            gh = "o hello sir", "hi sir", "hello sir" ,"hello", "hi" 
            speak(random.choice(gh))

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 
            print(pyjokes.get_joke())

        elif 'play video' in query:
            video_dir = 'C:\\Users\\Adityaraj\\Desktop\\JARVIS\\Jarvis viedio\\Me.mp4'
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir, video[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\Adityaraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to' in query or 'email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "Enter Email ID where you want to Send"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        # elif 'temperature' in query:
        #     res = app.query(query)
        #     speak(next(res.results).txt)

        elif 'calculate' in query or 'calculater' in query:
            speak("what should i calculate?")
            gh = takecommand().lower()
            res = app.query(gh)
            speak(next(res.results))

        elif 'thanks' in query or 'thank' in query or 'thank you' in query or 'thanks jarvis' in query or 'thanks my jarvis' in query or 'thank jarvis' in query or 'thank my jarvis' in query:
            speak("Its my pleasure, sir") 

        elif 'are you ok' in query or 'are you ok jarvis' in query:
            speak("i am ok, how are you sir?")

        if 'bye' in query or 'bye jarvis' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            break

        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Aditya. further It's a secret")

        elif "camera" in query or "take a photo" in query:
            dc.capture(1, "Jarvis Camera ", "img.jpg")

# Thanks You