import face_recognition
import cv2
import time,os

picture_of_me = face_recognition.load_image_file("/home/arpan/Pictures/Myself/arpan.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

while True:

    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        cv2.imwrite('/home/arpan/Pictures/test.jpg',frame)
    else:
        print("Webcam image failed!")
  
    unknown_picture = face_recognition.load_image_file("/home/arpan/Pictures/test.jpg")
    webcam_feed = face_recognition.face_encodings(unknown_picture)

    for face in webcam_feed:
        if face_recognition.compare_faces([my_face_encoding], face, tolerance=0.53)[0]:
            print("You are there")
        else:
            os.system('notify-send "Intruder Found"')
            print(face_recognition.face_distance([my_face_encoding], face))
            
    if len(webcam_feed) == 0:
        #os.system('notify-send "None Found"')
        print("None found")
    
    time.sleep(10)
    
'''
import cv2
import numpy as np

all_camera_idx_available = []

for camera_idx in range(10):
    cap = cv2.VideoCapture(camera_idx)
    if cap.isOpened():
        print(f'Camera index available: {camera_idx}')
        all_camera_idx_available.append(camera_idx)
        cap.release()
'''