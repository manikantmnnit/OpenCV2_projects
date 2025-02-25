#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pathlib
from pathlib import Path
import torch

# %%
path_name=Path.cwd()
image_BGR=cv2.imread(path_name/"OSCC_100x_1.jpg")
cv2.imshow('BGR image',image_BGR)
cv2.waitKey()
cv2.destroyAllWindows()
# %%
# Convert BGR to RGB
image_rgb = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
r,g,b=cv2.split(image_rgb)

fig,axes=plt.subplots(1,3,figsize=(15,14))
for i in range(3):
    hist_color=cv2.calcHist(
        [image_rgb],
        channels=[i],
        mask=None,
        histSize=[256],
        ranges=[0,256])
    axes[i].plot(hist_color, color=['red', 'green', 'blue'][i])
    axes[i].set_title(f"Histogram of {['Red', 'Green', 'Blue'][i]} channel")
plt.tight_layout()

# %%
# Save the histogram plot as an image
histogram_filename = "Color_histogram.png"
plt.savefig(histogram_filename)  # Save as PNG
plt.close()
# Load the saved histogram image using OpenCV
histogram_image = cv2.imread(histogram_filename)

# Save the histogram again in a different format if needed
cv2.imwrite("histogram.jpg", histogram_image)
# %%
