import time
import cv2

from models.Face_Recognition import Face_Recognition
from models.object_detection.object_detection_tutorial import run

# Helper functions
def getTime(start):
    fps = (1 / (time.time() - start))
    print("FPS:",fps)

class NeuralNets:
    # Basic Initialization
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.FR = Face_Recognition()

        while True:
            start = time.time()
            
            ret, self.frame = self.cap.read()
            self.frame = cv2.resize(self.frame, (500,500))
            self.main()
            cv2.imshow("hey Vsauce, Michael here", self.frame)
            getTime(start)
            
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    # This runs the Person Detection Neural Network using hog cascades open-cv
    def objectDetection(self, frame):
        a = run(frame)
        self.facialRecognition(a)

    # This runs the Facial Detection Neural Network using dlib
    def facialRecognition(self, frame):
        self.FR.run(frame)
        self.frame = self.FR.frame

    def main(self):
        self.objectDetection(self.frame)

NN = NeuralNets()

