img = cv2.imread("image.jpg")


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

  # cv.minAreaRect returns:
  # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
  rect = cv2.minAreaRect(c)
  box = cv2.boxPoints(rect)
  box = np.int0(box)

  # Retrieve the key parameters of the rotated bounding box
  center = (int(rect[0][0]),int(rect[0][1]))
  width = int(rect[1][0])
  height = int(rect[1][1])
  angle = int(rect[2])


  if width < height:
    angle = 90 - angle
  else:
    angle = -angle
  if angle <0:
    angle=-angle
    angle=180-angle
  label = "Angle: " + str(angle) + " deg"
  textbox = cv2.rectangle(img, (center[0]-35, center[1]-25),
    (center[0] + 100, center[1] + 10), (255,255,255), -1)
  cv2.putText(img, label, (center[0]-50, center[1]),
    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, cv2.LINE_AA)
  cv2.drawContours(img,[box],0,(0,0,255),2)

cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
