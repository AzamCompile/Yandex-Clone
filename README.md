# 🚀 Yandex Clone (Django Project)

Bu loyiha — Yandex ga o‘xshash web platforma kloni bo‘lib, Django framework asosida yaratilgan. Unda user authentication, Google login, product CRUD va admin panel mavjud.

---

## 🧩 Texnologiyalar

- Python 3.11+
- Django 6+
- Django Allauth (Google OAuth)
- SQLite / PostgreSQL
- HTML, CSS (Bootstrap)
- JavaScript

---

## 📌 Asosiy funksiyalar

### 👤 User system
- Email orqali login/register
- Google OAuth login
- Custom User model (username o‘chirib tashlangan)

### 🛍 Products
- Product yaratish (Create)
- O‘qish (List / Detail)
- O‘chirish (Delete)
- Yangilash (Update)

### 🔐 Admin panel
- Django admin orqali boshqaruv
- Superuser yaratish

### 🌐 Authentication
- Django Allauth orqali Google login
- Session based auth

---

## ⚙️ O‘rnatish

### 1. Repositoryni clone qiling:
```bash
git clone https://github.com/AzamCompile/Yandex-Clone
cd yandex-clone 

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

python manage.py createsuperuser


python manage.py runserver