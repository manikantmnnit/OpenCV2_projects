#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
#%%
path_name=Path.cwd()
image_BGR=cv2.imread(path_name/"OSCC_100x_1.jpg")
cv2.imshow('BGR image',image_BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
B,G,R=cv2.split(image_BGR)

zeros=np.zeros_like(B)

only_blue = cv2.merge([B, zeros, zeros])
only_green = cv2.merge([zeros, G, zeros])
only_red = cv2.merge([zeros, zeros, R])

# Show results
cv2.imshow("Only Blue", only_blue)
cv2.imshow("Only Green", only_green)
cv2.imshow("Only Red", only_red)

cv2.waitKey(0)
cv2.destroyAllWindows()


# %%

path_name
cv2.imwrite(str(path_name / "only_blue.jpg"),only_blue)
cv2.imwrite(str(path_name / "only_green.jpg"),only_green)
cv2.imwrite(str(path_name / "only_red.jpg"),only_red)
# %%
