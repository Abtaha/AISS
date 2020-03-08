import time
import cv2
import numpy as np
import urllib.request

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from models.Face_Recognition import Face_Recognition
from models.object_detection_lite.objDetection import run

def get_stream():
    stream = urllib.request.urlopen('http://192.168.10.7:5000/video_feed.jpg')
    total_bytes = b''
    i = 0
    while True:
        total_bytes += stream.read(1024)
        b = total_bytes.find(b'\xff\xd9') # JPEG end
        if not b == -1:
            a = total_bytes.find(b'\xff\xd8') # JPEG start
            jpg = total_bytes[a:b+2] # actual image
            total_bytes= total_bytes[b+2:] # other informations

            # decode to colored image ( another option is cv2.IMREAD_GRAYSCALE )
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            i = 1 # display image while receiving data
            if cv2.waitKey(1) ==27 or i == 1: # if user hit esc
                break
    return img

class NeuralNets:
    # Basic Initialization
    def __init__(self):
        self.FR = Face_Recognition()
        self.frame = np.empty((500, 500))

    # This runs the Google Object Detection API using Tensorflow
    def objectDetection(self, frame):
        a = run(frame)
        self.facialRecognition(a)

    # This runs the Facial Detection Neural Network using dlib
    def facialRecognition(self, frame):
        self.FR.run(frame)
        self.frame = self.FR.frame

    def run(self, frame):
        self.objectDetection(frame)

NN = NeuralNets()
#cap = cv2.VideoCapture(0)

while True:
    start = time.time()

    #ret, frame = cap.read()
    #frame = cv2.resize(frame, (500,500))
    
    frame=get_stream()
    
    NN.run(frame)
    
    cv2.imshow("hey Vsauce, Michael here", NN.frame)
    print(f"FPS: {1 / (time.time() - start)}")

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
cv2.destroyAllWindows()
