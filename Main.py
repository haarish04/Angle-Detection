img = cv2.imread("testimage.jpg")
cv2_imshow(img)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert image to binary
_, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Find all the contours in the thresholded image
contours, _ = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for i, c in enumerate(contours):

  # Calculate the area of each contour
  area = cv2.contourArea(c)

  # Ignore contours that are too small or too large
  if area < 3700 or 100000 < area:
    continue

  # Draw each contour only for visualisation purposes
  cv2.drawContours(img, contours, i, (0, 0, 255), 2)

  # Find the orientation of each shape
  getOrientation(c, img)

cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image to the current directory
cv2.imwrite("output_img.jpg", img)
