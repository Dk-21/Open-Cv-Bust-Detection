# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:13:47 2021

@author: divyp
"""
import cv2
from threading import Thread

frame = 0

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            global frame
            _, frame = cap.read()
            cv2.imshow("frame",frame)
def get_f():
    # print(frame)
    return frame
    
# def methodA():
#     cap = cv2.VideoCapture(0)
#     while cap.isOpened():
#         global frame
#         _, frame = cap.read()

# class myClassB(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
#     def run(self):
#         global frame
#         print(frame)

# p=Process(target=methodA())
# p.start()

myClassA()
# myClassB()
# from threading import Thread

# class myClassA(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
#     def run(self):
#         while True:
#             print 'A'

# class myClassB(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
#     def run(self):
#         while True:
#             print 'B'


# myClassA()
# myClassB()
# while True:
#     pass