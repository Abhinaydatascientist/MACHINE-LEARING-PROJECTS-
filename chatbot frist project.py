# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:04:39 2023

@author: Lenovo
"""

import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    try:
        with sr.Microphone() as mic:
            print('Listening...')
            listening.adjust_for_ambient_noise(mic)
            audio = listening.listen(mic)
            cmd = listening.recognize_google(audio)
            cmd = cmd.lower()
            if 'Abhi' in cmd:
                cmd = cmd.replace('Abhi', '')
                print(cmd)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        cmd = ''
    except sr.RequestError:
        print("Sorry, I'm currently unavailable.")
        cmd = ''
    return cmd

def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('Playing ' + song)
        pk.playonyt(song)

run()
