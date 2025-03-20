# Django Healthcare Backend

## 🚀 Project Overview
This project is a **Django REST API** for managing a **Healthcare System**, allowing users to:
- **Register/Login** using JWT authentication.
- **Manage Patients** (Create, Read, Update, Delete).
- **Manage Doctors** (Create, Read, Update, Delete).
- **Assign Doctors to Patients** (Mapping API).
- **Use PostgreSQL as the database**.

## 📌 Technologies Used
- **Django** (Backend Framework)
- **Django REST Framework (DRF)** (API Handling)
- **PostgreSQL** (Database)
- **JWT Authentication** (Secure API Access)

---

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anujyadav73/Healthcare_Backend
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```env
SECRET_KEY=your_secret_key
DATABASE_NAME=healthcare_db
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5️⃣ Apply Migrations & Create Superuser
```bash
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```
API will be available at: **http://127.0.0.1:8000/**

---

## 🛠 API Endpoints
### **1️⃣ Authentication APIs**
| Method | Endpoint | Description |
|--------|------------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login & Get JWT Token |

### **2️⃣ Patient Management APIs**
| Method | Endpoint | Description |
|--------|------------|-------------|
| `POST` | `/api/patients/` | Add a new patient (Authenticated users only) |
| `GET` | `/api/patients/` | Get all patients created by the logged-in user |
| `GET` | `/api/patients/<id>/` | Get details of a specific patient |
| `PUT` | `/api/patients/<id>/` | Update patient details |
| `DELETE` | `/api/patients/<id>/` | Delete a patient record |

### **3️⃣ Doctor Management APIs**
| Method | Endpoint | Description |
|--------|------------|-------------|
| `POST` | `/api/doctors/` | Add a new doctor (Authenticated users only) |
| `GET` | `/api/doctors/` | Retrieve all doctors |
| `GET` | `/api/doctors/<id>/` | Get details of a specific doctor |
| `PUT` | `/api/doctors/<id>/` | Update doctor details |
| `DELETE` | `/api/doctors/<id>/` | Delete a doctor record |

### **4️⃣ Patient-Doctor Mapping APIs**
| Method | Endpoint | Description |
|--------|------------|-------------|
| `POST` | `/api/mappings/` | Assign a doctor to a patient |
| `GET` | `/api/mappings/` | Retrieve all patient-doctor mappings |
| `GET` | `/api/mappings/<patient_id>/` | Get all doctors assigned to a specific patient |
| `DELETE` | `/api/mappings/<id>/` | Remove a doctor from a patient |

---

## 🔐 Authentication & Token Usage
1. **Register a User** (`POST /api/auth/register/`)
2. **Login to Get JWT Token** (`POST /api/auth/login/`)
3. **Use the Token in Requests**
   - Add this **header** in API requests:
   ```
   Authorization: Bearer your_access_token_here
   ```
4. **Refresh Token** (`POST /api/auth/token/refresh/`)

---

---

## 📌 Contributing
Feel free to fork this repository and submit a **pull request** with improvements! 🚀

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## ✨ Author
**Anuj Yadav**  


Happy coding! 🚀