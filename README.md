# Angle-Detection (PCA)

The second implementation of angle detection of object in images (using PCA)

Orientation.py:
It constructs a data array (data_pts) with the (x, y) coordinates of the contour points and then performs PCA analysis on the data points to find the principal components, i.e., the eigenvectors and eigenvalues. We then calculate the center (cntr) of the detected object followed by drawing the principal components as lines on the original image to visualize the orientation.

It calculates the angle of the orientation in radians (angle) later converted to degree in main.py

Find Axes.py
The drawAxis function is used to draw an arrow to visualize the orientation angle of a contour in an image. It takes the image, start point p_, end point q_, color, and scale as input parameters and draws the arrow between the start and end points with the specified color and thickness. The arrow represents the orientation angle between the two points.
