import cv2 # type: ignore
import numpy as np
import pandas as pd
from datetime import datetime
import os

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/trainer.yml")

labels = np.load("models/labels.npy", allow_pickle=True).item()

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

attendance_file = "data/attendance.csv"

# Create attendance file if not exists
if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["Student", "Date", "Time"]).to_csv(attendance_file, index=False)

cam = cv2.VideoCapture(0)
today = datetime.now().strftime("%Y-%m-%d")

print("Starting attendance system... Press ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        label_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # ❌ reject very small faces (noise / false match)
        if w < 80 or h < 80:
            student = "Unknown"
            color = (0, 0, 255)

        # ✅ accept only strong matches
        elif confidence < 45 and label_id in labels:
            student = labels[label_id]
            color = (0, 255, 0)

            df = pd.read_csv(attendance_file)

            # Avoid duplicate entry for same day
            if not ((df["Student"] == student) & (df["Date"] == today)).any():
                time_now = datetime.now().strftime("%H:%M:%S")
                df.loc[len(df)] = [student, today, time_now]
                df.to_csv(attendance_file, index=False)

        else:
            student = "Unknown"
            color = (0, 0, 255)

        # Show name + confidence (debug + viva)
        text = f"{student} ({int(confidence)})"

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

    cv2.imshow("Live Attendance System", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cam.release()
cv2.destroyAllWindows()

print("Attendance process completed")
