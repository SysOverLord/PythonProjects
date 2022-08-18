
from tkinter.tix import Tree
import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image



def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)
    
    
def cartoonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage,cv2.COLOR_BGR2RGB)
    
    if originalImage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit
    
    ReSized1 = cv2.resize(originalImage, (960, 540)) 
    #plt.imshow(ReSized1,cmap='gray')
    
    
    grayScaleImage =  cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
    
    #plt.imshow(ReSized2, cmap='gray')
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960,540))
    #plt.imshow(ReSized3, cmap='gray')
    
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (960, 540))
    #plt.imshow(ReSized4, cmap='gray')
    
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))
    #plt.imshow(ReSized5,cmap='gray')
    
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    #plt.imshow(ReSized6, cmap='gray')
    images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')


upload()
plt.show()