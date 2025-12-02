# 🚀 AI-CRM (HCP) — Full-Stack Application

A modern CRM system powered by **FastAPI (Backend)** and **React + Redux Toolkit + Vite (Frontend)** with a clean UI inspired by professional dashboard designs.

---

## 📁 Project Structure

```
AI-CRM-HCP/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   ├── index.css
    │   ├── components/
    │   ├── pages/
    │   └── app/store.js
    ├── package.json
    └── vite.config.js
```

---

# 🖥️ Backend — FastAPI + MySQL

## ✔️ 1. Create and Activate Virtual Environment

```
cd backend
python -m venv .venv
.venv\Scripts\activate
```

## ✔️ 2. Install Dependencies

```
pip install -r requirements.txt
```

## ✔️ 3. Create `.env`

```
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/hcp_crm
```

## ✔️ 4. Run Backend Server

```
uvicorn main:app --reload
```

### ✅ Backend will run at:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
👉 API Docs: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

# 🎨 Frontend — React + Vite + Redux Toolkit

## ✔️ 1. Install Frontend Dependencies

```
cd frontend
npm install
npm install @reduxjs/toolkit react-redux axios
```

## ✔️ 2. Start Development Server

```
npm run dev
```

### ✅ Frontend will run at:

👉 **[http://localhost:5173](http://localhost:5173)**

---

# 🔗 Combined Usage

| Component             | URL                                                      |
| --------------------- | -------------------------------------------------------- |
| **Backend (FastAPI)** | [http://127.0.0.1:8000](http://127.0.0.1:8000)           |
| **FastAPI Docs**      | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| **Frontend (React)**  | [http://localhost:5173](http://localhost:5173)           |

Ensure backend is running **before** frontend, so APIs can be used.

---

# 🛠️ Frontend API Setup

Inside `src/api/axios.js`:

```js
import axios from 'axios';

export default axios.create({
  baseURL: "http://127.0.0.1:8000"
});
```

---

# 🎯 Features

### Backend

✔ FastAPI REST APIs
✔ MySQL database
✔ CRUD for contacts/leads
✔ JWT authentication (optional)
✔ CORS enabled

### Frontend

✔ Modern UI (Inter font + clean layout)
✔ Redux Toolkit store
✔ API integration with FastAPI
✔ Pages for users, leads, dashboard
✔ Loader & error handling

---

# ▶️ Running the Full Stack

### **Step 1 — Start MySQL Server**

Make sure your DB is running.

### **Step 2 — Start Backend**

```
cd backend
uvicorn main:app --reload
```

### **Step 3 — Start Frontend**

```
cd frontend
npm run dev
```

---

# 📦 Build Frontend for Production

```
npm run build
```

---

# 🤝 Contribution

Pull requests welcome. Please ensure clean commit messages.

---

# 📜 License

MIT License — Free to use and modify.

---

## 🎉 Your AI-CRM Project is Ready!

Run both servers and enjoy the fully functional CRM dashboard.
