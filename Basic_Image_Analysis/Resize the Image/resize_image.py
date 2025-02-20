# Resizing an image means changing its dimensions (height and width) to a specified size, 
# often to fit a particular display or model input requirements. 
# It affects memory size by adjusting the number of pixels and channels, 
# reducing or increasing the image's memory consumption accordingly.
#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
# Load an image using 'imread' specifying the path to image
file_path='D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\Resize the Image\OSCC_100x_1.jpg'
input_BGR=cv2.imread(file_path) # image in BGR format
print('Original Image shape:',input_BGR.shape)
input_resize=cv2.resize(input_BGR,(500,500))
print('Resized Image shape:',input_resize.shape)


# Step 2: scaling down the image
scale_percent = 0.5 # 50 percent of original size

width_change = int(input_BGR.shape[1] * scale_percent)
height_change=int(input_BGR.shape[0] * scale_percent)

input_scale_down=cv2.resize(input_BGR,(height_change,width_change))

# step 3 scaling up the image

scale_percent=1.5

width_change = int(input_BGR.shape[1] * scale_percent)
height_change=int(input_BGR.shape[0] * scale_percent)


input_scale_up=cv2.resize(input_BGR,(height_change,width_change))

# step 4 
fig,axs=plt.subplots(1,3,figsize=(10,5))
axs[0].imshow(input_BGR)
axs[0].set_title('Original Image in BGR format')

axs[1].imshow(input_scale_down)
axs[1].set_title('scale  down of original Image')

axs[2].imshow(input_scale_up)
axs[2].set_title('scale up of original Image')

plt.show()
plt.tight_layout()
# # %%

# %%
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\Resize the Image\input_scale_down.jpg',input_scale_down)
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\Resize the Image\input_scale_up.png',input_scale_up)


# %%
# find memory size of each image
input_BGR.size/1024
print( " input image Size in KB:",input_BGR.size/1024)
print("scaling up image size in KB:",input_scale_up.size/1024)
print("scaling down image in KB: ",input_scale_down.size/1024)

# %%
