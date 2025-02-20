#%%
import cv2 
import numpy as np
import matplotlib.pyplot as plt
# %%
# Load an image using 'imread' specifying the path to image
file_path='D:\Computer Vision\CV2 based Projects\Gray_scaling\OSCC_100x_1.jpg'
input_BGR =cv2.imread(file_path) # image in BGR format

input_RGB=cv2.cvtColor(input,cv2.COLOR_BGR2RGB) # convert image to gray scale

# Step 2: Display the image
fig,axs=plt.subplots(2,2,figsize=(10,5))
axs[0,0].imshow(input_BGR)
axs[0,0].set_title('Image in BGR format')

axs[0,1].imshow(input_RGB)
axs[0,1].set_title('Image in RGB format')

axs[1,0].imshow(cv2.cvtColor(input_BGR,cv2.COLOR_BGR2GRAY))
axs[1,0].set_title('Image in Gray scale format')

axs[1,1].imshow(cv2.cvtColor(input_RGB,cv2.COLOR_RGB2GRAY))
axs[1,1].set_title('Image in Gray scale format')

plt.show()
plt.tight_layout()

# %% 
# save image in BGR and RGB format
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Gray_scaling\image_BGR_GRAY.jpg',cv2.cvtColor(input_BGR,cv2.COLOR_BGR2GRAY))
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Gray_scaling\image_RGB_GRAY.jpg',cv2.cvtColor(input_RGB,cv2.COLOR_BGR2GRAY))

# %%
