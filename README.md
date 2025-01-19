# To-Dos Flask App

The repository is a basic to-dos app made with `flask`, implementing CRUD with `flask-sqlalchemy` and a authentication with `flask-login`. The app have considerable simple templates due it was focused on learning CRUD Operations with the mentioned libraries.

## Instalation

Firstly, to install the app you need to have [Python 3](https://www.python.org/) and pip installed on your system. Then, follow the steps below.

1. Clone the repository

```bash
git clone https://github.com/Estebyte/TodosFlaskApp.git
cd TodosFlaskApp
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Database Setup

1. Set Flask app
```bash
cd app
export FLASK_APP=app.py    # On Windows: set FLASK_APP=app.py
```

2. Initialize migrations (only for the first time)
```bash
flask db init
```

3. Create initial migrations
```bash
flask db migrate -m "Initial migration"
```

4. Apply migrations
```bash
flask db upgrade
```

## Run the app

Execute `run.py` or in the console
```bash
flask run
```

## Contributing

Pull request are welcome. I am a student, and I am open to any contributions or sugestions.