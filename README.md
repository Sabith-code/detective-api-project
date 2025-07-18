# 🕵️ Detective Case Management System

## 🕵️ Project Overview

This project is a **custom API-powered detective case management system** that enables users (detectives) to seamlessly create, read, update, and delete information related to **cases**, **clues**, and **suspects**. It combines a lightweight, responsive frontend with a powerful Flask backend, allowing for smooth interaction and real-time updates.

Whether it's a high-profile bank robbery or a mysterious disappearance, detectives can use this tool to:

-  Organize multiple investigation cases  
-  Collect and track important clues  
- Maintain lists of potential suspects  

---

## 🔧 Technical Highlights

- **Backend**: Built using **Flask** and connected to a **MongoDB** database to store structured investigation data.
- **Frontend**: Clean and intuitive UI using plain **HTML, CSS, and JavaScript** — no complex frameworks.
- **API Design**: Fully custom RESTful API supporting all CRUD operations:
  - Create, retrieve, update, and delete **cases**
  - Add and list **clues** tied to specific cases
  - Add and list **suspects** associated with each case
- **API Testing**: Endpoints can be tested using tools like `curl`, Postman, or your browser.
- Integrated API Testing using [Keploy](https://keploy.io)
- CI/CD pipeline using GitHub Actions

---

## 🎯 Learning Outcomes:

- Understanding **REST API** development from scratch
- Practicing **CRUD operations** with a NoSQL database
- Integrating backend APIs with a **dynamic frontend**
- Building modular, maintainable code with clear separation of concerns

---

## 🌐 Real-World Use Case

Imagine you're a detective managing dozens of open cases — each with unique clues, suspects, and evolving descriptions. This app provides a simple, digital evidence board you can use to log discoveries, track leads, and focus your investigation.


## 📌 Features

-  Create, Read, Update, Delete (CRUD) for:
- Cases
- Clues (linked to cases)
- Suspects (linked to cases)
-  Powered by Flask + MongoDB backend
- RESTful API endpoints for integration
- Testing: Keploy API Testing Suite
- CI/CD: GitHub Actions

---

## Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python (Flask)    |
| Database  | MongoDB (local or Atlas) |
| API Style | REST              |

---
## How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sabith-code/detective-api-project.git
cd detective-api-project
```
### Step 2: Create & Activate Virtual Environment

```bash
python -m venv venv
```
Then activate:
## Windows:
```bash
venv\Scripts\activate
```
### macOS/Linux:
```bash
source venv/bin/activate
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Set Up MongoDB
Make sure MongoDB is running locally or use MongoDB Atlas.

Create a .env file in the root folder:
```bash
MONGO_URI=mongodb://localhost:27017
```
### Step 5: Run the Flask Server
```bash
python app.py
```
### Step 6: Open the Frontend
```bash
static/index.html
```


### 🔗 API Endpoints

### 🧳 Cases
| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | /cases         | List all cases      |
| POST   | /cases         | Create new case     |
| PUT    | /cases/:id     | Update case by ID   |
| DELETE | /cases/:id     | Delete case by ID   |

# Example: Create a New Case
```json
{
  "title": "Museum Robbery",
  "description": "Priceless painting stolen from museum"
}
```
### 🧩 Clues endpoints
| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| GET    | /clues/:case_id  | Get all clues for case  |
| POST   | /clues           | Add new clue to a case  |

# Example: Add a Clue
```json
{
  "case_id": "REPLACE_WITH_CASE_ID",
  "detail": "Security footage at 2:00 AM"
}
```

###  Suspects endpoints
| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | /suspects/:case_id | Get all suspects for case  |
| POST   | /suspects          | Add new suspect to a case  |

# Example: Add a Suspect
```json
{
  "case_id": "REPLACE_WITH_CASE_ID",
  "name": "John Doe"
}
```
---

##   Testing API with curl

## Create a Case

```bash
curl -X POST http://localhost:5000/cases \
  -H "Content-Type: application/json" \
  -d '{"title": "Bank Heist", "description": "Vault cracked at midnight"}'
```
## Get All Cases
```bash
curl http://localhost:5000/cases
```

## Add a Clue
```bash
curl -X POST http://localhost:5000/clues \
  -H "Content-Type: application/json" \
  -d '{"case_id": "your_case_id", "detail": "Crowbar found at scene"}'
```
## Add a Suspect
```bash
curl -X POST http://localhost:5000/suspects \
  -H "Content-Type: application/json" \
  -d '{"case_id": "your_case_id", "name": "Masked Robber"}'
```
## Delete a Case
```bash
curl -X DELETE http://localhost:5000/cases/your_case_id
```
## .gitignore
Your .gitignore file should include:
```bash
.env
venv/
__pycache__/
*.pyc
```
# Testing & Coverage
This project includes comprehensive test coverage using Pytest, ensuring the correctness and reliability of the API server.

## Types of Tests Implemented
### Unit Tests:
Tested core logic and validation functions, with and without mocking the database.

### Integration Tests:
Verified interactions between the Flask API and MongoDB database for CRUD operations.

### API Tests:
Ensured that all REST API endpoints behave correctly for valid and invalid inputs.

### Testing Tools & Frameworks

- **pytest**: For writing and running unit, integration, and API tests
- **pytest-cov**: To measure test coverage
- **unittest.mock**: Used for mocking MongoDB in isolated unit tests

### Test Coverage Achieved
Achieved over 90% code coverage, including edge cases and error handling.
Below is a screenshot from the generated HTML coverage report:

## Running Tests

### To run all tests:
```bash
pytest
```
### To check test coverage:
```bash
pytest --cov=backend tests/
```
### To generate an HTML report:
```bash
coverage html
```
Then open the report at htmlcov/index.html in your browser.

# Test Coverage

![Test Coverage](docs/Screenshot%202025-06-23%20195748.png)

##  Keploy API Testing

This project uses **Keploy** to automatically capture and replay API test cases from real requests and responses.

### ✅ Test Report Screenshot

![Keploy Test Report](/docs/Screenshot%202025-06-28%20113242.png)

---


## CI/CD Integration

This project is tested automatically using **GitHub Actions** on every push or pull request to `main`.

### ✅ Status

![CI/CD Pipeline](/docs/Screenshot%20(51).png)



🔗 [View GitHub Actions CI/CD Config](https://github.com/Sabith-code/detective-api-project/blob/main/.github/workflows/keploy.yml)

![CI/CD Pipeline](https://github.com/Sabith-code/detective-api-project/actions/workflows/keploy.yml/badge.svg)
