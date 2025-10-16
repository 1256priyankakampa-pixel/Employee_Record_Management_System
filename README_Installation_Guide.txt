===========================================================
EMPLOYEE RECORD SYSTEM - INSTALLATION GUIDE
===========================================================

1. PROJECT OVERVIEW
-----------------------------------------------------------
The Employee Record System is a web application built using Flask and SQLite.
It allows users to manage employee information including name, department,
and salary through a simple web interface. The system supports full CRUD
operations: Create, Read, Update, and Delete.

-----------------------------------------------------------
2. PREREQUISITES
-----------------------------------------------------------
Before running this application, make sure you have:
- Python 3.13 or above installed
- pip (Python package manager)
- Visual Studio Code or any IDE
- Internet connection to install dependencies

-----------------------------------------------------------
3. SETUP STEPS
-----------------------------------------------------------

a. Clone or Download the Project
   Option 1: If using Git
      git clone https://github.com/yourusername/employee-record-system.git

   Option 2: If downloaded as ZIP
      - Extract it anywhere on your computer
      - Open it in VS Code

b. Navigate to the Project Folder
      cd Project1_Employee_Record_System

c. Create and Activate a Virtual Environment
      python -m venv venv
      venv\Scripts\activate      (for Windows)

d. Install Dependencies
      pip install -r requirements.txt

-----------------------------------------------------------
4. DATABASE SETUP
-----------------------------------------------------------
To create the SQLite database, open Python shell in terminal:
      python

Then run the following:
-----------------------------------------------------------
import sqlite3
conn = sqlite3.connect('employees.db')
conn.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER)')
conn.close()
exit()
-----------------------------------------------------------

This will create a new file named "employees.db" in your project folder.

-----------------------------------------------------------
5. RUN THE APPLICATION
-----------------------------------------------------------
To start the Flask server:
      python app.py

Once running, open the following URL in your browser:
      http://127.0.0.1:5000/

-----------------------------------------------------------
6. FEATURES
-----------------------------------------------------------
- Add Employee
- View Employee List
- Edit Employee Details
- Delete Employee Record
- Data stored in SQLite database

-----------------------------------------------------------
7. FILE STRUCTURE
-----------------------------------------------------------
Project1_Employee_Record_System/
│
├── app.py
├── employees.db
├── requirements.txt
├── README_Installation_Guide.txt
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
└── static/
    └── style.css

-----------------------------------------------------------
8. HOW TO STOP THE SERVER
-----------------------------------------------------------
Press CTRL + C in your terminal window.

-----------------------------------------------------------
9. AUTHOR & TECHNOLOGIES
-----------------------------------------------------------
Developed by: Priyanka Kampa
Year: 2014
Technologies: Python | Flask | SQLite | HTML | CSS
IDE: Visual Studio Code

===========================================================
