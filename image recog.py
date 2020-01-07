import cv2
import vlc
cam=cv2.VideoCapture(0)
m=vlc.MediaPlayer(r'D:\playlist\Ujjwal mp3\{DEAAFC9F-533C-4473-AEA9-FB3FD2523866}.mp3')
fd=cv2.CascadeClassifier(r'C:\Program Files (x86)\Python36-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
flag=1
while True:
 r,i=cam.read()
 j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
 face=fd.detectMultiScale(j,1.3,7)
 l=len(face)
 total=0
 for(x,y,w,h) in face:
     cv2.rectangle(i,(x,y),(x+w,y+h) ,(0,255,255),5)
     total=w*h
     print(total)
 if(l>0):
     print('song played')
     m.play()
     flag=0
     m.audio_set_volume(100-int(total/1000))
 elif(flag==0):
     m.pause()
     print('song paused')
     flag=1  
 cv2.imshow('image1',i)

 k=cv2.waitKey(5)
 if(k==ord('q')):
    cv2.destroyAllWindows()
    break
