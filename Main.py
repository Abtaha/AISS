from tkinter import *
from PIL import ImageTk, Image

from Receiver.receiver import get_stream
from AI_System.Neural_Networks import NeuralNets

import cv2

root = Tk()

app = Frame(root, bg="white")
app.grid()

lmain = Label(app)
lmain.grid()

NN = NeuralNets()

def video_stream():
    frame = get_stream()
    
    NN.run(frame)
    
    cv2image = cv2.cvtColor(NN.frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

video_stream()
root.mainloop()


cv2.destroyAllWindows()