# Facial Recognition Based Attendance Management System
Desktop app that marks student attendance automatically using face recognition. MCA Sem-1 team project (3 members).

## Features
- Teacher/Admin login
- Student registration with 25 webcam face samples
- Real-time face detection (Haar Cascade) and recognition (LBPH)
- Auto Present/Absent marking with date, time, subject, teacher
- Subject-wise attendance stored in CSV
- Charts: bar, pie, histogram, monthly/weekday, per-student %
- Admin panel to manage teachers and students

## Tech Stack
Python, OpenCV, Tkinter, Pandas, NumPy, Matplotlib, Pillow, tkcalendar

## How to Run
pip install -r requirements.txt
python app.py

## Note
Face dataset is not included for privacy reasons.