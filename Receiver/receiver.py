import cv2
import numpy as np
import urllib.request
import time

def get_stream():
    stream = urllib.request.urlopen('http://127.0.0.1:5000/video_feed.jpg')
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
