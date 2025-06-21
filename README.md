# 🕵️ Detective Case Management System

This project is a full-stack application that allows detectives to manage **cases**, **clues**, and **suspects** through a clean and interactive interface.

## 📌 Features

- ✅ Create, Read, Update, Delete (CRUD) for:
  - Cases
  - Clues (linked to cases)
  - Suspects (linked to cases)
- 🎨 Modern, blog-style frontend with inline editing
- ⚡ Powered by Flask + MongoDB backend
- 🧠 RESTful API endpoints for integration

---

## 🏗️ Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python (Flask)    |
| Database  | MongoDB (local or Atlas) |
| API Style | REST              |

---

## 🔗 API Endpoints

### 🧳 Cases
| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | /cases         | List all cases      |
| POST   | /cases         | Create new case     |
| PUT    | /cases/:id     | Update case by ID   |
| DELETE | /cases/:id     | Delete case by ID   |

### 🧩 Clues
| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| GET    | /clues/:case_id  | Get all clues for case  |
| POST   | /clues           | Add new clue to a case  |

### 🕶️ Suspects
| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | /suspects/:case_id | Get all suspects for case  |
| POST   | /suspects          | Add new suspect to a case  |

---

## 🧪 Testing

You can test APIs using tools like:

```bash
curl http://localhost:5000/cases
