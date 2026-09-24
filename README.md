# Simple Django Helpdesk Project

This is a beginner-friendly Django project for classroom demonstration.

## 1. Open the project in VS Code
Open the `django_helpdesk_simple` folder in VS Code.

## 2. Create a virtual environment (Windows)

```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Install Django

```powershell
python -m pip install -r requirements.txt
```

## 4. Run database migrations

```powershell
python manage.py migrate
```

## 5. Create an admin user (optional)

```powershell
python manage.py createsuperuser
```

## 6. Start Django

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## What this demo teaches

Browser -> URL -> View -> Model -> SQLite -> Template -> Browser

Features:
- View all tickets
- Add a ticket
- Close a ticket
- Store data in SQLite
- Manage tickets in Django admin
