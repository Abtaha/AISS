import time
import cv2
import numpy as np

from models.Face_Recognition import Face_Recognition
from models.object_detection_lite.objDetection import run

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
cap = cv2.VideoCapture(0)

while True:
    start = time.time()

    ret, frame = cap.read()
    frame = cv2.resize(frame, (500,500))
    
    NN.run(frame)
    
    cv2.imshow("hey Vsauce, Michael here", NN.frame)
    print(f"FPS: {1 / (time.time() - start)}")

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
