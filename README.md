# Facerecognition (Windows & Raspberry Pi)
Face Recognition Attendance System( Windows python 3.7.3 / Raspberry Pi model 3 python 3..7.3)



The following Program is basically a Face recognition system with an addition of an Attendance feature. 


Participants are supposed to use the dataset.py to have around 200 images of them taken . These images are then saved in the dataset folder. Along with an individuals dataset , an Id is associated with it which will help diffrentiate it from other participants by compairing their IDs as well.


This dataset folder is then accesed by training.py to create binary face data of each individual from the 200 images taken. This data is then stored in a training.yml file.


We then run the face recognition part of the program which basically does the work of recognizing faces and returning the output of whose face it is recognizing. It does so with the help of a variable called Confidence score or Conf for short. 


Conf is basically a variable that tells how confident the program is in recognizing the persons face. The lower the number, the more confident the program. If this inverse propotionality relation bothers you , you can always subtract the value by 100 and it will then show its confidence score in percentage . For example if a face is detected and the conf or confidence score comes out to be 30.


This simply means that the program is (100 - 30) = 70% sure that it is that person . We can increase the accuracy of the program by adding more and more images in our dataset folder instead of 200. You can also set up a treshold "if" statement. For example "if" your confidence score is above 70% then acknowledge that person as recognized , "else" just ignore.



The ID variable is the one that was initialized in the dataset program to be associated with the individuals image.
This ID is then changed to the corresonding name of the person.This name is then displayed on the video capture screen.
Now as it is an attendence based system it needs to have some sort of check-in & check-out system. This is implemented in the above program. Whenever the id of a person is recognized, their name is then added to a .csv file that can be accesed with the help of Microsoft Excel.


You can quit the program by pressing 'Q' whenever you wish to. make sure your cursor is clicked on the video capture window that opens up otherwise the program won't respond to the button press.


When the program runs initially it's in check in mode.If the person wishes to check-out he simply needs to press the button 'W' or flip a switch(if he is using a Raspberry Pi ... refer to the program for easy understanding). By pressing W you can change to check out mode and the program would then mark you as checkout. The program also adds all these csv files to a folder called attendance. You can then access these csv files whenever you wish to. Also if a new day begins the program automatically names the excel file as the current date and also gives information on what time the person entered the premises.


The codes given above are for  windows running python 3.7.3 and also Raspberry pi 3 python 3.7.3
Modules to be installed : 
1.cv2(open cv)
2.datetime
3.numpy
4.csv
5.playsound(if you use the windows version )
6.RPi.GPIO (if you are using the Raspberry pi version)

I would recommend to install all these modules with the help of PIP install from the terminal window if youre using the normal Python IDLE. If you are using text editors such as sublime or Pycharm , you probabaly will be able to install these modules through the settings menu of these appliations. 


Special thanks to Jacky Lee ( https://www.youtube.com/user/jackyltle)

