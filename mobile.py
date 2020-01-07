import cv2
cam=cv2.VideoCapture('http://192.168.43.1:8080/video')
while True:
    r,i=cam.read()
    print(r)
    if(r==1):
        cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
