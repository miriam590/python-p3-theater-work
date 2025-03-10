# Theater Auditions Manager

##  Project Overview
The **Theater Auditions Manager** is a command-line application that manages auditions and roles for a theater production. It uses **SQLAlchemy ORM** to interact with an SQLite database, allowing users to track actors, their auditions, and the roles they are assigned to.

## Tech Stack
- **Python** 
- **SQLAlchemy** (ORM & Migrations)
- **SQLite** (Database)
- **CLI (Command-Line Interface)**

## Project Structure
```
📁 python-p3-defining-schema-with-sqlalchemy
│── app.py          # Main CLI application
│── models.py       # Database models using SQLAlchemy
│── database.py     # Database connection & initialization
│── debug.py        # Debugging & troubleshooting
│── README.md       # Project documentation
```

##  Installation & Setup
### 1 Clone the repository
```s
git clone git@github.com:miriam590/python-p3-theater-work.git
cd python-p3-defining-schema-with-sqlalchemy
```

### 2️ Create a Virtual Environment & Install Dependencies
```sh
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️ Initialize the Database
```sh
python database.py
```

##  Usage
### Running the CLI App
```sh
python app.py
```
### Available Commands:
- **Create Roles & Auditions**
- **View All Roles & Assigned Actors**
- **Assign Auditioned Actors to Roles**
- **Find the Lead & Understudy for a Role**

##  Debugging
To enable **interactive debugging**, use:
```sh
python debug.py
```

##  Features
-  **Create, Read, Update, Delete (CRUD) operations** for Roles & Auditions
-  **ORM-powered data handling** for structured queries
-  **CLI-driven interface** for seamless interaction
-  **SQLite database persistence**


##  Contact
For any issues or contributions, reach out via GitHub: https://github.com/miriam590/python-p3-theater-work.git

