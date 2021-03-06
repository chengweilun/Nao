#using UTF-8
import math
import naoqi
import numpy
import cv2
import moveto
import detection
import posinit
from naoqi import ALProxy
import grab
import drop

IP = "169.254.44.123" # set your Ip adress here
PORT = 9559

high=480
wide=640

def main(IP,PORT):
    posinit.posinit()
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say("Hello!")
    center=detection.GetCenter(IP,PORT,0)
    print center
    while (center[0] > (wide/2+30)) or (center[0] < (wide/2-30)):
        if center==(0,0):
            center=detection.GetCenter(IP,PORT,0)
            print center
            continue
        if center[0] > (wide/2+30):
            moveto.move(0,-2,0)
            tts.say("found the bar,check the x position")
            print "found the bar,check the x position"
        elif center[0] < (wide/2-30):
            moveto.move(0,2,0)
            tts.say("found the bar,check the x position")
            print "found the bar,check the x position"
        center=detection.GetCenter(IP,PORT,0)
        print center
    center=detection.GetCenter(IP,PORT,0)
    print "Found the bar,move forward"
    tts.say("found the bar,moveforward")
    while center[1]<440 and center!=(0,0):
        if center[1]<380:
            step=6
        else:
            step=3
        moveto.move(step,0,0)
        center=detection.GetCenter(IP,PORT,0)
        print center
    center=detection.GetCenter(IP,PORT,0)
    while center[1]<440 and center!=(0,0):
        if center[1]<380:
            step=6
        else:
            step=3
        moveto.move(step,0,0)
        center=detection.GetCenter(IP,PORT,0)
        print center
    center=detection.GetCenter(IP,PORT,0)
    counter=0
    while center!=(0,0):
        if counter==2:
            moveto.move(0,0,0.2)
            counter=0
        moveto.move(3,0,0)
        counter=counter+1
        center=detection.GetCenter(IP,PORT,0)

    moveto.move(0,0,0.1)
    tts.say("change camera")
    print "change camera"
    posinit.posinit() 
    center=detection.GetCenter(IP,PORT,1)
    while (center[0] > (wide/2+5)) or (center[0] < (wide/2-15)):
        if center==(0,0):
            center=detection.GetCenter(IP,PORT,1)
            print center
            continue
        if center[0] > (wide/2+5):
            moveto.move(0,-1,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the position"
        elif center[0] < (wide/2-15):
            moveto.move(0,1,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the position"
        center=detection.GetCenter(IP,PORT,1)
        print center
    center=detection.GetCenter(IP,PORT,1)
    while center[1]<160:
        moveto.move(2,0,0)
        center=detection.GetCenter(IP,PORT,1)
        print center
    center=detection.GetCenter(IP,PORT,1)
    while (center[0] > (wide/2)) or (center[0] < (wide/2-20)):
        if center==(0,0):
            center=detection.GetCenter(IP,PORT,1)
            print center
            continue
        if center[0] > (wide/2):
            moveto.move(0,-1,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the position"
        elif center[0] < (wide/2-20):
            moveto.move(0,1,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the position"
        center=detection.GetCenter(IP,PORT,1)
        print center
    print "ready to grab"
    tts.say("ready to grab")
    grab.grab(IP,PORT)

    moveto.move(-6,0,0)
    moveto.move(0,0,1)
    posinit.posinit2(0,25)
    center=detection.GetCenter2(IP,PORT,0)
    print center
    while center[0]<300 or center[0]>340:
        if center[0]<300:
            theta=0.1
        else:
            theta=-0.1
        moveto.move(0,0,theta)
        center=detection.GetCenter2(IP,PORT,0)
        print center
    while center[1]<420 and center!=(0,0):
        moveto.move(3,0,0)
        center=detection.GetCenter2(IP,PORT,0)
        print center
    center=detection.GetCenter2(IP,PORT,1)
    if center==(0,0):
        moveto.move(0,0,0.3)
    print center
    while center[1]<290 or center[1]>330:
        if center[1]<290:
            moveto.move(3,0,0)
        if center[1]>330:
            moveto.move(-3,0,0)
        center=detection.GetCenter2(IP,PORT,1)
        print center
    center=detection.GetCenter2(IP,PORT,1)
    print center
    while center[0]<290 or center[0]>310:
        if center[0]<290:
            theta=0.1
        else:
            theta=-0.1
        moveto.move(0,0,theta)
        center=detection.GetCenter2(IP,PORT,1)
        print center
    while center[1]<290 or center[1]>330:
        if center[1]<290:
            moveto.move(3,0,0)
        if center[1]>330:
            moveto.move(-3,0,0)
        center=detection.GetCenter2(IP,PORT,1)
        print center
    drop.drop(IP,PORT)

if __name__ == '__main__':
    IP="169.254.44.123"
    PORT=9559
    naoImage = main(IP, PORT)

