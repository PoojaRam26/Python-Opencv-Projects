#import the opencv Library

import cv2

image = cv2.imread('dancer2.png') #read the image  and store it in a variable

print(type(image)) 

##Display the Image

cv2.imshow("Dancer",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("Dancer",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Dancer",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

output = cv2.imwrite(image)
cv2.imshow(output)