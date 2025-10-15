Description

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
│   └── task_controller.py# Task list management
│
├── main.py               # Main entry point (CLI)
│
└── app.py                # Flask API application


# install

pip install flask

# Run flask

python main.py



