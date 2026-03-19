# Django Todo App 🚀

A full-featured Todo application built with Django, PostgreSQL, and Docker.
Includes a REST API ready to connect with a React frontend.

## 📋 About the Project

A backend web application that allows users to:
- Create and manage personal todo lists
- Organize todos into categories
- Register, login, and manage their account securely
- Access all features via a REST API

## 🛠️ Tech Stack

- **Backend:** Django 6.0, Python 3.13
- **Database:** PostgreSQL 16
- **API:** Django REST Framework
- **Containerization:** Docker & Docker Compose
- **Authentication:** Django built-in auth system

## 🚀 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository
```bash
   git clone https://github.com/Khamis-Mdeghi/django-todo-app.git
   cd django-todo-app
```

2. Create a `.env` file in the root directory
```
   SECRET_KEY=your_secret_key_here
   DB_NAME=django_db
   DB_USER=django_user
   DB_PASSWORD=your_password
   DB_HOST=db
   DB_PORT=5432
```

3. Build and run with Docker
```bash
   docker-compose up --build
```

4. Create a superuser
```bash
   docker-compose exec web python manage.py createsuperuser
```

5. Visit the app
```
   http://127.0.0.1:8000/todos/
```

## 📡 API Endpoints

### Todos
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos/api/` | Get all todos |
| POST | `/todos/api/` | Create a todo |
| GET | `/todos/api/<id>/` | Get one todo |
| PUT | `/todos/api/<id>/` | Edit a todo |
| DELETE | `/todos/api/<id>/` | Delete a todo |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos/api/categories/` | Get all categories |
| POST | `/todos/api/categories/` | Create a category |
| GET | `/todos/api/categories/<id>/` | Get one category |
| PUT | `/todos/api/categories/<id>/` | Edit a category |
| DELETE | `/todos/api/categories/<id>/` | Delete a category |

### Example Response
```json
{
    "id": 1,
    "title": "Learn Django",
    "description": "Study Django framework",
    "completed": false,
    "created_at": "2026-03-19T12:00:00Z",
    "category": 2,
    "category_name": "Study"
}
```

## ✨ Features

- ✅ Full CRUD for todos and categories
- ✅ User authentication (register, login, logout)
- ✅ Password change and reset via email
- ✅ Each user sees only their own todos
- ✅ REST API for frontend integration
- ✅ Dockerized for easy setup
- ✅ PostgreSQL database

## 🔜 Coming Soon

- React frontend integration
- Deployment to production
- Todo filtering by category

## 👨‍💻 Author

**Khamis Mdeghi**
- GitHub: [@Khamis-Mdeghi](https://github.com/Khamis-Mdeghi)
