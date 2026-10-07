import cv2
import numpy as np
import os

dataset_path = "data/dataset"
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_id = 0

for folder in sorted(os.listdir(dataset_path)):
    folder_path = os.path.join(dataset_path, folder)

    # sirf directories allow
    if not os.path.isdir(folder_path):
        continue

    print(f"Training label {label_id} -> {folder}")
    label_map[label_id] = folder

    for img in os.listdir(folder_path):
        if not img.lower().endswith(".jpg"):
            continue

        img_path = os.path.join(folder_path, img)
        gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if gray is None:
            continue

        faces.append(gray)
        labels.append(label_id)

    # ✅ label increment YAHAN hota hai (per student)
    label_id += 1

recognizer.train(faces, np.array(labels))
recognizer.save("models/trainer.yml")
np.save("models/labels.npy", label_map)

print("Model trained successfully")
