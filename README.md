# 📝 Notes App

A secure and user-friendly note-taking web application built with Python Flask. This application allows users to create accounts, log in securely, and manage their personal notes with full CRUD functionality. ✨

## 📋 Table of Contents
- [✨ Features](#-features)
- [📦 Prerequisites](#-prerequisites)
- [🚀 Installation](#-installation)
- [💻 Usage](#-usage)
- [📸 Screenshots](#-screenshots)
- [📁 Project Structure](#-project-structure)
- [🔒 Security Features](#-security-features)
- [🌐 API Endpoints](#-api-endpoints)
- [🗄️ Database Schema](#️-database-schema)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🕒 Last Updated](#-last-updated)

## ✨ Features

- **👤 User Authentication**: Secure user registration and login system
- **🔐 Password Security**: Passwords are hashed using PBKDF2:SHA512 algorithm
- **📝 Personal Notes**: Create, view, and delete personal notes
- **🎯 Session Management**: Secure user session handling with Flask-Login
- **📱 Responsive Design**: Clean and intuitive web interface
- **💾 SQLite Database**: Lightweight database for storing user data and notes
- **⚡ Real-time Feedback**: Flash messages for user actions and validation

## 📦 Prerequisites

Before running this application, make sure you have the following installed:

- **🐍 Python 3.7 or higher**
- **📦 pip** (Python package installer)
- **🔧 Git** (for cloning the repository)
- **🌐 Web browser** (Chrome, Firefox, Safari, etc.)

## 🚀 Installation

Follow these step-by-step instructions to set up the Notes App on your local machine:

1. **📥 Clone the repository:**
   ```bash
   git clone https://github.com/DrAlgoStrange/Notes-Web-App.git
   cd Notes-Web-App
   ```

2. **🏠 Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **⚡ Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **📋 Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **🎬 Run the application:**
   ```bash
   python main.py
   ```

6. **🌐 Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`

## 💻 Usage

### 🎯 Getting Started

1. **👤 Create an Account:**
   - Navigate to the signup page
   - Enter your name, email, and password (minimum 7 characters)
   - Confirm your password
   - Click "Sign Up" to create your account

2. **🔑 Login:**
   - Go to the login page
   - Enter your registered email and password
   - Click "Login" to access your notes

3. **📝 Managing Notes:**
   - **➕ Create Notes**: Use the text area on the home page to write your note and click submit
   - **👀 View Notes**: All your notes are displayed on the home page with timestamps
   - **🗑️ Delete Notes**: Click the delete button next to any note to remove it

### 💡 Examples

- **✨ Creating a new note:**
  Simply type your note in the text area and submit. Notes can be up to 100,000 characters long.

- **🔍 User validation:**
  The app validates email formats and ensures passwords are secure before account creation.

## 📸 Screenshots

### 🔑 Login Page
![Login Page](./screenshots/login-page.png)
*Secure login interface with email and password validation*

### 📝 Registration Page
![Signup Page](./screenshots/signup-page.png)
*User registration with password confirmation and validation*

### 🏠 Home Dashboard
![Home Page](./screenshots/home-page.png)
*Main dashboard showing user notes with create and delete functionality*

### ✅ Note Creation
![Note Creation](./screenshots/note-creation.png)
*Creating a new note with real-time feedback*


## 📁 Project Structure

```
📁 Notes App/
├── 🌐 website/
│   ├── ⚙️ __init__.py          # App factory and configuration
│   ├── 🔐 auth.py              # Authentication routes (login/signup/logout)
│   ├── 👀 views.py             # Main application routes
│   ├── 🗄️ models.py            # Database models (User, Notes)
│   ├── 🎨 templates/           # HTML templates
│   │   ├── 📄 base.html
│   │   ├── 🏠 home.html
│   │   ├── 🔑 login.html
│   │   └── 📝 signup.html
│   └── 📦 static/              # CSS, JS, and other static files
├── 💾 instance/
│   └── 🗃️ database.db          # SQLite database file
├── 🎬 main.py                  # Application entry point
├── 📋 requirements.txt         # Python dependencies
└── 📖 README.md               # Project documentation
```

## 🔒 Security Features

- **🔐 Password Hashing**: User passwords are securely hashed using PBKDF2:SHA512 algorithm
- **🛡️ Session Management**: Flask-Login handles user sessions securely
- **✅ Input Validation**: Email format validation and password strength requirements
- **🚫 SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection attacks
- **🔒 User Authorization**: Users can only view and modify their own notes

## 🌐 API Endpoints

### 🔐 Authentication Routes (`/auth/`)
- `GET/POST 🔑 /auth/login` - User login page and authentication
- `GET/POST 📝 /auth/signup` - User registration page and account creation
- `GET 🚪 /auth/logout` - User logout (requires authentication)

### 🏠 Main Application Routes (`/`)
- `GET/POST 📋 /` - Home page with note creation and display (requires authentication)
- `POST 🗑️ /delete-note` - Delete a specific note (AJAX endpoint, requires authentication)

## 🗄️ Database Schema

### 👤 User Table
- `🆔 id` (Integer, Primary Key) - Unique user identifier
- `📛 name` (String, 200 chars) - User's display name
- `📧 email` (String, 100 chars, Unique) - User's email address
- `🔐 password` (String, 500 chars) - Hashed password

### 📝 Notes Table
- `🆔 id` (Integer, Primary Key) - Unique note identifier
- `📄 data` (String, 100,000 chars) - Note content
- `🕒 date` (DateTime) - Note creation timestamp
- `👤 user_id` (Integer, Foreign Key) - Reference to user who created the note

## 🤝 Contributing

Contributions are welcome! Here's how you can help: 🎉

1. **🍴 Fork the repository**
2. **🌟 Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **💾 Make your changes and commit:**
   ```bash
   git commit -m "Add your feature description"
   ```
4. **📤 Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **📨 Create a Pull Request**

### 📋 Development Guidelines
- ✅ Follow PEP 8 style guidelines for Python code
- 💬 Add comments for complex functionality
- 🧪 Test your changes thoroughly before submitting
- 📖 Update documentation if necessary

## 👏 Credits

Thanks to the following technologies and libraries that made this project possible:
- **🌶️ Flask** - Web framework for Python
- **🗄️ Flask-SQLAlchemy** - SQLAlchemy integration for Flask
- **🔑 Flask-Login** - User session management
- **🔧 Werkzeug** - Password hashing utilities
- **💾 SQLite** - Lightweight database engine

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. ⚖️

### 📋 Third-Party Licenses
This project uses the following third-party libraries:
- 🌶️ Flask (BSD-3-Clause License)
- 🗄️ Flask-SQLAlchemy (BSD License)
- 🔑 Flask-Login (MIT License)

## 🕒 Last Updated

This README was last updated on August 25, 2025. 📅

---
