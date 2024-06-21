import cv2
import numpy as np

image_size = 500


def create_gradient_background(size):
    gradient = np.zeros((size, size, 3), dtype=np.uint8)
    for i in range(size):
        color_value = int(255 * (i / size))
        gradient[i, :] = (color_value, color_value, color_value)
    return gradient


image = create_gradient_background(image_size)

center = (image_size // 2, image_size // 2)
radius = image_size // 3
line_thickness = 5
red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

cv2.circle(image, center, radius, white, line_thickness)

cv2.line(image, (center[0] - 50, center[1] - 50), (center[0] - 50, center[1]), blue, line_thickness)
cv2.line(image, (center[0] - 25, center[1] - 50), (center[0] - 25, center[1]), blue, line_thickness)
cv2.line(image, (center[0] + 25, center[1] - 50), (center[0] + 25, center[1]), blue, line_thickness)
cv2.line(image, (center[0] + 50, center[1] - 50), (center[0] + 50, center[1]), blue, line_thickness)

cv2.line(image, (center[0] - 50, center[1] - 50), (center[0] - 25, center[1] - 50), red, line_thickness)
cv2.line(image, (center[0] + 25, center[1] - 50), (center[0] + 50, center[1] - 50), red, line_thickness)

cv2.ellipse(image, center, (50, 50), 0, 0, 180, green, line_thickness)
cv2.ellipse(image, center, (25, 25), 0, 0, 180, green, line_thickness)

cv2.imshow('U Letter', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
