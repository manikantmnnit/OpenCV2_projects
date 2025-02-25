#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pathlib
from pathlib import Path

# %%
path_name=Path.cwd()
image_BGR=cv2.imread(path_name/"OSCC_100x_1.jpg")
cv2.imshow('BGR image',image_BGR)
cv2.waitKey()
cv2.destroyAllWindows()
# %%
# conver image into grayscale
image_gray=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2GRAY)
hist_gray=cv2.calcHist([image_gray],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_gray,color='r')
plt.title("Gray scale image histogram")
# %%
cv2.imwrite(path_name/'hist_gray.jpg',hist_gray)
