print("initialization ongoing wait for some seconds")
from subprocess import call  ## Used for swapping new process for Voice control Mode
import speech_recognition as sr  ## For identifying or classifying the speech or recognise the speech

import serial
import cv2    ## webcam library
import numpy as np  ## Multidimentional Array or mathematical cal. purpose of code
import time  # showing the date & time live
import os    # Operating system os for rasberripy i.e. interact with the python code exicution
from cvzone.HandTrackingModule import HandDetector  # inbuild gesture Library import
import RPi.GPIO as GPIO  # to refer the GPIO through the rest of your script

GPIO.setwarning(False)   # setwarning i.e. stop & starting programe again
r = sr.Recogniser()      # r variable and from sr we use Recogniser
text = {}
text1 = {}
print("Land")
print("All library Succsfully import")
GPIO.setmode(GPIO.BOARD)   ## GPIO of Rasberi pi
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
button = 16      # Power Button for jesture = 1 & voice = 0
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  ## PUll Up/Down supply voltage till GPIO set to defined value

video_capture = cv2.VideoCapture(0)
detect = HandDetector(detectionCon=0.5)  ## execution time

while True:
    button_state = GPIO.input(button)  ##button variable & taking GPIO IO form Pi
    # print("Button States")
    # print("button state")
    if button_state == False:
        ret, frame = video_capture.read()   ## Capturing the vedio live inret, frame variable
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)    ## Resizing the image according to our Convenience On X & Y Axis
        #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        hand, small_frame = detect.findHands(small_frame)  ## Variable and tracking hand points from 1
        #print("Open_Camera")
        if hand:
            hand1 = hand[0]
            fingers1 = detect.fingersUp(hand1)  ## only one hand
            print(fingers1)


            def areEqual(fingers1, arr2):   ## Function areequal and use for loop for the Fingure range from 0 to 5
                for i in range(0, 5):
                    if (fingers1[i] != arr2[i]):
                        return False

                return True


            if (areEqual(fingers1, [1, 1, 1, 1, 1])):  ## All fingers is on high or up mode then start command
                print("start")
                GPIO.output(10, True)     ## for triping the relay for motor 1
                GPIO.output(8, False)  # 1
                GPIO.output(11, True)     ## triping relay for motor 2
                GPIO.output(12, False)

            if (areEqual(fingers1, [1, 1, 0, 0, 0])):  ## according to indexes of fingers the coommand will exicute
                print("Left")                          ## two finger for left command
                GPIO.output(10, True)
                GPIO.output(8, False)
                GPIO.output(11, False)  # 2
                GPIO.output(12, True)

            if (areEqual(fingers1, [1, 0, 1, 1, 1])):  ## for right command 4 middle fingers is use
                print("right")
                GPIO.output(10, False)
                GPIO.output(8, True)
                GPIO.output(11, True)
                GPIO.output(12, False)  # 3

            if (areEqual(fingers1, [0, 0, 0, 0, 0])):  ## for stop command  ALl fingers get close
                print("Stop")
                GPIO.output(10, False)
                GPIO.output(8, False)  # 4
                GPIO.output(11, False)
                GPIO.output(12, False)

            if (areEqual(fingers1, [0, 1, 1, 0, 0])):  ## for back command TWO FIngers are use
                print("Back")
                GPIO.output(10, True)
                GPIO.output(8, True)    # 5
                GPIO.output(11, False)
                GPIO.output(12, False)

            if (areEqual(fingers1, [0, 1, 1, 0, 0])):  ## left side 2 fingers are used
                print("Back")
                GPIO.output(10, False)  # 6
                GPIO.output(8, True)
                GPIO.output(11, False)
                GPIO.output(12, True)

            if (areEqual(fingers1, [1, 1, 1, 0, 0])):  # 3 Fingers are use for back command
                print("Back")
                GPIO.output(10, False)
                GPIO.output(8, True)
                GPIO.output(11, False)  # 7
                GPIO.output(12, True)

            cv2.imshow('Video', small_frame)
            if (cv2.waitKey(2) == 210): ## Allow to wait for specific time untill 210 milliseconds completed
                cv2.destroyAllWindows()  ## after delay ditroying all windows
                break

        else:
            def listen1():  ## class listen1
                with sr.microphone(device_index=1) as source:  ## Microphone index 1
                    r.adjust_for_ambient_noise(source)  ## Extra onather noise
                    print("say sSomething")  ## master command
                    call(["espeak", "-s140"])  ## from call library import espeak at -s140
                    audio = r.listen(source)  ## stored in audio command
                    print("got it");  ## master coomand
                return audio


        def voice(audio1): ## audio1 is the class for another voice command
            try:                                       ## Exception file handelling , trial and error
                text1 = r.recognize_google(audio1)     ## text1 is variable stored the recognition
                # call("espeak "+ text, shell = True)
                print("you said:  " + text1);  ## printout the output
                return text1
            except sr.UnknownValueError:   ## onather voice came or module does not understnd the our voice command
                call(["espeak", ".s140 = ven +18 .2", ])  ## from call library import espeak at -s140 ven +18.2 is an internal part of library or library internal part
                print("Google Speech Recognition could not undestand")
                return 0
            except sr.RequestError as c:
                print("Could not requet result from Google  ");
                return 0


        def main(text):
            text = voice(audio1);
            text = {}


        # if__name__ == '__main__':
        if __name__ == "__main__": ## when prg is in only main the only next programe under the is main function is work
            while (1):  ## while true
                audio1 = listen1()
                text = voice(audio1)
                if text == "hello":
                    text = {}
                    call(["espeak", "-s140      -ven+18 -z", "Okay Master , Wating for Your Command"])
                elif 'forward' in text:
                    text = {}
                    GPIO.output(10, True)
                    GPIO.output(8, False)
                    GPIO.output(11, True)
                    GPIO.output(12, False)
                    # GPIO.output(led, 1)
                    call(["espeak", "-s140      -ven+18 -z", "okay Sir, Start MOve forword"])
                    print("Forword");

                elif 'back' in text:
                    text = {}
                    # GPIO.output(led, 0)
                    call(["espeak", "-s140      -ven+18 -z", "okay Sir, Start Move backword"])

                    GPIO.output(10, False)
                    GPIO.output(8, True)
                    GPIO.output(11, False)
                    GPIO.output(12, True)
                    print("Back");

                elif 'left' in text:
                    text = {}
                    GPIO.output(10, True)
                    GPIO.output(8, False)
                    GPIO.output(11, False)
                    GPIO.output(12, True)

                    call(["espeak", "-s140      -ven+18 -z", " okay sir, start move leftside "])
                    print("left");

                elif 'right' in text:

                    text = {}
                    GPIO.output(10, True)
                    GPIO.output(8, False)
                    GPIO.output(11, True)
                    GPIO.output(12, False)
                    call(["espeak", "-s140      -ven+18 -z", "okay sir, start move rightside"])
                    print("right");

                elif 'stop' in text:
                    GPIO.output(10, False)
                    GPIO.output(8, False)
                    GPIO.output(11, False)
                    GPIO.output(12, False)
                    call(["espeak", "-s140      -ven+18 -z", "okay sir, Stop Movement"])
                    print("stop");
                    text = {}
                else:
                    call(["espeak", "-s140      -ven+18 -z", "Unknown Command please repeate"])






