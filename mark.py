# mark assistant project programming using python

from tkinter.filedialog import *
import urllib.request
from playsound import playsound
from tkinter import *
from tkinter.ttk import *
from time import strftime
# from ursina import *
from phue import Bridge
from ip_address import bridge_ip_address
# from ursina.prefabs.first_person_controller import FirstPersonController
import pyautogui
import PySimpleGUI as sg
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog
from googlesearch import search
import speech_recognition as sr
import time
import tkinter as tk
import requests
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
import speedtest
import turtle as tl
import turtle
import numpy as np
import random
import math
import psutil
import smtplib
import pyfirmata
import pygame as pg
import os
from turtle import *
from turtle import Screen, Turtle, mainloop
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog
from phonenumbers import geocoder
from phnumber import number
import phonenumbers
from phonenumbers import carrier
from phnumber import number
# from opencage.geocoder import OpenCageGeocoder
import requests
from googletrans import Translator
from Chess import __chess__
import psutil
import pynotifier
from sklearn import *
from train_model import __trainModel__
from plot_regression import __jsonSklearn__
from mark_sklearn import __barModel__
from plyer import notification


def __mark__():

    def __battery__():
        import psutil
        import time
        import pyttsx3
        from win10toast import ToastNotifier # also need to install win32api
        import threading

        toaster = ToastNotifier()
        x=pyttsx3.init()
        x.setProperty('volume',10)
        count = 0

        def show_notification(show_text):
            toaster.show_toast(show_text,
                                icon_path=r'C:\Users\pc\Downloads\coding_computer_pc_screen_code_icon_193925.ico',
                                duration=10)
        # loop the toaster over some period of time
        while toaster.notification_active():
            time.sleep(0.1)

        def monitor():
            while (True):
                time.sleep(10)
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = int(battery.percent)

                if percent < 90:
                    if plugged == False:
                        processThread = threading.Thread(target=show_notification, args=("Your Battery at "+str(percent)+"% Please plug the cable",))  # <- note extra ','
                        processThread.start()
                        x.say("Your battery is getting low so charge it right now")
                        x.runAndWait()
                        count = 0
                elif percent == 100:
                    if plugged == True:
                        processThread = threading.Thread(target=show_notification, args=("Charging is getting complete",))  # <- note extra ','
                        processThread.start()
                        x.say("Charging is getting complete")
                        x.runAndWait()
                elif percent == 90:
                    if plugged == True:
                        if count == 0:
                            processThread = threading.Thread(target=show_notification, args=("Your Battery at 90% Please plug out the cable",))  # <- note extra ','
                            processThread.start()
                            x.say("Your battery at 90% ")
                            x.runAndWait()
                            count = count + 1

            if __name__ == "__main__":
                monitor()

    # __battery__()

    # Error code key messanger
    def math_req():
        print('Module: math')
        print('The version of math is: ' + math.__version__)

    def spr_req():
        print('Module: speech_recognition')
        print('The version of spr is: ' + sr.__version__)

    def pyttsx3_req():
        print('Module: pyttsx3')
        print('The version is: ' + pyttsx3.__version__)

    def tl_req():
        print('Module: turtle')
        print('The version is: ' + tl.__version__)

    def ran_req():
        print('Module: random')
        print('The version is: ' + random.__version__)

    def __sysload__():
        num_per = 1
        while num_per <= 99:
            print(num_per)
            num_per = num_per + 1

        print('100%')
        time.sleep(2)

    #__sysload__()
    print('==========================================================')
    print('loading...')
    print('System is online and ready!')

    # Setting the voice settings:
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)



    def speak(text1):
        engine.say(text1)
        print('Mark: ' + text1)
        engine.runAndWait()


    # def welcomeTime():
    #     ## playsound('captured_sound.mp3')
    #     hour = datetime.now().hour
    #     tt = time.strftime('%I:%M %p')

    #     if hour >= 6 and hour < 12:
    #         speak('Good morning sir, its ' + tt)

    #     elif hour >=12 and hour < 18:
    #         speak('Good afternoon sir, its ' + tt)

    #     elif hour >=18 and hour < 24:
    #         speak('Good evening sir, its ' + tt)

    #     else:
    #         speak('Good night sir, its ' + tt)

    #     speak('How can i help you sir?')


    # welcomeTime()


    def welcomeTime():
        import time as t

        hour = datetime.now().hour
        tt = t.strftime('%I:%M %p')

        if hour >= 6 and hour < 12:
            speak('Good morning sir, its ' + tt)

        elif hour >=12 and hour < 18:
            speak('Good afternoon sir, its ' + tt)

        elif hour >=18 and hour < 24:
            speak('Good evening sir, its ' + tt)

        else:
            speak('Good night sir, its ' + tt)


        root = Tk()
        root.title('Time')

        def time():
            string = strftime('%I:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)

        label = Label(root,font=("ds-digital", 80), background='black', foreground='cyan')
        label.pack(anchor='center')
        time()

        mainloop()

        # from time import sleep
        # t.sleep(10)
        # quit()

        speak('How can i help you sir?')

    welcomeTime()


    # Taking commands from user:
    def take_command():
        try:
            with sr.Microphone() as source:
                #playsound('Notification_sound.mp3'
                print('Recognizing...')
                time.sleep(1)
                print('listening...')
                print('')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'mark' in command:
                    command = command.replace('mark', 'mark')
                    speak('Yes sir, how can i help you?')

        except sr.RequestError:
            speak("Sorry, i didn't get that")

        # except UnknownValueError:
        #     speak("Sorry sir, i didn't get that!")

        return command

    # Running user's command request:
    def __runMark__():
        command = take_command()
        print('Akshay: ' + command)
        def __query__():
            def __commands__():
                if 'introduce' in command:
                ## playsound('captured_sound.mp3')
                    speak("Hi, my name is mark, i am a visual assistant. How can i help you?")

                if 'good morning mark' in command:
                ## playsound('captured_sound.mp3')
                    speak('Good morning sir, how can i help you?')

                elif 'your name' in command:
                ## playsound('captured_sound.mp3')
                    speak('You should already know that i am mark!')

                elif 'my name' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok, what should i call you?')
                    if 'akshay' in command:
                        speak("Ok akshay, anytime you need help just ask for me.")

                elif 'hai' in command:
                ## playsound('captured_sound.mp3')
                    speak('Yes, may i help in something?')

                elif 'chess ai' in command:
                    speak('Ok sir, please choose depth as 5.')
                    subprocess.call("E:\MarkVR1\ChessEngine-main\Main.exe")

                elif 'chess multiplayer' in command:
                    speak('Ok sir, Opening chess multiplayer game interface...')
                    __chess__()

                elif 'what are you doing' in command:
                ## playsound('captured_sound.mp3')
                    speak('Nothing, except waiting for your command!')

                elif 'you born' in command:
                ## playsound('captured_sound.mp3')
                    speak('I was born in 2021 june 21.')

                elif 'who are you' in command:
                ## playsound('captured_sound.mp3')
                    speak('I am mark, a visual assistant for collaborating with users.')

                elif 'i am bored' in command:
                ## playsound('captured_sound.mp3')
                    tt = take_command()
                    tt.replace('Ok', '')
                    speak("Ok here's a joke...")
                    speak(pyjokes.get_joke())

                elif 'what can you do' in command:
                ## playsound('captured_sound.mp3')
                    speak("Here is what i can do: ")
                    print('Search google')
                    print('Open google')
                    print('Open youtube')
                    print('Search youtube')
                    print('Open amazon')
                    print('Open google classroom')
                    print('Open cmd')
                    print('Open calculator')
                    print('Open notepad')
                    print('What is the time?')
                    print('and more...')

                elif 'open google' in command:
                ## playsound('captured_sound.mp3')
                    import turtle
                    import time

                    logo = turtle.Turtle()
                    logo.color("#4285F4", "#4285F4")
                    logo.pensize(5)
                    logo.speed(20)

                    logo.hideturtle()

                    logo.forward(120)
                    logo.right(90)
                    logo.circle(-150, 50)
                    logo.color("#0F9D58")
                    logo.circle(-150, 100)
                    logo.color("#F4B400")
                    logo.circle(-150, 60)
                    logo.color("#DB4437", "#DB4437")

                    logo.begin_fill()
                    logo.circle(-150, 100)
                    logo.right(90)
                    logo.forward(50)
                    logo.right(90)
                    logo.circle(100, 100)
                    logo.right(90)
                    logo.forward(50)
                    logo.end_fill()

                    logo.begin_fill()
                    logo.color("#F4B400", "#F4B400")
                    logo.right(180)
                    logo.forward(50)
                    logo.right(90)

                    logo.circle(100, 60)
                    logo.right(90)
                    logo.forward(50)
                    logo.right(90)
                    logo.circle(-150, 60)
                    logo.end_fill()

                    logo.right(90)
                    logo.forward(50)
                    logo.right(90)
                    logo.circle(100, 60)
                    logo.color("#0F9D58", "#0F9D58")
                    logo.begin_fill()
                    logo.circle(100, 100)
                    logo.right(90)
                    logo.forward(50)
                    logo.right(90)
                    logo.circle(-150, 100)
                    logo.right(90)
                    logo.forward(50)
                    logo.end_fill()

                    logo.right(90)
                    logo.circle(100, 100)
                    logo.color("#4285F4", "#4285F4")
                    logo.begin_fill()
                    logo.circle(100, 25)
                    logo.left(115)
                    logo.forward(65)
                    logo.right(90)
                    logo.forward(42)
                    logo.right(90)
                    logo.forward(124)
                    logo.right(90)
                    logo.circle(-150, 50)
                    logo.right(90)
                    logo.forward(50)

                    logo.end_fill()
                    logo.penup()

                    logo.goto(40, 200)

                    logo.color('green')
                    speak('Welcome to google chrome...')
                    logo.write('Welcome to google chrome...', font=('JetBrains Mono', 20, 'normal'), align='center')

                    time.sleep(1)

                    # Gooogle app
                    import google
                    from google import runGoogle

                    runGoogle()


                elif 'search google' in command:
                ## playsound('captured_sound.mp3')
                    sr.Microphone(device_index=1)
                    r=sr.Recognizer()

                    r.energy_threshold=5000

                    with sr.Microphone() as source:
                        speak("What do you want to search for?")
                        print('listening...')
                        audio = r.listen(source)
                        try:
                            text = r.recognize_google(audio)
                            find = "Your search : {}".format(text)
                            speak('Searching ' + 'for : {}'.format(text))
                            url = 'https://www.google.co.in/search?q='
                            search_url = url + text
                            webbrowser.open(search_url)
                        except:
                            speak("Sorry, i can't recognize")

                elif 'youtube' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening youtube...')
                    webbrowser.open('https://www.youtube.com/')

                elif 'whatsapp' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening whatsapp...')
                    webbrowser.open('https://web.whatsapp.com/')

                elif 'mother' in command:
                ## playsound('captured_sound.mp3')
                    speak('Hi, madam my name is mark how can i help you?')

                elif 'father' in command:
                ## playsound('captured_sound.mp3')
                    speak('Hi sir, how can i help you?')

                elif 'sister' in command:
                ## playsound('captured_sound.mp3')
                    speak('Hi kid, how can i help you?')

                elif 'pinterest' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening pintrest...')
                    webbrowser.open('https://in.pinterest.com/')

                elif 'music' in command:
                ## playsound('captured_sound.mp3')
                    speak("Ok here's cute ukulele music")
                    playsound('bensound-cute.mp3')
                    speak('i have more...')
                    playsound('bensound-ukulele.mp3')
                    speak("here's the next one...")
                    playsound('bensound-smile.mp3')

                elif 'translator interface' in command:
                    def googleTranslate():
                        speak('Opening translater interface...')
                        translator = Translator()
                        speak('Please enter your text...')
                        text = input('Text: ')
                        speak("Your input is, " + text)

                        speak('Please type the language to convert the text into...')
                        translate = input('Translate to: ')
                        speak("Sir, your translation language is, " + translate)

                        OUTPUT = translator.translate(text, dest=translate)
                        speak(OUTPUT.text)

                    googleTranslate()

                elif 'game with me' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok, let us see who will win!')
                    turtle.title('Stick Game 2.0')

                    SCREENWIDTH = 750
                    SCREENHEIGHT = 600

                    MINSTICKS = 8
                    MAXSTICKS = 31

                    HUNIT = SCREENHEIGHT // 12
                    WUNIT = SCREENWIDTH // ((MAXSTICKS // 5) * 11 + (MAXSTICKS % 5) * 2)

                    SCOLOR = (63, 63, 31)

                    HCOLOR = (0, 129, 1)
                    COLOR = (227, 42, 1)

                    def randomrow():
                        return random.randint(MINSTICKS, MAXSTICKS)

                    def computerzug(state):
                        xored = state[0] ^ state[1] ^ state[2]
                        if xored == 0:
                            return randommove(state)
                        for z in range(3):
                            s = state[z] ^ xored
                            if s <= state[z]:
                                move = (z, s)
                                return move

                    def randommove(state):
                        m = max(state)
                        while True:
                            z = random.randint(0,2)
                            if state[z] > (m > 1):
                                break
                        rand = random.randint(m > 1, state[z]-1)
                        return z, rand


                    class NimModel(object):
                        def __init__(self, game):
                            self.game = game

                        def setup(self):
                            if self.game.state not in [Nim.CREATED, Nim.OVER]:
                                return
                            self.sticks = [randomrow(), randomrow(), randomrow()]
                            self.player = 0
                            self.winner = None
                            self.game.view.setup()
                            self.game.state = Nim.RUNNING

                        def move(self, row, col):
                            maxspalte = self.sticks[row]
                            self.sticks[row] = col
                            self.game.view.notify_move(row, col, maxspalte, self.player)
                            if self.game_over():
                                self.game.state = Nim.OVER
                                self.winner = self.player
                                self.game.view.notify_over()
                            elif self.player == 0:
                                self.player = 1
                                row, col = computerzug(self.sticks)
                                self.move(row, col)
                                self.player = 0

                        def game_over(self):
                            return self.sticks == [0, 0, 0]

                        def notify_move(self, row, col):
                            if self.sticks[row] <= col:
                                return
                            self.move(row, col)


                    class Stick(turtle.Turtle):
                        def __init__(self, row, col, game):
                            turtle.Turtle.__init__(self, visible=False)
                            self.row = row
                            self.col = col
                            self.game = game
                            x, y = self.coords(row, col)
                            self.shape("square")
                            self.shapesize(HUNIT/10.0, WUNIT/20.0)
                            self.speed(0)
                            self.pu()
                            self.goto(x,y)
                            self.color("white")
                            self.showturtle()

                        def coords(self, row, col):
                            packet, remainder = divmod(col, 5)
                            x = (3 + 11 * packet + 2 * remainder) * WUNIT
                            y = (2 + 3 * row) * HUNIT
                            return x - SCREENWIDTH // 2 + WUNIT // 2, SCREENHEIGHT // 2 - y - HUNIT // 2

                        def makemove(self, x, y):
                            if self.game.state != Nim.RUNNING:
                                return
                            self.game.controller.notify_move(self.row, self.col)


                    class NimView(object):
                        def __init__(self, game):
                            self.game = game
                            self.screen = game.screen
                            self.model = game.model
                            self.screen.colormode(255)
                            self.screen.tracer(False)
                            self.screen.bgcolor((147, 208, 0))
                            self.writer = turtle.Turtle(visible=False)
                            self.writer.pu()
                            self.writer.speed(0)
                            self.sticks = {}
                            for row in range(3):
                                for col in range(MAXSTICKS):
                                    self.sticks[(row, col)] = Stick(row, col, game)
                            self.display("Game Loading...")
                            self.screen.tracer(True)

                        def display(self, msg1, msg2=None):
                            self.screen.tracer(False)
                            self.writer.clear()
                            if msg2 is not None:
                                self.writer.goto(0, - SCREENHEIGHT // 2 + 48)
                                self.writer.pencolor("green")
                                self.writer.write(msg2, align="center", font=("JetBrains Mono",18))
                            self.writer.goto(0, - SCREENHEIGHT // 2 + 20)
                            self.writer.pencolor("black")
                            self.writer.write(msg1, align="center", font=("JetBrains Mono",14))
                            self.screen.tracer(True)

                        def setup(self):
                            self.screen.tracer(False)
                            for row in range(3):
                                for col in range(self.model.sticks[row]):
                                    self.sticks[(row, col)].color(SCOLOR)
                            for row in range(3):
                                for col in range(self.model.sticks[row], MAXSTICKS):
                                    self.sticks[(row, col)].color("white")
                            self.display("Your turn! Click leftmost stick to remove.")
                            self.screen.tracer(True)

                        def notify_move(self, row, col, maxspalte, player):
                            if player == 0:
                                farbe = HCOLOR
                                for s in range(col, maxspalte):
                                    self.sticks[(row, s)].color(farbe)
                            else:
                                speak('Oh man i need to think more')
                                self.display("more thinking...")
                                time.sleep(0.5)
                                speak('I am thinking')
                                self.display("mark is thinking...")
                                farbe = COLOR
                                for s in range(maxspalte-1, col-1, -1):
                                    time.sleep(0.2)
                                    self.sticks[(row, s)].color(farbe)
                                speak("Your turn! Click leftmost stick to remove.")
                                self.display("Your turn! Click leftmost stick to remove.")

                        def notify_over(self):
                            if self.game.model.winner == 0:
                                speak("Congratulations you're the winner!")
                                msg2 = "Congratulations you're the winner!"
                            else:
                                speak('Oh yeah, i win!')
                                msg2 = "Sorry, mark is the winner."
                            self.display("To play again press space bar. To clear press ESC.", msg2)

                        def clear(self):
                            if self.game.state == Nim.OVER:
                                self.screen.clear()


                    class NimController(object):

                        def __init__(self, game):
                            self.game = game
                            self.sticks = game.view.sticks
                            self.BUSY = False
                            for stick in self.sticks.values():
                                stick.onclick(stick.makemove)
                            self.game.screen.onkey(self.game.model.setup, "space")
                            self.game.screen.onkey(self.game.view.clear, "Escape")
                            speak("Press space bar to start the game")
                            self.game.view.display("Press space bar to start game")
                            self.game.screen.listen()

                        def notify_move(self, row, col):
                            if self.BUSY:
                                return
                            self.BUSY = True
                            self.game.model.notify_move(row, col)
                            self.BUSY = False


                    class Nim(object):
                        CREATED = 0
                        RUNNING = 1
                        OVER = 2
                        def __init__(self, screen):
                            self.state = Nim.CREATED
                            self.screen = screen
                            self.model = NimModel(self)
                            self.view = NimView(self)
                            self.controller = NimController(self)


                    def main():
                        mainscreen = turtle.Screen()
                        mainscreen.mode("standard")
                        mainscreen.setup(SCREENWIDTH, SCREENHEIGHT)
                        nim = Nim(mainscreen)
                        return "EVENTLOOP"

                    if __name__ == "__main__":
                        main()
                        turtle.mainloop()

                elif 'lights' in command:
                ## playsound('captured_sound.mp3')
                    speak('Turning on smart lights...')
                    def access_lights(bridge_ip_address):
                        b = Bridge(bridge_ip_address)
                        light_names_list = b.get_light_objects('name')
                        return light_names_list

                    def film_lights():
                        lights = access_lights(bridge_ip_address)
                        for light in lights:
                            lights[light].on = True
                            lights[light].hue = 7000
                            lights[light].saturation = 100

                    def danger_mode():
                        lights = access_lights(bridge_ip_address)
                        while True:
                            time.sleep(1)
                            for light in lights:
                                lights[light].on = True
                                lights[light].hue = 180
                                lights[light].saturation = 100

                            time.sleep(1)
                            for light in lights:
                                lights[light].on = True
                                lights[light].hue = 7000
                                lights[light].saturation = 100

                    if __name__ == '__main__':
                        film_lights()

                elif 'calculator' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening calculator...')
                    subprocess.call('calc.exe')

                elif 'space shooter' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok you can play with your friend on the same device!')

                    pg.font.init()
                    pg.mixer.init()

                    WIDTH, HEIGHT = 900, 500
                    WIN = pg.display.set_mode((WIDTH, HEIGHT))
                    pg.display.set_caption("Space Fight 2.0!")

                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)
                    RED = (0, 163, 0)
                    YELLOW = (255, 255, 0)
                    GREEN = (0, 163, 0)

                    BORDER = pg.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

                    #BULLET_HIT_SOUND = pg.mixer.Sound('assets/Grenade+1.mp3')
                    #BULLET_FIRE_SOUND = pg.mixer.Sound('assets/Gun+Silencer.mp3')

                    HEALTH_FONT = pg.font.SysFont('JetBrains Mono', 26)
                    WINNER_FONT = pg.font.SysFont('JetBrains Mono', 90)

                    FPS = 60
                    VEL = 5
                    BULLET_VEL = 15
                    MAX_BULLETS = 3
                    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 55

                    YELLOW_HIT = pg.USEREVENT + 1
                    RED_HIT = pg.USEREVENT + 2

                    YELLOW_SPACESHIP_IMAGE = pg.image.load(os.path.join('assets', 'spaceship_green.png'))
                    YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

                    RED_SPACESHIP_IMAGE = pg.image.load(os.path.join('assets', 'spaceship_yellow.png'))
                    RED_SPACESHIP = pg.transform.rotate(pg.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

                    SPACE = pg.transform.scale(pg.image.load(os.path.join('assets', 'background-black.png')), (WIDTH, HEIGHT))


                    def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
                        WIN.blit(SPACE, (0, 0))
                        pg.draw.rect(WIN, BLACK, BORDER)

                        red_health_text = HEALTH_FONT.render(
                            "Player 2 health: " + str(red_health), 1, GREEN)
                        yellow_health_text = HEALTH_FONT.render(
                            "Player 1 health: " + str(yellow_health), 1, YELLOW)
                        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
                        WIN.blit(yellow_health_text, (10, 10))

                        WIN.blit(RED_SPACESHIP, (yellow.x, yellow.y))
                        WIN.blit(YELLOW_SPACESHIP, (red.x, red.y))

                        for bullet in red_bullets:
                            pg.draw.rect(WIN, RED, bullet)

                        for bullet in yellow_bullets:
                            pg.draw.rect(WIN, YELLOW, bullet)

                        pg.display.update()


                    def yellow_handle_movement(keys_pressed, yellow):
                        if keys_pressed[pg.K_a] and yellow.x - VEL > 0:  # LEFT
                            yellow.x -= VEL
                        if keys_pressed[pg.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
                            yellow.x += VEL
                        if keys_pressed[pg.K_w] and yellow.y - VEL > 0:  # UP
                            yellow.y -= VEL
                        if keys_pressed[pg.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
                            yellow.y += VEL


                    def red_handle_movement(keys_pressed, red):
                        if keys_pressed[pg.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
                            red.x -= VEL
                        if keys_pressed[pg.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
                            red.x += VEL
                        if keys_pressed[pg.K_UP] and red.y - VEL > 0:  # UP
                            red.y -= VEL
                        if keys_pressed[pg.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
                            red.y += VEL


                    def handle_bullets(yellow_bullets, red_bullets, yellow, red):
                        for bullet in yellow_bullets:
                            bullet.x += BULLET_VEL
                            if red.colliderect(bullet):
                                pg.event.post(pg.event.Event(RED_HIT))
                                yellow_bullets.remove(bullet)
                            elif bullet.x > WIDTH:
                                yellow_bullets.remove(bullet)

                        for bullet in red_bullets:
                            bullet.x -= BULLET_VEL
                            if yellow.colliderect(bullet):
                                pg.event.post(pg.event.Event(YELLOW_HIT))
                                red_bullets.remove(bullet)
                            elif bullet.x < 0:
                                red_bullets.remove(bullet)


                    def draw_winner(text):
                        draw_text = WINNER_FONT.render(text, 1, WHITE)
                        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                                            2, HEIGHT/2 - draw_text.get_height()/2))
                        pg.display.update()
                        pg.time.delay(5000)


                    def main():
                        red = pg.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                        yellow = pg.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

                        red_bullets = []
                        yellow_bullets = []

                        red_health = 10
                        yellow_health = 10

                        clock = pg.time.Clock()
                        run = True
                        while run:
                            clock.tick(FPS)
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    run = False
                                    pg.quit()

                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                                        bullet = pg.Rect(
                                            yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                                        yellow_bullets.append(bullet)
                                        #BULLET_FIRE_SOUND.play()

                                    if event.key == pg.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                                        bullet = pg.Rect(
                                            red.x, red.y + red.height//2 - 2, 10, 5)
                                        red_bullets.append(bullet)
                                        #BULLET_FIRE_SOUND.play()

                                if event.type == RED_HIT:
                                    red_health -= 1
                                    #BULLET_HIT_SOUND.play()

                                if event.type == YELLOW_HIT:
                                    yellow_health -= 1
                                    #BULLET_HIT_SOUND.play()

                            winner_text = ""
                            if red_health <= 0:
                                winner_text = "Player 2 Wins!"

                            if yellow_health <= 0:
                                winner_text = "Player 1 Wins!"

                            if winner_text != "":
                                draw_winner(winner_text)
                                break

                            keys_pressed = pg.key.get_pressed()
                            yellow_handle_movement(keys_pressed, yellow)
                            red_handle_movement(keys_pressed, red)

                            handle_bullets(yellow_bullets, red_bullets, yellow, red)

                            draw_window(red, yellow, red_bullets, yellow_bullets,
                                        red_health, yellow_health)

                        main()


                    if __name__ == "__main__":
                        main()

                elif 'space adventures' in command:
                ## playsound('captured_sound.mp3')
                    speak('So i am the alien with my alien friends!')
                    pg.font.init()

                    WIDTH, HEIGHT = 750, 750
                    WIN = pg.display.set_mode((WIDTH, HEIGHT))
                    pg.display.set_caption("Space Shooter Tutorial")

                    # Load images
                    RED_SPACE_SHIP = pg.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
                    GREEN_SPACE_SHIP = pg.image.load(os.path.join("assets", "spaceship_green.png"))
                    BLUE_SPACE_SHIP = pg.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

                    # Player player
                    YELLOW_SPACE_SHIP = pg.image.load(os.path.join("assets", "spaceship_yellow.png"))

                    # Lasers
                    RED_LASER = pg.image.load(os.path.join("assets", "pixel_laser_red.png"))
                    GREEN_LASER = pg.image.load(os.path.join("assets", "pixel_laser_green.png"))
                    BLUE_LASER = pg.image.load(os.path.join("assets", "pixel_laser_blue.png"))
                    YELLOW_LASER = pg.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

                    # Background
                    BG = pg.transform.scale(pg.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

                    class Laser:
                        def __init__(self, x, y, img):
                            self.x = x
                            self.y = y
                            self.img = img
                            self.mask = pg.mask.from_surface(self.img)

                        def draw(self, window):
                            window.blit(self.img, (self.x, self.y))

                        def move(self, vel):
                            self.y += vel

                        def off_screen(self, height):
                            return not(self.y <= height and self.y >= 0)

                        def collision(self, obj):
                            return collide(self, obj)


                    class Ship:
                        COOLDOWN = 30

                        def __init__(self, x, y, health=100):
                            self.x = x
                            self.y = y
                            self.health = health
                            self.ship_img = None
                            self.laser_img = None
                            self.lasers = []
                            self.cool_down_counter = 0

                        def draw(self, window):
                            window.blit(self.ship_img, (self.x, self.y))
                            for laser in self.lasers:
                                laser.draw(window)

                        def move_lasers(self, vel, obj):
                            self.cooldown()
                            for laser in self.lasers:
                                laser.move(vel)
                                if laser.off_screen(HEIGHT):
                                    self.lasers.remove(laser)
                                elif laser.collision(obj):
                                    obj.health -= 10
                                    self.lasers.remove(laser)

                        def cooldown(self):
                            if self.cool_down_counter >= self.COOLDOWN:
                                self.cool_down_counter = 0
                            elif self.cool_down_counter > 0:
                                self.cool_down_counter += 1

                        def shoot(self):
                            if self.cool_down_counter == 0:
                                laser = Laser(self.x, self.y, self.laser_img)
                                self.lasers.append(laser)
                                self.cool_down_counter = 1

                        def get_width(self):
                            return self.ship_img.get_width()

                        def get_height(self):
                            return self.ship_img.get_height()


                    class Player(Ship):
                        def __init__(self, x, y, health=100):
                            super().__init__(x, y, health)
                            self.ship_img = YELLOW_SPACE_SHIP
                            self.laser_img = YELLOW_LASER
                            self.mask = pg.mask.from_surface(self.ship_img)
                            self.max_health = health

                        def move_lasers(self, vel, objs):
                            self.cooldown()
                            for laser in self.lasers:
                                laser.move(vel)
                                if laser.off_screen(HEIGHT):
                                    self.lasers.remove(laser)
                                else:
                                    for obj in objs:
                                        if laser.collision(obj):
                                            objs.remove(obj)
                                            if laser in self.lasers:
                                                self.lasers.remove(laser)

                        def draw(self, window):
                            super().draw(window)
                            self.healthbar(window)

                        def healthbar(self, window):
                            pg.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
                            pg.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


                    class Enemy(Ship):
                        COLOR_MAP = {
                                    "red": (RED_SPACE_SHIP, RED_LASER),
                                    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                                    "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                                    }

                        def __init__(self, x, y, color, health=100):
                            super().__init__(x, y, health)
                            self.ship_img, self.laser_img = self.COLOR_MAP[color]
                            self.mask = pg.mask.from_surface(self.ship_img)

                        def move(self, vel):
                            self.y += vel

                        def shoot(self):
                            if self.cool_down_counter == 0:
                                laser = Laser(self.x-20, self.y, self.laser_img)
                                self.lasers.append(laser)
                                self.cool_down_counter = 1


                    def collide(obj1, obj2):
                        offset_x = obj2.x - obj1.x
                        offset_y = obj2.y - obj1.y
                        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

                    def main():
                        run = True
                        FPS = 60
                        level = 0
                        lives = 5
                        main_font = pg.font.SysFont("comicsans", 50)
                        lost_font = pg.font.SysFont("comicsans", 60)

                        enemies = []
                        wave_length = 5
                        enemy_vel = 1

                        player_vel = 5
                        laser_vel = 5

                        player = Player(300, 630)

                        clock = pg.time.Clock()

                        lost = False
                        lost_count = 0

                        def redraw_window():
                            WIN.blit(BG, (0,0))
                            # draw text
                            lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
                            level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

                            WIN.blit(lives_label, (10, 10))
                            WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

                            for enemy in enemies:
                                enemy.draw(WIN)

                            player.draw(WIN)

                            if lost:
                                lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
                                WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

                            pg.display.update()

                        while run:
                            clock.tick(FPS)
                            redraw_window()

                            if lives <= 0 or player.health <= 0:
                                lost = True
                                lost_count += 1

                            if lost:
                                if lost_count > FPS * 3:
                                    run = False
                                else:
                                    continue

                            if len(enemies) == 0:
                                level += 1
                                wave_length += 5
                                for i in range(wave_length):
                                    enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                                    enemies.append(enemy)

                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    quit()

                            keys = pg.key.get_pressed()
                            if keys[pg.K_LEFT] and player.x - player_vel > 0: # left
                                player.x -= player_vel
                            if keys[pg.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
                                player.x += player_vel
                            if keys[pg.K_UP] and player.y - player_vel > 0: # up
                                player.y -= player_vel
                            if keys[pg.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
                                player.y += player_vel
                            if keys[pg.K_SPACE]:
                                player.shoot()

                            for enemy in enemies[:]:
                                enemy.move(enemy_vel)
                                enemy.move_lasers(laser_vel, player)

                                if random.randrange(0, 2*60) == 1:
                                    enemy.shoot()

                                if collide(enemy, player):
                                    player.health -= 10
                                    enemies.remove(enemy)
                                elif enemy.y + enemy.get_height() > HEIGHT:
                                    lives -= 1
                                    enemies.remove(enemy)

                            player.move_lasers(-laser_vel, enemies)

                    def main_menu():
                        title_font = pg.font.SysFont("comicsans", 70)
                        run = True
                        while run:
                            WIN.blit(BG, (0,0))
                            title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
                            WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
                            pg.display.update()
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    run = False
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    main()
                        pg.quit()


                    main_menu()

                elif 'screenshot' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening screenshot app...')
                    subprocess.call('SnippingTool.exe')

                elif 'current location' in command:
                ## playsound('captured_sound.mp3')
                    Key = "c682145a35c8464dbbfeeb58c6329c1a"
                    r = requests.get('https://get.geojs.io/')

                    ## Country display on screen according to phnum
                    locate_number = phonenumbers.parse(number)
                    location = geocoder.description_for_number(locate_number, "en")
                    print("##Country note: " + location)

                    ## print IP Address
                    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                    ipAdd = ip_request.json()['ip']
                    print('IP Address: ' + ipAdd)


                    ## get service provider
                    service_provider = phonenumbers.parse(number)
                    print("Mobile net: " + carrier.name_for_number(service_provider,  "en"))

                    ## Details of location information
                    URL = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_request = requests.get(URL)
                    geo_data = geo_request.json()
                    # print(geo_data)

                    print("latitude: " + geo_data['latitude'])
                    print("longtitude: " + geo_data['longitude'])

                    speak("Sir you are in, " + geo_data['city'])
                    speak("city of " + geo_data['region'])
                    speak("which is the state of " + geo_data['country'])

                elif 'ai mode' in command:
                    speak('Please wait, loading models sir...')
                    from train_model import __trainModel__
                    from mark_sklearn import __barModel__
                    from plot_regression import __jsonSklearn__
                    from time import sleep

                    def __analyse__():
                        speak('Training model of mark SK lern...')
                        # __barModel__()
                        speak('Detecting accuracy of model...')
                        sleep(2)
                        # __jsonSklearn__
                        speak('Model is up to date sir!')

                        def __train__():
                            num_per = 1
                            while num_per <= 99:
                                print(num_per)
                                num_per = num_per + 1

                            print('100%')

                        __train__()

                    __analyse__()

                    sleep(2)

                    __trainModel__()

                elif 'notepad' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening notepad...')
                    subprocess.call('notepad.exe')

                elif 'command prompt' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening command prompt...')
                    subprocess.call('cmd.exe')

                elif 'image' in command:
                ## playsound('captured_sound.mp3')
                    speak('Please type the path of the image...')
                    file = input('Type the file path: ')
                    img = Image.open(file)
                    img.show()

                elif 'internet speed test' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok, checking internet speed test...')
                    test = speedtest.Speedtest()

                    speak("Loading server list...")
                    test.get_servers()
                    speak('Choosing best server...')
                    best = test.get_best_server()

                    speak(f"Found: {best['host']} located in {best['country']}")

                    speak('Performing download test...')
                    download_result = test.download()

                    speak('Performing upload test...')
                    upload_result = test.upload()

                    ping = test.results.ping

                    print('Bites per second (download): ', download_result)
                    print('Bites per second (upload)', upload_result)
                    print('Total result: ', ping)

                    speak('Bites per second (download): ', download_result)
                    speak('Bites per second (upload)', upload_result)
                    speak('Total result: ', ping)


                elif 'play' in command:
                ## playsound('captured_sound.mp3')
                    song = command.replace('play', '')
                    speak('playing ' + song)
                    pywhatkit.playonyt(song)

                elif 'more volume' in command:
                ## playsound('captured_sound.mp3')
                    speak('Volume has increased by 1.')
                    pyautogui.press('volumeup')

                elif 'less volume' in command:
                ## playsound('captured_sound.mp3')
                    speak('Volume has decreased by 1.')
                    pyautogui.press('volumedown')

                elif 'mute volume' in command:
                ## playsound('captured_sound.mp3')
                    speak('Volume is muted.')
                    pyautogui.press('volumemute')

                elif 'story' in command:
                ## playsound('captured_sound.mp3')
                    speak('What story?')
                    story = command.replace('story', '')
                    speak('Ok opening ' + story)

                if 'email to my mum' in command:
                ## playsound('captured_sound.mp3')
                    speak('Please type the message in the placeholder below...')
                    message = input('Message: ')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('pythoncode970@gmail.com', 'Akki7&Buddi')
                    server.sendmail('pythoncode970@gmail.com',
                                    'kadalisravanthi007@gmail.com',
                                    message)
                    speak('Email successfully sent!')

                if 'email to my dad' in command:
                ## playsound('captured_sound.mp3')
                    speak('Please type the message in the placeholder below...')
                    message = input('Message: ')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('pythoncode970@gmail.com', 'Akki7&Buddi')
                    server.sendmail('pythoncode970@gmail.com',
                                    'kadalinaresh007@gmail.com',
                                    message)
                    speak('Email successfully sent!')

                elif 'email to my mom' in command:
                ## playsound('captured_sound.mp3')
                    speak('Please type the message in the placeholder below...')
                    message = input('Message: ')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('pythoncode970@gmail.com', 'pythoncode@2010')
                    server.sendmail('pythoncode970@gmail.com',
                                    'kadalisravanthi007@gmail.com', message)
                    speak('Email successfully sent!')

                # elif 'weather' in command:
                # ## playsound('captured_sound.mp3')
                #     speak('Ok, please type the location of the place in the window given.')
                #     def getWeather(canvas):
                #         city = textField.get()
                #         api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
                #
                #         # Requests for json data
                #         json_data = requests.get(api).json()
                #         condition = json_data['weather'][0]['main']
                #         temp = int(json_data['main']['temp'] - 273.15)
                #         min_temp = int(json_data['main']['temp_min'] - 273.15)
                #         max_temp = int(json_data['main']['temp_max'] - 273.15)
                #         pressure = json_data['main']['pressure']
                #         humidity = json_data['main']['humidity']
                #         wind = json_data['wind']['speed']
                #         sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                #         sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
                #
                #         # Getting info and conditions
                #         final_info = condition + "\n" + str(temp) + "°C"
                #         final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                #         label1.config(text = final_info)
                #         label2.config(text = final_data)
                #
                #         return 'Thank you for using Weather App!'
                #
                #
                #     # Creating area and perimeter for the window
                #     canvas = tk.Tk()
                #     canvas.geometry("600x500")
                #     canvas.title("Weather App")
                #     f = ("JetBrains Mono Light", 15)
                #     t = ("JetBrains Mono Light", 20)
                #
                #     # Adjusting size of the window
                #     textField = tk.Entry(canvas, justify='center', width=20, font=t)
                #     textField.pack(pady=20)
                #     textField.focus()
                #     textField.bind('<Return>', getWeather)
                #
                #     # Getting labels and running the app
                #     label1 = tk.Label(canvas, font=t)
                #     label1.pack()
                #     label2 = tk.Label(canvas, font=f)
                #     label2.pack()
                #     canvas.mainloop()

                elif 'weather' in command:
                    # import WeatherApp_withicons
                    # from WeatherApp_withicons import weatherApp
                    #
                    # app = watherApp()
                    # app()

                    import tkinter as tk
                    import requests
                    from PIL import Image, ImageTk

                    def weatherApp():
                        app = tk.Tk()

                        HEIGHT = 500
                        WIDTH = 600

                        def format_response(weather_json):
                            try:
                                city = weather_json['name']
                                conditions = weather_json['weather'][0]['description']
                                temp = weather_json['main']['temp']
                                final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
                            except:
                                final_str = 'There was a problem retrieving that information'
                            #final_str = 'hello'
                            return final_str


                        def get_weather(city):
                            weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
                            url = 'https://api.openweathermap.org/data/2.5/weather'
                            params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units':'imperial'}
                            response = requests.get(url, params=params)
                            print(response.json())
                            weather_json = response.json()

                            results['text'] = format_response(response.json())

                            icon_name = weather_json['weather'][0]['icon']
                            open_image(icon_name)

                        def open_image(icon):
                            size = int(lower_frame.winfo_height()*0.25)
                            img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
                            weather_icon.delete("all")
                            weather_icon.create_image(0,0, anchor='nw', image=img)
                            weather_icon.image = img

                        C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
                        background_image= tk.PhotoImage(file='./landscape.png')
                        background_label = tk.Label(app, image=background_image)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        C.pack()

                        frame = tk.Frame(app,  bg='#42c2f4', bd=5)
                        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
                        #frame_window = C.create_window(100, 40, window=frame)

                        textbox = tk.Entry(frame, font=40)
                        textbox.place(relwidth=0.65, relheight=1)

                        submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(textbox.get()))
                        #submit.config(font=)
                        submit.place(relx=0.7, relheight=1, relwidth=0.3)

                        lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
                        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

                        bg_color = 'white'
                        results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
                        results.config(font=40, bg=bg_color)
                        results.place(relwidth=1, relheight=1)

                        weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
                        weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


                        app.mainloop()

                    weatherApp()


                elif 'who' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('who', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'when' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('when', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'why' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('why', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'where' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('where', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'what' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('what', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'math problems' in command:
                ## playsound('captured_sound.mp3')
                    speak("Here's what i found")
                    webbrowser.open('https://study.com/academy/subj/math.html')

                elif 'search for' in command:
                ## playsound('captured_sound.mp3')
                    query = command.replace('search for', '')
                    info = wikipedia.summary(query, 1)
                    speak(info)

                elif 'tell me about' in command:
                ## playsound('captured_sound.mp3')
                    person = command.replace('tell me about', '')
                    info = wikipedia.summary(person, 1)
                    speak(info)

                elif 'bored' in command:
                ## playsound('captured_sound.mp3')
                    speak('Do you want me to tell a story?')
                    ct = take_command
                    ct.replace('Yes', '')

                elif 'time' in command:
                ## playsound('captured_sound.mp3')
                    speak('Sir, the time is ' + strftime('%I:%M:%S %p'))
                    root = Tk()
                    root.title('Time')

                    def time():
                        string = strftime('%I:%M:%S %p')
                        label.config(text=string)
                        label.after(1000, time)

                    label = Label(root,font=("ds-digital", 80), background='black', foreground='cyan')
                    label.pack(anchor='center')
                    time()

                    mainloop()


                elif 'link' in command:
                ## playsound('captured_sound.mp3')
                    speak('What do you want to search for?')
                    ct = take_command()
                    search_link = ct.replace('search for ', '')
                    speak("Here's what i found")
                    for i in search(search_link,
                                    tld='co.in',
                                    lang='en',
                                    tbs='0',
                                    num=10,
                                    stop=10,
                                    pause=2.0):

                        print(i)

                elif 'joke' in command:
                ## playsound('captured_sound.mp3')
                    speak("Ok here's a joke...")
                    speak(pyjokes.get_joke())

                # elif 'battery' in command:
                # ## playsound('captured_sound.mp3')
                #     battery = psutil.sensors_battery()
                #     percent = str(battery.percent)
                #     plugged = battery.power_plugged
                #     plugged = "plugged in" if plugged else "not plugged in"
                #     speak(f'Battery is {percent}%, the laptop is {plugged}')

                elif 'battery' in command:
                    import psutil
                    from plyer import notification
                    import time

                    battery = psutil.sensors_battery()

                    per=battery.percent
                    title = 'Battery percentage'
                    speak("Sir "+str(per)+"% battery is remaining")
                    notification.notify(title=title,
                                    message=str(per)+"% battery remaining",
                                    app_icon=r"C:\Users\pc\Downloads\coding_computer_pc_screen_code_icon_193925.ico",
                                    timeout=10,
                                    toast=True)

                elif 'discord' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening discord...')
                    webbrowser.open('https://discord.com/channels/@me/835445338789642241')

                elif 'turn on the light' in command:
                ## playsound('captured_sound.mp3')
                    import time
                    from time import sleep
                    import datetime
                    speak('Ok turning on the light sir...')
                    board = pyfirmata.Arduino('COM4')
                    led = board.get_pin('d:13:o')

                    while True:
                        led.write(1) # 1 means HiGH
                        time.sleep(1)
                        led.write(0) # 0 means LOW
                        time.sleep(1)

                elif 'amazon prime' in command:
                ## playsound('captured_sound.mp3')
                    speak('Opening amazon prime movies...')
                    webbrowser.open('https://www.primevideo.com/ref=av_auth_return_redir')

                elif 'online buying service' in command:
                    speak('Opening Amazon website...')
                    webbrowser.open('https://www.amazon.in/')

                elif 'run arduino voice controlled bot' in command:
                ## playsound('captured_sound.mp3')
                    speak("Ok sir here's the file path")
                    path = "E:\Akshay_Python\Data_Analysis\Python_IDLE_checkpoints\Python_Analysis\Python_Apps\Python_Programming\ARDUINO_Python_Programs\ARDUINO_VOICE_CONTROLLED_BOT\ARDUINO_VOICE_CONTROLLED_BOT.ino"
                    print(path)
                    speak('Please click on the upload button in the arduino IDE')


                # elif 'find current location' in command:
                #     engine = pyttsx3.init()
                #     voices = engine.getProperty('voices')
                #     engine.setProperty('voice', voices[0].id)

                #     r = requests.get('https://get.geojs.io/')
                #     ip_requests = requests.get('https://get.geojs.io/v1/ip.json')

                #     ipAdd = ip_requests.json()['ip']
                #     print(ipAdd)

                #     url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                #     geo_requests = requests.get(url)
                #     geo_data = geo_requests.json()
                #     # print(geo_data)
                #     engine.say('Sir you are in, ')
                #     engine.runAndWait()
                #     speak(geo_data['city'])

                #     print(geo_data['region'])

                #     print(geo_data['country'])

                #     print(geo_data['timezone'])


                elif 'cartoon photo' in command:
                ## playsound('captured_sound.mp3')
                    speak('Sure, why not, just select your file!')
                    photo = askopenfilename()
                    img = cv2.imread(photo)

                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    grey = cv2.medianBlur(grey, 5)
                    edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

                    #cartoonize
                    color = cv2.bilateralFilter(img, 9, 250, 250)
                    cartoon = cv2.bitwise_and(color, color, mask=edges)

                    cv2.imshow("Image", img)
                    cv2.imshow("Cartoon", cartoon)

                    #save
                    cv2.imwrite("cartoon.png", cartoon)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                elif 'colors' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok sir showing colourful designs')
                    def main():
                        peacecolors = ("red",  "orange", "yellow",
                                    "green", "blue",
                                    "indigo", "violet")

                        reset()
                        Screen()
                        up()
                        goto(-320,-195)
                        width(70)

                        for pcolor in peacecolors:
                            color(pcolor)
                            down()
                            forward(640)
                            up()
                            backward(640)
                            left(90)
                            forward(66)
                            right(90)

                        width(25)
                        color("white")
                        goto(0,-170)
                        down()

                        circle(170)
                        left(90)
                        forward(340)
                        up()
                        left(180)
                        forward(170)
                        right(45)
                        down()
                        forward(170)
                        up()
                        backward(170)
                        left(90)
                        down()
                        forward(170)
                        up()

                        goto(0,300) # vanish if hideturtle() is not available ;-)
                        return "Done!"

                    if __name__ == "__main__":
                        main()
                        mainloop()

                elif 'rgb calculator' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok sir showing RGB Calculator')
                    class ColorTurtle(Turtle):
                        def __init__(self, x, y):
                            Turtle.__init__(self)
                            self.shape("square")
                            self.resizemode("user")

                            self.shapesize(3,3,5)
                            self.pensize(10)
                            self._color = [0,0,0]
                            self.x = x
                            self._color[x] = y
                            self.color(self._color)
                            self.speed(0)
                            self.left(90)
                            self.pu()
                            self.goto(x,0)
                            self.pd()
                            self.sety(1)
                            self.pu()
                            self.sety(y)
                            self.pencolor("gray25")
                            self.ondrag(self.shift)

                        def shift(self, x, y):
                            self.sety(max(0,min(y,1)))
                            self._color[self.x] = self.ycor()
                            self.fillcolor(self._color)
                            setbgcolor()

                    def setbgcolor():
                        screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

                    def main():
                        global screen, red, green, blue
                        screen = Screen()
                        screen.delay(0)
                        screen.setworldcoordinates(-1, -0.3, 3, 1.3)

                        red = ColorTurtle(0, .5)
                        green = ColorTurtle(1, .5)
                        blue = ColorTurtle(2, .5)
                        setbgcolor()

                        writer = Turtle()
                        writer.ht()
                        writer.pu()
                        writer.goto(1,1.15)
                        writer.write("RGB Calculator",align="center",font=("JetBrains Mono",30))
                        return "Thank you for using RGB Calculator!"


                    if __name__ == "__main__":
                        msg = main()
                        print(msg)
                        mainloop()

                elif 'Corona cases' in command:
                ## playsound('captured_sound.mp3')
                    speak('Ok sir here are the corona cases')
                    def getCovidData():
                        api = "https://disease.sh/v3/covid-19/all"
                        json_data = requests.get(api).json()
                        total_cases = str(json_data['cases'])
                        total_deaths = str(json_data['deaths'])
                        today_cases = str(json_data['todayCases'])
                        today_deaths = str(json_data['todayDeaths'])
                        today_recovered = str(json_data['todayRecovered'])
                        updated_at = json_data['updated']
                        date = datetime.datetime.fromtimestamp(updated_at/1e3)
                        label.config(text = "Total Cases(#1): "+total_cases+
                            "\n"+"Total Deaths(#1): "+total_deaths+
                            "\n"+"Today Cases(#2): "+today_cases+
                            "\n"+"Today Deaths(#2): "+today_deaths+
                            "\n"+"Today Recovered: "+today_recovered)

                        label2.config(text = date)

                    canvas = tk.Tk()
                    canvas.geometry("700x400")
                    canvas.title("Corona Tracker App")

                    f = ("JetBrains Mono", 15)

                    button = tk.Button(canvas, font = f, text = "Load", command = getCovidData)
                    button.pack(pady = 20)

                    label = tk.Label(canvas, font = f)
                    label.pack(pady=20)

                    label2 = tk.Label(canvas, font = 8)
                    label2.pack()
                    getCovidData()

                    canvas.mainloop()

                elif 'camera' in command:
                # playsound('captured_sound.mp3')
                    speak('Opening camera sir')
                    # Defining CreateWidgets() function to create necessary tkinter widgets
                    def createwidgets():
                        root.feedlabel = Label(root, bg="steelblue", fg="white", text="WEBCAM FEED", font=('JetBrains Mono',20))
                        root.feedlabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

                        root.cameraLabel = Label(root, bg="steelblue", borderwidth=3, relief="groove")
                        root.cameraLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

                        root.saveLocationEntry = Entry(root, width=55, textvariable=destPath)
                        root.saveLocationEntry.grid(row=3, column=1, padx=10, pady=10)

                        root.browseButton = Button(root, width=10, text="BROWSE", command=destBrowse)
                        root.browseButton.grid(row=3, column=2, padx=10, pady=10)

                        root.captureBTN = Button(root, text="CAPTURE", command=Capture, bg="LIGHTBLUE", font=('JetBrains Mono',15), width=20)
                        root.captureBTN.grid(row=4, column=1, padx=10, pady=10)

                        root.CAMBTN = Button(root, text="STOP CAMERA", command=StopCAM, bg="LIGHTBLUE", font=('JetBrains Mono',15), width=13)
                        root.CAMBTN.grid(row=4, column=2)

                        root.previewlabel = Label(root, bg="steelblue", fg="white", text="IMAGE PREVIEW", font=('JetBrains Mono',20))
                        root.previewlabel.grid(row=1, column=4, padx=10, pady=10, columnspan=2)

                        root.imageLabel = Label(root, bg="steelblue", borderwidth=3, relief="groove")
                        root.imageLabel.grid(row=2, column=4, padx=10, pady=10, columnspan=2)

                        root.openImageEntry = Entry(root, width=55, textvariable=imagePath)
                        root.openImageEntry.grid(row=3, column=4, padx=10, pady=10)

                        root.openImageButton = Button(root, width=10, text="BROWSE", command=imageBrowse)
                        root.openImageButton.grid(row=3, column=5, padx=10, pady=10)

                        # Calling ShowFeed() function
                        ShowFeed()

                    # Defining ShowFeed() function to display webcam feed in the cameraLabel;
                    def ShowFeed():
                        # Capturing frame by frame
                        ret, frame = root.cap.read()

                        if ret:
                            # Flipping the frame vertically
                            frame = cv2.flip(frame, 1)

                            # Displaying date and time on the feed
                            cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'), (20,30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,255))

                            # Changing the frame color from BGR to RGB
                            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

                            # Creating an image memory from the above frame exporting array interface
                            videoImg = Image.fromarray(cv2image)

                            # Creating object of PhotoImage() class to display the frame
                            imgtk = ImageTk.PhotoImage(image = videoImg)

                            # Configuring the label to display the frame
                            root.cameraLabel.configure(image=imgtk)

                            # Keeping a reference
                            root.cameraLabel.imgtk = imgtk

                            # Calling the function after 10 milliseconds
                            root.cameraLabel.after(10, ShowFeed)
                        else:
                            # Configuring the label to display the frame
                            root.cameraLabel.configure(image='')

                    def destBrowse():
                        # Presenting user with a pop-up for directory selection. initialdir argument is optional
                        # Retrieving the user-input destination directory and storing it in destinationDirectory
                        # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
                        destDirectory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

                        # Displaying the directory in the directory textbox
                        destPath.set(destDirectory)

                    def imageBrowse():
                        # Presenting user with a pop-up for directory selection. initialdir argument is optional
                        # Retrieving the user-input destination directory and storing it in destinationDirectory
                        # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
                        openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")

                        # Displaying the directory in the directory textbox
                        imagePath.set(openDirectory)

                        # Opening the saved image using the open() of Image class which takes the saved image as the argument
                        imageView = Image.open(openDirectory)

                        # Resizing the image using Image.resize()
                        imageResize = imageView.resize((640, 480), Image.ANTIALIAS)

                        # Creating object of PhotoImage() class to display the frame
                        imageDisplay = ImageTk.PhotoImage(imageResize)

                        # Configuring the label to display the frame
                        root.imageLabel.config(image=imageDisplay)

                        # Keeping a reference
                        root.imageLabel.photo = imageDisplay

                    # Defining Capture() to capture and save the image and display the image in the imageLabel
                    def Capture():
                        # Storing the date in the mentioned format in the image_name variable
                        image_name = datetime.now().strftime('%d-%m-%Y %H-%M-%S')

                        # If the user has selected the destination directory, then get the directory and save it in image_path
                        if destPath.get() != '':
                            image_path = destPath.get()
                        # If the user has not selected any destination directory, then set the image_path to default directory
                        else:
                            messagebox.showerror("ERROR", "NO DIRECTORY SELECTED TO STORE IMAGE!!")

                        # Concatenating the image_path with image_name and with .jpg extension and saving it in imgName variable
                        imgName = image_path + '/' + image_name + ".jpg"

                        # Capturing the frame
                        ret, frame = root.cap.read()

                        # Displaying date and time on the frame
                        cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'), (430,460), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,255))

                        # Writing the image with the captured frame. Function returns a Boolean Value which is stored in success variable
                        success = cv2.imwrite(imgName, frame)

                        # Opening the saved image using the open() of Image class which takes the saved image as the argument
                        saved_image = Image.open(imgName)

                        # Creating object of PhotoImage() class to display the frame
                        saved_image = ImageTk.PhotoImage(saved_image)

                        # Configuring the label to display the frame
                        root.imageLabel.config(image=saved_image)

                        # Keeping a reference
                        root.imageLabel.photo = saved_image

                        # Displaying messagebox
                        if success :
                            messagebox.showinfo("SUCCESS", "IMAGE CAPTURED AND SAVED IN " + imgName)


                    # Defining StopCAM() to stop WEBCAM Preview
                    def StopCAM():
                        # Stopping the camera using release() method of cv2.VideoCapture()
                        root.cap.release()

                        # Configuring the CAMBTN to display accordingly
                        root.CAMBTN.config(text="START CAMERA", command=StartCAM)

                        # Displaying text message in the camera label
                        root.cameraLabel.config(text="OFF CAM", font=('JetBrains Mono',70))

                    def StartCAM():
                        # Creating object of class VideoCapture with webcam index
                        root.cap = cv2.VideoCapture(0)

                        # Setting width and height
                        width_1, height_1 = 640, 480
                        root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width_1)
                        root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height_1)

                        # Configuring the CAMBTN to display accordingly
                        root.CAMBTN.config(text="STOP CAMERA", command=StopCAM)

                        # Removing text message from the camera label
                        root.cameraLabel.config(text="")

                        # Calling the ShowFeed() Function
                        ShowFeed()

                    # Creating object of tk class
                    root = tk.Tk()

                    # Creating object of class VideoCapture with webcam index
                    root.cap = cv2.VideoCapture(0)

                    # Setting width and height
                    width, height = 640, 480
                    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

                    # Setting the title, window size, background color and disabling the resizing property
                    root.title("Pycam")
                    root.geometry("1340x700")
                    root.resizable(True, True)
                    root.configure(background = "dark green")

                    # Creating tkinter variables
                    destPath = StringVar()
                    imagePath = StringVar()

                    createwidgets()
                    root.mainloop()

                elif 'video' in command:
                # playsound('captured_sound.mp3')
                    def run_video():
                        speak('please enter the path sir!')
                        path = input('Enter path: ')
                        cap = cv2.VideoCapture(path)

                        while (True):
                            ret, frame = cap.read()
                            cv2.imshow('Media Player',frame)
                            if (cv2.waitKey(1) & 0xFF == ord('q')):
                                break

                    run_video()

                elif 'connect webcam' in command:
                    ipAdd = "192.168.1.3:8080"
                    url = "https://192.168.1.3:8080/"
                    print("Ip_Address: " + ipAdd)
                    speak('Ok sir, redirecting you to webcam facility and features')
                    webbrowser.open(url)

                elif 'detect my hands' in command:
                    speak('Ok sir, detecting your hands...')
                    import cv2
                    import mediapipe as mp

                    mp_drawing = mp.solutions.drawing_utils
                    mp_hands = mp.solutions.hands

                    cap = cv2.VideoCapture(0)

                    with mp_hands.Hands(
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:
                        while cap.isOpened():
                            success, image = cap.read()

                            if not success:
                                print("Ignoring empty camera frame.")
                                # If loading a video, use 'break' instead of 'continue'.
                                continue

                            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

                            image.flags.writeable = False
                            results = hands.process(image)

                            # Draw the hand annotations on the image.
                            image.flags.writeable = True
                            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                            if results.multi_hand_landmarks:
                                for hand_landmarks in results.multi_hand_landmarks:
                                    mp_drawing.draw_landmarks(
                                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                            cv2.imshow('Hand detector', image)

                            if cv2.waitKey(5) & 0xFF == 'q':
                                quit()

                        cap.release()

                elif 'detect my face' in command:
                    speak('Ok sir detecting your face...')
                    import cv2
                    import numpy as np
                    import dlib
                    import mediapipe as mp

                    mp_drawing = mp.solutions.drawing_utils
                    mp_hands = mp.solutions.hands

                    cap = cv2.VideoCapture(0)

                    detector = dlib.get_frontal_face_detector()
                    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

                    while True:
                        _, frame = cap.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        faces = detector(gray)
                        for face in faces:
                            x1 = face.left()
                            y1 = face.top()
                            x2 = face.right()
                            y2 = face.bottom()
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

                            landmarks = predictor(gray, face)

                            for n in range(0, 68):
                                x = landmarks.part(n).x
                                y = landmarks.part(n).y
                                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

                        cv2.imshow("Face Detector", frame)

                        key = cv2.waitKey(10)
                        if key & 0xFF == ord('q'):
                            break

                elif 'login notes' in command:
                # playsound('captured_sound.mp3')
                    speak('Ok sir opening web app login notes interface!')
                    from website import create_app

                    app = create_app()

                    if __name__ == '__main__':
                        app.run(debug=True)

                elif 'thank you' in command:
                ## playsound('captured_sound.mp3')
                    speak('No problem, anytime sir!')

                elif 'shutdown' in command:
                    ## playsound('captured_sound.mp3')
                    speak('Ok, shutting down assistant...')
                    quit()

                # elif 'stop' in command:
                # ## playsound('captured_sound.mp3')
                #     speak('Ok, shutting down assistant...')
                #     quit()

                # elif 'close' or 'stop' in command:
                # ## playsound('captured_sound.mp3')
                #     speak('Ok, shutting down assistant...')
                #     quit()

            __commands__()


        __query__()


    while True:
        __runMark__()

    # Sample running sensor indicator (SRSI)
    msp = True

    while msp == True:
        print('MARK 40.1.1')

    # if __name__ == '__main__':
    #     __mark__()
