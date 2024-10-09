# Flask-ToDoList

A simple and interactive To-Do List application built with Flask. It allows users to manage their tasks efficiently with a clean and user-friendly interface.

## Features

- **Add Tasks**: Easily add new tasks to your to-do list.
- **Delete Tasks**: Remove tasks that are completed or no longer needed.
- **Edit Tasks**: Edit your exising tasks.
- **Database Integration**: Persistent storage of tasks using SQLALCHEMY.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.


### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/TencoDev/Flask-ToDoList.git
cd Flask-ToDoList
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
Set up the database:
```
```bash
flask db init
flask db migrate
flask db upgrade
```

4. **Run the application:**

```bash
flask run
The app will be available at http://127.0.0.1:5000/.
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
