 
# import the opencv library
import cv2
import time
  
# define a video capture object
vid = cv2.VideoCapture(2)
time.sleep(0)
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    print(frame)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite("/run/media/blaregrimoire/43218a61-a62c-4196-9ff9-4b1d33ade7ad/Camera/{}.png".format(str(int(round(time.time(), 5)*100000))), frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(5)
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()