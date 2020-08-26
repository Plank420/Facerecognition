# Facerecognition
Face Recognition Attendance System


The following Program is basically a Face recognition system with an addition of an Attendance feature. 
participants are supposed to use the dataset.py to have around 200 images of them taken . these images are then saved in the dataset folder. along with an individuals dataset an Id is associated with it which will help diffrentiate it from other participants.


this dataset folder is then accesed by training.py to create binary face data of each individual from the 200 images taken. this data is then stored in a training.yml file.


We then run the face recognition part of the program which basically does the work of recognizing faces and returning the output of whose face it is recognizing. it does so with the help of a variable called Confidence score or Conf for short. 


Conf is basically a variable that tells how confident the program is in recognizing the persons face. the Lower the number the more confident is the program. if this inverse propotionality relation bothers you , you can always subtract the value by 100 and it will then show its confidence score in percentage . for example if a face is detected and the conf or confidence score comes out to be 30,


this simply means that the program is 100 - 30 = 70% sure that it is that person . we can increase the accuracy of the program by adding more and more images in our dataset folder instead of 200. you can also set up a treshold if statement. for example if ur confidence score is above 70% only then acknowledge that person is recognized , else just ignore.



The ID variable is the one that was initialized in the dataset program to be associated with the individuals image.
this ID is then changes to the corresonding name of the person.this name is then displayed on the video capture screen.
Now as it is a attendence based system it needs to have some sort of check in check out system. this is implemented in the above program. whenever the id of a person is recognized their name is then added to a .csv file that can be accesed with the help of microsoft excel.


you can quit the program by pressing 'Q' whenever you wish to. make sure your cursor is clicked on the video capture window that opens up otherwise the program wont respond to the button press


when the program runs initially its in check in mode.if the person wishes to check out he simply needs to press the button 'W' or flip a switch(if he is using a raspberry pi ... refer to the program for easy understanding). By pressing W you can change to check out mode and the program would then mark you as checkout. The program also adds all these csv files to a folder called attendance. you can then acces these csv files whenever you wish too. also if a new day begins the program automatically names the excel file as the current date and also gives information on what time the person entered the premises.


there codes given above are for A windows running python 3.7.3 and also Raspberry pi 3 python 3.7.3
modules to be installed : 
cv2(open cv)
datetime
numpy
csv
playsound(if you use the windows version )
RPi.GPIO (if you are using the Raspberry pi version)


Special thanks to Jacky Lee ( https://www.youtube.com/user/jackyltle)


