import cv2
import csv
from datetime import datetime
from datetime import date
from playsound import playsound
import numpy as np
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT , initial = GPIO.HIGH)
GPIO.setup(33,GPIO.OUT , initial = GPIO.LOW)
GPIO.setup(8,GPIO.OUT , initial = GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(40,GPIO.HIGH)
GPIO.output(33,GPIO.LOW)
sleep(1)
g=8
while g>0:
    GPIO.output(40,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)
    sleep(0.1)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(8,GPIO.HIGH)
    sleep(0.1)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(33, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(40,GPIO.HIGH)
    sleep(0.1)
    g=g-1

#playsound("Welcome.mp3")#just audio to make it look cool 
def value(x):
    x='1'
    print (x)
    return x
    
mohid=0
abram=0
odd=2
x='0'
en = '1'
#playsound('initialize.mp3')#just audio to make it look cool
p='/media/pi/ATTENDANCE/' +str(date.today())+'.csv'  #create a file with todays date
#if a file with todays date exists modify that otherwise just create one 
try:
    open(p ,'r',newline='') 
except:
    with open(p ,'w',newline='') as fp:
        a = csv.writer(fp,delimiter=',')
        data =[[ 'check','name','time']]  #put in check name and time on top of the excel sheet for easier understanding
        a.writerows(data)

#to mark attendence i call this function
def markAttendance(name):
    o=name
    name ='Check In        '+name
    with open(p,'r+') as f:
        myDataList = f.readlines()
        nameList= []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            #the below if statement will check wheter the person has already been checked in or not
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H%M%S')
            #playsound("Attendancemarked.mp3") #just audio to make it look cool 
            print("im checking in")
            GPIO.output(8,GPIO.LOW)
            GPIO.output(40,GPIO.HIGH)
            f.writelines(f'\n{name},{o},{dtString}')
            sleep(1)
            GPIO.output(40,GPIO.LOW)
            GPIO.output(8,GPIO.HIGH)
            
#to mark checkout i call this function
def outAttendance(name):
    o=name
    name ='Check Out         ' + name
    with open(p,'r+') as f:
        myDataList = f.readlines()
        nameList= []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            #the below if statement will check wheter the person has already checked out or not
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H%M%S')
            print("im checking out ")
            GPIO.output(33,GPIO.LOW)
            GPIO.output(40,GPIO.HIGH)
            #playsound("checkoutmarked.mp3") #just audio to make it look cool 
            f.writelines(f'\n{name},{o},{dtString}')
            sleep(1)
            GPIO.output(40,GPIO.LOW)
            GPIO.output(33,GPIO.HIGH)


# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# use the trained model
recognizer.read('trainer/trainer.yml')

# Load prebuilt model to detect if a face exists or not
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# This is for the font
font = cv2.FONT_HERSHEY_TRIPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
GPIO.output(8,GPIO.HIGH)
GPIO.output(40,GPIO.LOW)
value(x)
x=value(x)

#playsound("markingattendance.mp3")


# Loop
#simply put this x and now im afraid removing it will mess the whole program up
if x=='1':
    while True:
        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,0,0), 1)

            # Recognize the face belongs to which ID
            Id ,conf= recognizer.predict(gray[y:y+h,x:x+w])

            # Check the ID if exist 
            if(Id == 1):
                if(conf<75):#check if the confidence score is less than 50 , the less the confidence score is the more better will the recognition be
                    Id = "Mohid"
                    if en == '1':  #its a counter for the user to decide to put on attendance mode or check out mode
                        print("Marking Attendance")
                        markAttendance(Id)# according to the EN value a attendance function or the check out function will be invoked
                    else:
                        print("Checking  Out")
                        outAttendance(Id)
                else:
                    Id=" Please Stand Closer"
                
                            #if counter 0 add the time nd increment counter to avoid overriding

                    #If not exist, then it is Unknown
            elif(Id == 2): #make sure to create multiple ids
                if(conf<75):
                    Id = "Abram"
                    if en =='1':
                        markAttendance(Id)
                    else:
                        outAttendance(Id)
                else:
                    Id=" Please Stand Closer"
            elif(Id == 3): #make sure to create multiple ids
                if(conf<50):
                    Id = "NA"
                    if en =='1':
                        markAttendance(Id)
                    else:
                        outAttendance(Id)
                else:
                    Id=" Please Stand Closer"
            elif(Id == 4): #make sure to create multiple ids
                if(conf<50):
                    Id = "NA"
                    if en =='1':
                        markAttendance(Id)
                    else:
                        outAttendance(Id)
                else:
                    Id=" Please Stand Closer"

            elif(Id == 5): #make sure to create multiple ids
                if(conf<50):
                    Id = "NA"
                    if en =='1':
                        markAttendance(Id)
                    else:
                        outAttendance(Id)
                else:
                    Id=" Please Stand Closer"
            else:
                Id ="Unknown" #if not recognised then this shiz
            print(Id)
            print(en)
            print(conf)
                            

            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,0,0), 1) #u can change the design of ur output box in here 
            cv2.putText(im, str(Id), (x,y-40), font, 1, (0,0,0), 2)   # you can change the design of your output text in here

        # Display the video frame with the bounded rectangle
        cv2.imshow('im',im) 

        # If 'q' is pressed, close program
        #if 'w' is pressed, put the program in check out mode 

        pressedKey = cv2.waitKey(100) & 0xFF
        if pressedKey == ord('q'): #this is to close the program 
            break
        elif pressedKey == ord('w'): # this one is to chose checkout mode    once its pressed u can go back  u will have to restart the whole program probabaly by restarting ur system ( if u are using a raspberry pi)
            #playsound("checkout.mp3")
            odd=odd+1
            nen = odd%2
            if nen == 0:
                en='1'
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(33,GPIO.LOW)
            elif nen == 1:
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(8,GPIO.LOW)
                print("Checking out")
                en = '2'

# Stop the camera
#playsound("terminating.mp3") #just audio to make it look cool
GPIO.output(8,GPIO.LOW)
GPIO.output(40,GPIO.HIGH)
GPIO.output(33,GPIO.LOW)
sleep(0.5)
GPIO.output(40,GPIO.LOW)
GPIO.output(33,GPIO.HIGH)
sleep(0.2)
GPIO.output(33,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
sleep(0.2)
GPIO.output(8,GPIO.LOW)
GPIO.output(33, GPIO.HIGH)
sleep(0.2)
GPIO.output(33, GPIO.LOW)
GPIO.output(40,GPIO.HIGH)
sleep(0.5)
GPIO.output(40,GPIO.LOW)
GPIO.output(33,GPIO.HIGH)
sleep(0.2)
GPIO.output(33,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
sleep(0.2)
GPIO.output(8,GPIO.LOW)
GPIO.output(33, GPIO.HIGH)
sleep(0.2)
GPIO.output(33, GPIO.LOW)
GPIO.output(40,GPIO.HIGH)
sleep(0.5)
GPIO.output(40,GPIO.LOW)
cam.release()
# Close all windows
cv2.destroyAllWindows() #audio to make it cool
#playsound("Nice.mp3")
