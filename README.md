#Yatube social network API project#
###About:
The Yatube project is a social network in which users have the opportunity to create an account, publish entries, subscribe to their favorite authors and mark their favorite entries. In this project, an interface for exchanging data from the Yatube social network is implemented. It provides clients with access to the database. The data is transmitted in JSON format.
###Developers:
- [Iskander Ryskulov](https://github.com/IskanderRRR)

###Applied technologies:
- Python 3
- Django Rest Framework
- Git
- Pytest

### Cloning a repository and switching to it on the command line:
`https://github.com/IskanderRRR/api_final_yatube.git`

`cd api_final_yatube`

### Cоздать и активировать виртуальное окружение:
Виртуальное окружение должно использовать Python 3.7

`pyhton -m venv venv`

- Если у вас Linux/MacOS
`source venv/bin/activate`

- Если у вас windows
`source venv/scripts/activate`

### Установка зависимостей из файла requirements.txt:
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`

### Выполнить миграции:
`python manage.py migrate`
### Запуск проекта:
`python manage.py runserver`
