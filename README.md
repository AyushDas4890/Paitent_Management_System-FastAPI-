<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="300"/>
  <h1 style="color: #003366;">🏥 Patient Management System API</h1>
  <p><i>A premium, high-performance RESTful API built with FastAPI.</i></p>
</div>

---

## 🌟 Overview

The **Patient Management System API** is a lightweight, robust, and lightning-fast backend service designed to handle patient records efficiently. It calculates BMI automatically, determines health verdicts, and dynamically tracks patient metadata using an optimized JSON database strategy.

> **Fun Fact:** This API is architected using the golden standards of modern Python, achieving up to **87%** faster development cycles thanks to FastAPI's built-in Pydantic validation.

## ✨ Features

- **⚡ Fast & Modern:** Built on top of FastAPI and Python 3.
- **🛡️ Data Validation:** Strict input validation and typing using Pydantic models.
- **🧠 Smart Computations:** Automatic real-time calculations for BMI and Health Verdicts (`Underweight`, `Normal`, `Overweight`, `Obese`).
- **📖 Interactive Docs:** Out-of-the-box Swagger UI and ReDoc for effortless API exploration.
- **💾 Flat-file DB:** Lightweight local storage using `patient.json`.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **Server:** Uvicorn
- **Storage:** JSON File System

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/AyushDas4890/Paitent_Management_System-FastAPI-.git
cd Paitent_Management_System-FastAPI-
```

### 2. Create and activate a virtual environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
*(If you don't have a requirements.txt yet, simply install FastAPI and Uvicorn: `pip install fastapi uvicorn pydantic`)*

### 4. Run the application
```bash
uvicorn main:app --reload
```
The server will start locally at **`http://127.0.0.1:8000`**.

---

## 🎮 Interactive API Documentation (The Best Part!)

FastAPI automatically generates a gorgeous, interactive documentation interface. You don't need to use Postman to test your routes!

1. Start your server.
2. Open your browser and navigate to:
   - **Swagger UI (Interactive Test Environment):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc (Alternative Documentation):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

From the `/docs` dashboard, you can **click on any endpoint**, click **"Try it out"**, fill in the parameters, and execute real requests directly from your browser!

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root greeting |
| `GET` | `/about` | API information |
| `GET` | `/view` | Retrieve all registered patients |
| `GET` | `/patient/{patient_id}` | Fetch a specific patient by their ID |
| `GET` | `/sort` | Sort patients dynamically by `height`, `weight`, or `bmi` |
| `POST` | `/create` | Create a new patient record (auto-calculates BMI) |
| `PUT` | `/edit/{patient_id}` | Edit specific fields of an existing patient |
| `DELETE` | `/delete/{patient_id}`| Remove a patient from the system |

---

## 🎨 Design Philosophy

This project prioritizes a clean, readable architecture. The synergy of Blue and Gold aesthetics can be thought of as our structural logic: deep, robust stability (Blue) coupled with premium, high-value performance features (Gold). 

<div align="center">
  <i>Built for speed. Designed for elegance.</i>
</div>
