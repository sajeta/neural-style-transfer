# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:41:37 2018

@author: marin
"""

import cv2

def RGB_to_grayscale(imagePath): 
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Gray image', gray)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()