# User Management System

A beginner-friendly full-stack project built with Python, Flask, SQLite, HTML, CSS and JavaScript.

## Features

- User registration
- User detail storage
- Email uniqueness
- Password hashing
- Login/logout
- Session-based authentication
- Dashboard
- Registered-user table
- Client-side password confirmation
- SQLite database
- Git/GitHub ready

## User details stored

- Name
- Email
- Phone
- Date of birth
- Gender
- City
- Password hash
- Account creation time

## Run locally

### 1. Create and activate virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically as `database.db`.

## GitHub

Before pushing:

```bash
git init
git add .
git commit -m "Initial user management project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Security notes

This is a learning project. Before production use, change the Flask secret key, use environment variables, enable HTTPS, add CSRF protection, add stronger validation/rate limiting, and use a production database.

Never commit real user data, passwords, `.env` files, or `database.db` to GitHub.
