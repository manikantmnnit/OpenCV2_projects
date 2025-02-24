#%%
import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
# %%
file_path=Path.cwd()
image=cv2.imread(file_path/"OSCC_100x_1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("image_1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
# mean,median, std
mean = np.mean(image)
median = np.median(image)
std_dev = np.std(image)
variance = np.var(image)
min_val = np.min(image)
max_val = np.max(image)

print(f"Mean: {mean}, Median: {median}, Std Dev: {std_dev}, Variance: {variance}, Min: {min_val}, Max: {max_val}")

# %%
