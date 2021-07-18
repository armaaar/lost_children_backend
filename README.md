# lost_children_backend

The frontend for the lost children project. This project uses [django](https://www.djangoproject.com/).

## Prerequisites

First, make sure you have [Python](https://www.python.org/) installed. Python 3 is recommended.

This project uses [pipenv](https://pypi.org/project/pipenv/) to manage packages and versions. Refer to their [installation](https://github.com/pypa/pipenv#installation) section to know how to install it.

## Setup

1. Create `.env` file in the project root with the required environment variables. See `.env.example` for list of environment variables.

2. Activate the virtual environment using `pipenv shell`

3. Install all packages: `pipenv install`

## Useful scripts

### `pipenv` commands

- Activate virtual environment:

```bash
pipenv shell
```

- Install all pacakges for this project:

```bash
pipenv install
```

- install a package:

```bash
# Install a normal dependancy:
pipenv install mypackage

# Install a dev dependency:
pipenv install mypackage --dev
```

- Create requirements.txt if needed:

```bash
pipenv lock -r > requirements.txt
```

### `django` commands

Don't forget to activate the virtual environment first. For full list of commands, refer to [manage.py documentation](https://docs.djangoproject.com/en/3.2/ref/django-admin/)

- Run the development server:

```bash
python manage.py runserver
```

- Create a new app (module):

```bash
python manage.py startapp module_name
```

- Create a migration:

```bash
python manage.py makemigrations module_name
```

- Migrate database:

```bash
python manage.py migrate
```

- Create a superuser for admin interface:

```bash
python manage.py createsuperuser
```

- Check app for errors:

```bash
python manage.py check
```

## Troubleshooting

Most of the problems you might face will mostly be because you are not using the right virual environment or that you didn't install the required packages. Make sure your IDE using the correct interpretter from your venv. You can get the path to the venv interpretter using:

```bash
pipenv --py
```

## TODO list
