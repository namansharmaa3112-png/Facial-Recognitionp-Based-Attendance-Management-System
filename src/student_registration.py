import pandas as pd
import os

file_path = "data/students.csv"

def register_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["StudentID", "Name"])

    if sid in df["StudentID"].values:
        print("Student already registered!")
        return

    new_data = pd.DataFrame([[sid, name]], columns=["StudentID", "Name"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

    print("Student Registered Successfully")

register_student()
