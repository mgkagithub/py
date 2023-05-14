import cv2 
import mediapipe as mp
import time 
from time import sleep
import pyautogui as pg
screen_w , screen_h = pg.size()
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
#cv2.namedWindow("mouse", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("mouse", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
    _,frame = cap.read()
    rgb_frame = frame
    flipped = cv2.flip(rgb_frame,flipCode = 1)
    frame_h , frame_w ,_ = frame.shape
    output = hand_detector.process(flipped)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(flipped,hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks):
                x = int(landmark.x*frame_w)
                y = int(landmark.y*frame_h)
                if id == 8: #index
                    index_x = screen_w/frame_w*x
                    index_y = screen_h/frame_h*y
                    cv2.circle(img = flipped,center = (x,y),radius = 20,color = (0,255,255))
                    pg.moveTo(index_x,index_y)
                if id == 4: #thumb
                    thumb_x = screen_w/frame_w*x
                    thumb_y = screen_h/frame_h*y
                    cv2.circle(img = flipped,center = (x,y),radius = 20,color = (0,255,255))
                if id == 12: #middle
                    middle_x = screen_w/frame_w*x
                    middle_y = screen_h/frame_h*y
                    cv2.circle(img = flipped,center = (x,y),radius = 20,color = (0,255,255))
                    print(abs(middle_y-thumb_y))
                    if abs(middle_y-thumb_y) < 30 and abs(middle_x-thumb_x) < 30:
                        print("click")
                        pg.click(button = 'left', clicks = 2)
                        
                    else:
                        pg.moveTo(index_x,index_y)                       
                if id == 16: #ring
                    ring_x = screen_w/frame_w*x
                    ring_y = screen_h/frame_h*y
                    cv2.circle(img = flipped,center = (x,y),radius = 20,color = (0,255,255))
                    print(abs(ring_y - thumb_y))
                    if abs(ring_y - thumb_y) < 40 and abs(ring_x - thumb_x) < 40 :
                        print("closing program")
                        exit()
                    else:
                        pg.moveTo(index_x,index_y) 
                if id == 20: #pinky
                    pinky_x = screen_w/frame_w*x
                    pinky_y = screen_h/frame_h*y
                    cv2.circle(img = flipped,center = (x,y),radius = 20,color = (0,255,255))


#    cv2.imshow("mouse", flipped)
    cv2.waitKey(1)
