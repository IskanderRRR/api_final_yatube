# Yatube social network API project#
### About:
The Yatube project is a social network in which users have the opportunity to create an account, publish entries, subscribe to their favorite authors and mark their favorite entries. In this project, an interface for exchanging data from the Yatube social network is implemented. It provides clients with access to the database. The data is transmitted in JSON format.
### Developers:
- [Iskander Ryskulov](https://github.com/IskanderRRR)

### Applied technologies:
- Python 3
- Django Rest Framework
- Git
- Pytest

### Cloning a repository and switching to it on the command line:
`https://github.com/IskanderRRR/api_final_yatube.git`

`cd api_final_yatube`

### Create and activate virtual environment:

The virtual environment must use Python 3.7

`pyhton -m venv venv`

- Linux/MacOS

`source venv/bin/activate`

- Windows

`source venv/scripts/activate`

### Installing dependencies from the requirements.txt file:
`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

### Run migrations:
`python manage.py migrate`
### Run project:
`python manage.py runserver`
