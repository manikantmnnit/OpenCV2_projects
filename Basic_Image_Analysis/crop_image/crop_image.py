
#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
# Load an image using 'imread' specifying the path to image
file_path='D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\crop_image\OSCC_100x_1.jpg'
input_BGR=cv2.imread(file_path) # image in BGR format

# %% Crop Image
# Define the cropping coordinates (x, y, width, height)
x, y, w, h = 100, 100, 300, 300  # (start_x, start_y, width, height)

# Crop the original image
input_crop = input_BGR[y:y+h, x:x+w]  # Slice the image to get the region of interest

# Show original and cropped images
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(input_BGR)
axs[0].set_title('Original Image in BGR format')

axs[1].imshow(input_crop)
axs[1].set_title('Cropped Image')

plt.show()
plt.tight_layout()

# %% Save cropped image
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\crop_image\input_crop.jpg', input_crop)

# %% Print memory size of cropped image
print("Cropped Image Size in KB:", input_crop.size / 1024)

# %%
