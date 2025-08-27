from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://face-attendence-real-tim-30208-default-rtdb.firebaseio.com/'
})

ref = db.reference('students')
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = {
    "223715": {
        "Name": "Dipanshu Mishra",
        "Major": "MSC IT",
        "Session": "2022-24",
        "Total Attendance": 0,
        "Standing": 'Good',
        "year": 2,
        "Last_attendance_time": current_time
    },
    "223726": {
        "Name": "Pravish Pandey",
        "Major": "MSC IT",
        "Session": '2022-24',
        "Total Attendance": 0,
        "Standing": 'Bad',
        "year": 2,
        "Last_attendance_time": current_time
    },
    "223732": {
        "Name": "Ananya Chhavi",
        "Major": "MSC IT",
        "Session": '2022-24',
        "Total Attendance": 0,
        "Standing": 'Bad',
        "year": 2,
        "Last_attendance_time": current_time
    }
    # add more students...
}

for key, value in data.items():
    ref.child(key).set(value)

print("Student data added to Firebase Realtime Database.")
