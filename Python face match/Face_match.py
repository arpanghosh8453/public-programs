import face_recognition
import cv2
import time,os

picture_of_me = face_recognition.load_image_file("/home/arpan/Pictures/Myself/arpan.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

none_count = 0
intruder_count = 0
camera_fail = 0

while True:

    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    return_value, frame = cap.read()
    cap.release()
    
    if return_value:
        cv2.imwrite('/home/arpan/Pictures/test.jpg',frame)
        unknown_picture = face_recognition.load_image_file("/home/arpan/Pictures/test.jpg")
        webcam_feed = face_recognition.face_encodings(unknown_picture)

        i_am_present = False

        for face in webcam_feed:
            if face_recognition.compare_faces([my_face_encoding], face, tolerance=0.47)[0]:
                print("You are there | ",face_recognition.face_distance([my_face_encoding], face))
                i_am_present = True
            else:
                #os.system('notify-send "Intruder Found"')
                print("Intruder Found! | ",face_recognition.face_distance([my_face_encoding], face))
        

                
        if len(webcam_feed) == 0:
            #os.system('notify-send "None Found"')
            print("None found")
            none_count += 1
        else:
            if not i_am_present:
                intruder_count += 1
            else:
                none_count = 0
                intruder_count = 0
                camera_fail = 0
    else:
        print("Webcam image failed!")
        camera_fail += 1
        #os.system('notify-send "No webcam Found"')

  

    if ((none_count >= 15) or (intruder_count >= 3)) or camera_fail >= 3:
        print("Lockdown initiated")
        os.system('notify-send "Lockdown initiated!"')
        
    
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