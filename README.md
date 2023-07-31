# Angle-Detection

First implementation of detecting inclination and measuring angle with respect to objects in image. This method involves finding of contours after transforming image using thresholding. This is followed by computing the area of the object and hence finding out the center point of the object in question.

Using this center, we form a bounding box around the object.
We calculate angle keeping in mind that values range between 0-180 degrees.

The second implementation involves PCA analysis of the image which can be found in the PCA branch


![Screenshot 2023-07-31 154801](https://github.com/haarish04/Angle-Detection/assets/131394736/d131ecb7-5b3b-47c7-b2d5-7ab280e381a2)

![Screenshot 2023-07-31 154814](https://github.com/haarish04/Angle-Detection/assets/131394736/95bc7b4d-67a5-4f2b-8ca4-e9bb9de3abca)
