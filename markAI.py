from mark import __mark__
import pyttsx3
from plyer import notification
# from win10toast import ToastNotifier
# import os
# import subprocess

def __markAI__():
    # voice settings
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    def speak(audio):
        engine.say(audio)
        print('Mark: ' + audio)
        engine.runAndWait()

    def __notify__():
        title = "Mark"
        message = "Mark is currently activated!"
        notification.notify(title=title,
                        message=message,
                        app_icon=r"E:\MarkVR1\App_icon\coding_computer_pc_screen_code_icon_193925.ico",
                        timeout=10,
                        toast=True)

        speak(message)

    def __runCustomized__():
        speak('Please enter the password sir...')
        engine_st = input('Password: ')
        if engine_st == "mark@4044":
            __notify__()
            __mark__()

    def __runProgram__():
        speak('Loading assistant...')
        __notify__()
        __mark__()

        if engine_st == "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe":
            speak('Ok sir, terminating assistant!')


    # subprocess.call("E:\MarkVR1\Mark_AI\Mark_AI.lnk")

    __runProgram__()

__markAI__()
