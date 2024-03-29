import time
import cv2
from flask import Flask, render_template, Response
cap = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""

    # Read until video is completed
    #while(cap.isOpened()):
      # Capture frame-by-frame
    ret, img = cap.read()
    if ret == True:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (500,500))
        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            #time.sleep(0.1)
        #else:
        #    break


@app.route('/video_feed.jpg')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
