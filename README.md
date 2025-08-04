 
# 📄 Patient Document Upload Portal

This is a full-stack PDF management system where users can upload, view, download, and delete PDF files. I built this project from scratch using React (frontend) and Django + SQLite (backend) as part of my internship assessment.

##🌟 Key Features
-------------------

- Simple and secure PDF upload system using Django REST Framework

- Fast file handling with real-time feedback (upload success/fail messages)

- 📂 Uploaded files are listed with filename, size, and action buttons

- Download and delete options work instantly from UI

- 🌐 React and Django are fully integrated with proper CORS setup

- 🎨 Clean Bootstrap styling for a user-friendly experience

- 💾 Media files stored safely in a separate `media/uploads/` folder

---

## 🚀 How to Run the Project

### ▶️ Backend (Django + SQLite)

***(bash)****

cd patient_portal
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
