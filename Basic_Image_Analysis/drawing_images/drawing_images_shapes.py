#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
#%%
zeros=np.zeros([255,255,3])
ones=np.ones([255,255,3])
fig,axs=plt.subplots(1,2 ,figsize=(15,10))
axs[0].imshow(zeros)
axs[0].set_title('Black color image')
axs[1].imshow(ones)
axs[1].set_title('White color image')

# %%
file_path=Path.cwd()
# Draw a Line (start_point, end_point, color, thickness)
Zeros_line=cv2.line(zeros, (0, 50), (450, 50), (255, 0, 0), 3)  # Red line
Zeros_line=cv2.line(Zeros_line, (50, 0), (50, 450), (0,255, 0), 3)  
plt.imshow(Zeros_line)

cv2.imwrite(str(file_path / "lines.jpg"), Zeros_line)

# %%
