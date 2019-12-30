from os import listdir
from os.path import isfile, join
import os
import cv2
import dlib
import numpy as np

video_path = 'Video_path'

def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.8, thickness=1):

    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
    cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness, lineType=cv2.LINE_AA)

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(video_path)

img_size = 64
margin = 0.2
frame_count = 0

