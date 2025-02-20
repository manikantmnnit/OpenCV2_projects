
#%%
import numpy as np
import cv2
import matplotlib.pyplot as plt
# %%
# Load an image using 'imread' specifying the path to image
file_path='D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\OSCC_100x_1.jpg'
input = cv2.imread(file_path) # image in BGR format

# Step 2: Display the image
cv2.imshow('First Image', input)  # 'First Image' is the window title

# Step 3: Wait for a key press (0 means wait indefinitely)
cv2.waitKey(0)

# Step 4: Close all OpenCV windows
cv2.destroyAllWindows()


# %%
# display image using matplotlib
fig,axs=plt.subplots(1,2,figsize=(10,5))
axs[0].imshow(input)
axs[0].set_title('First Image using Matplotlib in BGR format')
axs[1].imshow(cv2.cvtColor(input, cv2.COLOR_BGR2RGB))
axs[1].set_title('First Image using Matplotlib in RGB format')
plt.show()
print('Image shape:',input.shape)
print('Image data type:',input.dtype)
print('Image size:',input.size)
print('Image max value:',input.max())
print('Image min value:',input.min())
print('image width (no of pixels from left to right rows) : {0} pixels'.format(input.shape[1]))
print('image height (no of pixels from top to bottom columns): {0} pixels'.format(input.shape[0]))
# %%
# save image in BGR and RGB format

cv2.imwrite('D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\OSCC_100x_1_BGR.jpg',input)
cv2.imwrite('D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\OSCC_100x_1_RGB.jpg',cv2.cvtColor(input, cv2.COLOR_BGR2RGB))

# %%
