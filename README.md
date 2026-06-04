# 🚀 CareerOS

A full-stack Django-based Career Management Platform designed to help users organize and track their professional growth in one place.

## 🌐 Live Demo

**Live Application:** https://careeros-4rkb.onrender.com

---

## 📌 Features

### 🔐 Authentication

* User Registration
* User Login & Logout
* Secure Authentication System
* Custom User Model

### 👤 Profile Management

* Create and Update Profile
* Upload Profile Picture
* Add Bio, Location, Contact Information
* GitHub & LinkedIn Integration

### 💼 Job Application Tracker

* Add Job Applications
* Track Application Status
* Store Company Information
* Manage Application Dates

### 📄 Resume Management

* Upload Multiple Resumes
* View Resume Details
* Download Resume Files
* Organize Resume Versions

### 🎤 Interview Tracker

* Schedule Interviews
* Track Interview Status
* Store Interview Notes
* Manage Upcoming Interviews

### 🎯 Goal Management

* Create Career Goals
* Track Progress
* Update Goal Status
* Monitor Achievement Progress

### 📚 Learning Tracker

* Track Courses and Certifications
* Monitor Learning Progress
* Manage Learning Resources
* Record Completion Status

### 📊 Dashboard

* Career Analytics Overview
* Application Statistics
* Interview Statistics
* Goal Tracking Summary
* Learning Progress Overview

---

## 🛠️ Tech Stack

### Backend

* Python
* Django 6

### Database

* MySQL (Development)
* PostgreSQL (Production)

### Frontend

* HTML5
* CSS3
* JavaScript

### Deployment

* Render
* WhiteNoise
* Gunicorn

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
CareerOS
│
├── accounts/
├── dashboard/
├── profiles/
├── jobs/
├── resumes/
├── interviews/
├── goals/
├── learning/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
├── media/
├── config/
│
├── requirements.txt
├── Procfile
├── build.sh
└── manage.py
```

---

## ⚙️ Local Setup

### Clone Repository

```bash
git clone <repository-url>
cd CareerOS
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

---

## 🚀 Deployment

The application is deployed on Render using:

* PostgreSQL Database
* Gunicorn
* WhiteNoise
* Environment Variables
* Automated GitHub Deployments

---

## 🎯 Future Enhancements

* Email Notifications
* Resume Analysis using AI
* Job Recommendation Engine
* Interview Preparation Assistant
* Django REST API
* Mobile Responsive Enhancements

---

## 👨‍💻 Author

**Suraj Sharma**

Python Developer | Django Developer

GitHub: https://github.com/your-github-username

LinkedIn: https://linkedin.com/in/your-linkedin-profile
