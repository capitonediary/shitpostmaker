 
import cv2
import os
from PIL import Image
import numpy as np
import datetime
from PIL import ImageDraw

image_folder = 'Camera'
video_name = 'outputvideo.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = sorted(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
fps = 110
period = 5
video = cv2.VideoWriter(video_name, 0, fps, (width,height))

font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (350, 430)
  
# fontScale
fontScale = 0.5
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method

   
for image in images:
    dt_object = datetime.datetime.fromtimestamp(int(image[:-4])/100000)
    #print(str(dt_object))
    f = cv2.imread(os.path.join(image_folder, image))
    #f = cv2.putText(cv2.imread(os.path.join(image_folder, image)), str(dt_object), org, font, 
                #fontScale, color, thickness, cv2.LINE_AA)
    #f = cv2.putText(f, "~{} mins/sec".format(round((fps * period)/60, 2)), (30, 30), font, 
                    #fontScale, color, thickness, cv2.LINE_AA)
    video.write(f)

cv2.destroyAllWindows()
video.release()