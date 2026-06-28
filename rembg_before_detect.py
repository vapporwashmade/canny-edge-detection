import cv2
import numpy as np
from rembg import remove

img = cv2.imread("pommel.jpg")
img_no_bg = remove(img)
cv2.imwrite("pommel_no_bg.jpg", img_no_bg)

alpha_channel = img_no_bg[:, :, 3]

img_blur = cv2.GaussianBlur(alpha_channel, (3, 3), 0)

final_edges = cv2.Canny(img_blur, 100, 200)

cv2.imwrite("pommel_rembg_then_blur.jpg", final_edges)