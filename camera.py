 
import cv2
import time
  
vid = cv2.VideoCapture(0)
time.sleep(0)
while(True):
      
 
    ret, frame = vid.read()
  

    cv2.imshow('frame', frame)
    cv2.imwrite("./Camera/{}.png".format(str(int(round(time.time(), 5)*100000))), frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(5)
vid.release()
cv2.destroyAllWindows()
