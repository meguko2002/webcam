import cv2
import numpy as np

height = 40
width = 500
start_list = (0, 255, 255)
stop_list = (180, 255, 255)

bar =np.zeros((height, width, len(start_list)), dtype=np.uint8)
for i, (start, stop) in enumerate(zip(start_list, stop_list)):
    bar[:, :, i] = np.tile(np.linspace(start, stop, width), (height, 1))

hsv = cv2.cvtColor(bar, cv2.COLOR_HSV2BGR)
cv2.imshow('tmp', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
