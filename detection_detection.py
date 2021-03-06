# -*-coding:utf-8 -*-
import naoqi
import Image
import time
import cv2
import numpy as np
from naoqi import ALProxy
import math

def getImage(IP, PORT, flag):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2  ## VGA
    colorSpace = 11  ## RGB
    ##转换摄像头
    camProxy.setParam(18, flag)
    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    t0 = time.time()
    naoImage = camProxy.getImageRemote(videoClient)
    t1 = time.time()
    #print "acquisition delay", t1 - t0
    camProxy.unsubscribe(videoClient)
    # package.
    # Get the image size and pixel array.
    imageWidth = 640
    imageHeight = 480
    array = naoImage[6]
    # Create a PIL Image from our pixel array.
    im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
    ci = np.array(im)  ##转化成numpy格式图像
    r, g, b = cv2.split(ci)  ##opencv的图像为BGR因此需要转换一下
    ci = cv2.merge([b, g, r])
    return ci

def GetCenter(IP, PORT, flag):
    detection = 0
    x=y=0
    frame = getImage(IP, PORT, flag)
    # frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([156, 43, 46])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask3 = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_or(mask1, mask2)
    res = cv2.bitwise_or(res, mask3)
    res= cv2.medianBlur(res,5) 
    ret, binary = cv2.threshold(res, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        if d[1][1]>d[1][0]:
            a=d[1][1]
            b=d[1][0]
        else:
            a=d[1][0]
            b=d[1][1]
        if a!=0.0 and b!=0.0:
            if flag==0:
                if (a/b)>1 and (a/b)<6 and area>500:
                    detection=1
                    point=contours[i]
            if flag==1:
                if (a/b)>0.5 and (a/b)<6 and area>4000 and area>(a*b*0.6):
                    detection=1
                    point=contours[i]
    if detection==1:
        c=cv2.moments(point)
        x=c['m10']/c['m00']
        y=c['m01']/c['m00']
    while(detection==1):
        cv2.drawContours(frame,point,-1,(0,0,255),3)
        cv2.imshow('image',frame)
        if cv2.waitKey(20)&0xFF==27:
            break
    cv2.destroyAllWindows()
    return (x,y)

def GetCenter2(IP,PORT,flag):
    detection = 0
    frame = getImage(IP, PORT, flag)
    frame = cv2.pyrMeanShiftFiltering(np.asarray(frame), 10.0, 35.0)
    frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    res = cv2.inRange(hsv, lower_black, upper_black)
    res= cv2.medianBlur(res,5) 
    ret, binary = cv2.threshold(res, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x=y=0
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        if d[1][1]>d[1][0]:
            a=d[1][1]
            b=d[1][0]
        else:
            a=d[1][0]
            b=d[1][1]
        if a!=0.0 and b!=0.0 and flag==1:
            if a/b>0.5 and a/b<3 and area<25000 and area>1000:
                point=contours[i]
                detection=1
        if a!=0.0 and b!=0.0 and flag==0:
            if a/b>1 and a/b<3 and area<12000 and area>2000 and area>a*b*0.6:
                point=contours[i]
                detection=1
    if detection==1:
        c=cv2.moments(point)
        x=c['m10']/c['m00']
        y=c['m01']/c['m00']
    while(detection==1):
        cv2.drawContours(frame,point,-1,(0,0,255),3)
        cv2.imshow('image',frame)
        if cv2.waitKey(20)&0xFF==27:
            break
    cv2.destroyAllWindows()
    return (x,y)
