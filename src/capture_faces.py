import cv2 # type: ignore
import os
import sys

roll = sys.argv[1]
name = sys.argv[2]

folder = f"data/dataset/{roll}_{name}"
os.makedirs(folder, exist_ok=True)

cam = cv2.VideoCapture(0)
count = 0

print("Capturing faces... Press ESC to stop")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Capture Face", frame)
    cv2.imwrite(f"{folder}/{count}.jpg", frame)
    count += 1

    if cv2.waitKey(1) == 27 or count >= 50:
        break

cam.release()
cv2.destroyAllWindows()
print("Face data saved")
