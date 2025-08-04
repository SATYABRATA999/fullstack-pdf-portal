# 🧠 Design & Architecture - Patient Document Upload Portal

## 🔧 Tech Stack

- **Frontend:** React (with Axios & Bootstrap)
- **Backend:** Django + Django REST Framework
- **Database:** SQLite
- **Storage:** Local media folder for uploaded PDFs

---

## 🌐 API Endpoints (Django)

| Method | Endpoint                      | Description              |
|--------|-------------------------------|--------------------------|
| GET    | `/api/`                       | List all uploaded PDFs   |
| POST   | `/api/upload/`                | Upload a new PDF         |
| GET    | `/api/<id>/`                  | Download/view a PDF      |
| DELETE | `/api/<id>/delete/`           | Delete a PDF             |

---

## 📁 Folder Structure

