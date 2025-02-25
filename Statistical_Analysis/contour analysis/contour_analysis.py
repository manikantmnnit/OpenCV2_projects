import cv2
import numpy as np
import pathlib
#%%
# Step 1: Create or load a binary image
# Example: Create a binary image with some shapes
binary_image = np.zeros((400, 400), dtype=np.uint8)  # Black background

# Draw a white rectangle
cv2.rectangle(binary_image, (50, 50), (200, 200), 255, -1)  # Filled rectangle

# Draw a white circle
cv2.circle(binary_image, (300, 300), 50, 255, -1)  # Filled circle
file_path=pathlib.Path.cwd()

cv2.imwrite(file_path/'rect_circ_image.jpg',binary_image)
#%%
# Step 2: Find contours in the binary image
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 3: Analyze the contours
print(f"Number of contours detected: {len(contours)}")

for i, contour in enumerate(contours):
    # Calculate contour area
    area = cv2.contourArea(contour)
    print(f"Contour {i + 1}: Area = {area}")

    # Calculate contour perimeter
    perimeter = cv2.arcLength(contour, True)
    print(f"Contour {i + 1}: Perimeter = {perimeter}")

    # Get bounding box
    x, y, w, h = cv2.boundingRect(contour)
    print(f"Contour {i + 1}: Bounding Box = (x={x}, y={y}, w={w}, h={h})")

    # Get centroid (center of mass)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        print(f"Contour {i + 1}: Centroid = (cx={cx}, cy={cy})")

# Step 4: Draw contours on the original binary image
output_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)  # Convert to color image for drawing
cv2.drawContours(output_image, contours, -1, (0, 255, 255), 4)  # Draw contours in green
# %%
import matplotlib.pyplot as plt
# Step 5: Display the output image with contours
fig, axes = plt.subplots(1, 2, figsize=(15, 10))

# Plot the binary image on the first subplot using imshow
axes[0].imshow(binary_image, cmap='gray')
axes[0].set_title('Binary Image Plot')
axes[0].axis('off')  # Optionally turn off the axis

# Example plot on the second subplot (e.g., plot a histogram of pixel values)
axes[1].imshow(output_image,cmap="gray")
axes[1].set_title('Contour of Binary Image')

# Show the plot
plt.show()


# %%
