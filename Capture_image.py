import cv2
import matplotlib.pyplot as plt

cap = cv2.cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False

image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.title("Captured Image")
plt.show()

cap.release()