# Description

This project is a task management application (ToDoList) written in Python.
It is designed following the MVC (Model-View-Controller) pattern and uses object-oriented programming to structure tasks and interactions.
The project can run in CLI mode or through a Flask API to test HTTP routes.


# Path of file and folder

todolist/
│
├── models/
│   └── task.py           # Definition of the Task class
│
├── views/
│   └── cli_view.py       # Command-line interface
│
├── controllers/
│   └── task_controller.py # Task list management
│
├── main.py               # Main entry point (CLI)
│
└── app.py                # Flask API application

# clone repository

git clone <project_url>
cd todolist


# Install dependencies

pip install flask #install flask

pip install -r # Install all requirement

# Run cli mode in interface

python main.py


# Run flask API Mode

python main.py


Access the API at: http://127.0.0.1:5000

Available routes:

GET / → Welcome message

POST /add → Add a task (requires JSON body with "title")

GET /tasks → List all tasks

DELETE /delete/<index> → Delete a task by index


# Features
Add, list, and delete tasks

MVC architecture for clean separation of concerns

Object-oriented design with reusable components

Dual interface: CLI and RESTful API

# Author

Project created for learning Python, MVC design, and Flask API development. Perfect for beginners exploring backend architecture and HTTP routing.



