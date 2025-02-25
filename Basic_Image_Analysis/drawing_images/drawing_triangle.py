import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create a black image
image = np.zeros([255, 255, 3], dtype=np.uint8)

# Draw a rectangle (start_point, end_point, color, thickness)
image_with_rectangle = cv2.rectangle(image.copy(), (50, 50), (200, 150), (0, 255, 0), 3)  # Green rectangle

# Draw a circle (center, radius, color, thickness)
image_with_circle = cv2.circle(image.copy(), (150, 200), 50, (255, 0, 0), 3)  # Red circle

# Draw a triangle (3 points, color, thickness)
points = np.array([[100, 200], [200, 300], [50, 300]], dtype=np.int32)
image_with_triangle = cv2.polylines(image.copy(), [points], isClosed=True, color=(0, 0, 255), thickness=3)  # Blue triangle

# Display the images
fig, axs = plt.subplots(1, 3, figsize=(15, 10))

# Show rectangle
axs[0].imshow(image_with_rectangle)
axs[0].set_title('Rectangle')

# Show circle
axs[1].imshow(image_with_circle)
axs[1].set_title('Circle')

# Show triangle
axs[2].imshow(image_with_triangle)
axs[2].set_title('Triangle')

plt.show()

# Save the image with the shapes
file_path = Path.cwd()
cv2.imwrite(str(file_path / "triangle_shapes.jpg"), image_with_triangle)
