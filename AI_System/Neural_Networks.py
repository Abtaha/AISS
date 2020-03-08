import time
import cv2
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from AI_System.models.Face_Recognition import Face_Recognition
from AI_System.models.object_detection_lite.objDetection import run


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
