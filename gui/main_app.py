import tkinter as tk
import subprocess
import os

PYTHON_PATH = r"C:\ProgramData\anaconda3\python.exe"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_script(script_path):
    subprocess.Popen([PYTHON_PATH, script_path], cwd=BASE_DIR)

def capture_faces():
    run_script(os.path.join(BASE_DIR, "src", "capture_faces.py"))

def train_model():
    run_script(os.path.join(BASE_DIR, "src", "train_model.py"))

def start_attendance():
    run_script(os.path.join(BASE_DIR, "src", "recognize_attendance.py"))

root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("400x300")

tk.Label(root, text="Smart Attendance System",
         font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="Capture Faces",
          width=25, command=capture_faces).pack(pady=5)

tk.Button(root, text="Train Model",
          width=25, command=train_model).pack(pady=5)

tk.Button(root, text="Start Attendance",
          width=25, command=start_attendance).pack(pady=5)

tk.Button(root, text="Exit",
          width=25, command=root.destroy).pack(pady=20)

root.mainloop()
