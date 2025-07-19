# 👤📷 FACE RECOGNITION ATTENDANCE SYSTEM


An AI-powered system that automates attendance tracking using real-time face recognition. Built with Python, OpenCV, and Firebase.

---

## 📌 Features

- ✅ Real-time face detection using webcam
- ✅ Face recognition using LBPH algorithm (OpenCV)
- ✅ Firebase integration for student data and attendance logs
- ✅ Attendance records saved with date and time
- ✅ Graphical User Interface (GUI) with Tkinter
- ✅ Admin can add, delete, and track students
- ✅ Export attendance as CSV

---

## 🧰 Tech Stack

| Technology      | Purpose                            |
|-----------------|------------------------------------|
| Python          | Programming language               |
| OpenCV          | Face detection & recognition       |
| Tkinter         | GUI toolkit                        |
| Firebase (Firestore, Storage) | Cloud database & image storage |
| CSV             | Attendance export format           |
| NumPy           | Matrix operations                  |

---



---

## 🧪 How It Works

1. **Register Student**
   - Capture face image via webcam
   - Store image in `student_images/` and Firebase
   - Save name, ID in Firestore

2. **Train Model**
   - Run `train_model.py`
   - Train LBPH recognizer on stored images

3. **Mark Attendance**
   - Run `main.py`
   - Recognizes faces and marks attendance in CSV & Firebase

