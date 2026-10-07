from flask import Flask, render_template, request, redirect, flash
import pandas as pd
import os
import subprocess

app = Flask(__name__)
app.secret_key = "attendance_secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMIN_FILE = os.path.join(BASE_DIR, "data", "admin.csv")
STUDENT_FILE = os.path.join(BASE_DIR, "data", "students.csv")
PYTHON_PATH = r"C:\ProgramData\anaconda3\python.exe"

os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)

if not os.path.exists(ADMIN_FILE):
    pd.DataFrame(columns=["username", "password", "email"]).to_csv(ADMIN_FILE, index=False)

if not os.path.exists(STUDENT_FILE):
    pd.DataFrame(columns=["roll", "name", "course", "year", "semester", "subject"]).to_csv(STUDENT_FILE, index=False)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        df = pd.read_csv(ADMIN_FILE)
        if ((df["username"] == request.form["username"]) &
            (df["password"] == request.form["password"])).any():
            return redirect("/dashboard")
        flash("Invalid credentials")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        df = pd.read_csv(ADMIN_FILE)
        if (df["username"] == request.form["username"]).any():
            flash("Admin already exists")
        else:
            df.loc[len(df)] = [
                request.form["username"],
                request.form["password"],
                request.form["email"]
            ]
            df.to_csv(ADMIN_FILE, index=False)
            flash("Admin created")
            return redirect("/")
    return render_template("signup.html")


@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    password = None
    if request.method == "POST":
        df = pd.read_csv(ADMIN_FILE)
        row = df[df["username"] == request.form["username"]]
        if not row.empty:
            password = row.iloc[0]["password"]
        else:
            flash("User not found")
    return render_template("forgot.html", password=password)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/register", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        df = pd.read_csv(STUDENT_FILE)
        df.loc[len(df)] = [
            request.form["roll"],
            request.form["name"],
            request.form["course"],
            request.form["year"],
            request.form["semester"],
            request.form["subject"]
        ]
        df.to_csv(STUDENT_FILE, index=False)

        subprocess.Popen([
            PYTHON_PATH,
            os.path.join(BASE_DIR, "src", "capture_faces.py"),
            request.form["roll"],
            request.form["name"]
        ])

        flash("Student registered & face capture started")
        return redirect("/dashboard")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
