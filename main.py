import cv2
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Loading grayscale image
image_path = "pommel.jpg"
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Gaussian blur
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

# Canny edge detection
edges = cv2.Canny(img_blur, threshold1=150, threshold2=350)

cv2.imwrite("pommel_line_drawing.jpg", edges)
# Plot Original Grayscale
plt.subplot(1, 2, 1)
plt.title("Original (Grayscale)")
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

# Plot Canny Edges
plt.subplot(1, 2, 2)
plt.title("Canny Edge Detection")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
