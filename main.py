import cv2

def nothing(x):
    pass

img = cv2.imread("pommel.jpg", cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

cv2.namedWindow('Canny Tuner', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Low Thresh', 'Canny Tuner', 50, 255, nothing)
cv2.createTrackbar('High Thresh', 'Canny Tuner', 150, 255, nothing)

cv2.waitKey(100)

while True:
    low = cv2.getTrackbarPos('Low Thresh', 'Canny Tuner')
    high = cv2.getTrackbarPos('High Thresh', 'Canny Tuner')

    if low == -1 or high == -1:
        break

    edges = cv2.Canny(img_blur, low, high)
    cv2.imshow('Canny Tuner', edges)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()