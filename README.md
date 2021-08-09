# Cinema Ticket - A Django powered app for booking cinema tickets

There tends to be long lines for booking movie tickets at the cinema especially for new blockbuster movies.
Even having to go through the same formalities for regular movies takes some time.
This app aims to solve these problems by letting users book their movie tickets online.

## Requirements
* Python 3.7+
* Django 3.2+ and other dependencies in the Pipfile
* PostgreSQL

## Installation
After cloning the project, create a virtual environment using pipenv and run the following command:
```bash
pipenv install
```

Rename the .env.example file to .env and update the environment variables.

To create an admin user:
```bash
python manage.py createsuperuser
```
Create the database and start the server with the following commands:
```bash
python manage.py migrate

python manage.py runserver
```

## License

This project is [MIT licensed](LICENSE).