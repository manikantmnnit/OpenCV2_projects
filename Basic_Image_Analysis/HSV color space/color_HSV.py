#%%
import cv2
import matplotlib.pyplot as plt

# Load the image
file_path = 'D:\Computer Vision\CV2 based Projects\Basic_Image_Analysis\HSV color space\OSCC_100x_1.jpg'
input_BGR = cv2.imread(file_path)

#%%

# Convert the image from BGR to HSV color space
input_HSV = cv2.cvtColor(input_BGR, cv2.COLOR_BGR2HSV)

# Extract HSV channels
hue_channel = input_HSV[:, :, 0]  # Hue channel
saturation_channel = input_HSV[:, :, 1]  # Saturation channel
value_channel = input_HSV[:, :, 2]  # Value channel

# Display the original and HSV images
fig, axs = plt.subplots(3, 2, figsize=(10, 5))
axs[0,0].imshow(cv2.cvtColor(input_BGR, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
axs[0,0].set_title('Original Image in RGB')

axs[0,1].imshow(cv2.cvtColor(input_HSV, cv2.COLOR_BGR2RGB))  # HSV image converted to RGB for display
axs[0,1].set_title('Image in HSV Color Space')

# Hue channel (you might want to use `cmap='hsv'` to visualize it better)
axs[1, 0].imshow(hue_channel, cmap='hsv')
axs[1, 0].set_title('Hue Channel')

# Saturation channel
axs[1, 1].imshow(saturation_channel, cmap='gray')  # Grayscale display of saturation
axs[1, 1].set_title('Saturation Channel')

# Value channel
axs[2, 0].imshow(value_channel, cmap='gray')  # Grayscale display of value
axs[2,0].set_title('Value Channel')

plt.tight_layout()
plt.show()
# %%
