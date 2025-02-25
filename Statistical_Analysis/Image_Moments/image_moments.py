#%%
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pathlib

# %%
file_name=pathlib.Path.cwd()
image_bgr=cv2.imread(filename=file_name/"OSCC_100x_1.jpg")
cv2.imshow('image_bgr',image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
img_gray=cv2.cvtColor(image_bgr,cv2.COLOR_BGR2GRAY)
_,img_binary=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
image_moments=cv2.moments(img_binary, binaryImage=False)

# %%
import pandas as pd
data_moment=pd.DataFrame([image_moments])
data_moment.to_csv('data_moments.csv')

# %%
for moment, value in image_moments.items():
    if "m" in moment:  # Filter out non-moment entries
        print(f"{moment}: {value}")

# Central Moments (muXX) and Normalized Moments (nuXX)
print("\nCentral Moments (muXX):")
for moment, value in image_moments.items():
    if "mu" in moment:
        print(f"{moment}: {value}")

print("\nNormalized Moments (nuXX):")
for moment, value in image_moments.items():
    if "nu" in moment:
        print(f"{moment}: {value}")

# %%
# Calculate Centroid (cx, cy) using the moments
cx = image_moments['m10'] / image_moments['m00']
cy = image_moments['m01'] / image_moments['m00']

# Calculate Area (m00)
area = image_moments['m00']

# Print calculated properties
print(f"Centroid: (cx, cy) = ({cx}, {cy})")
print(f"Area (m00): {area}")
# %%
