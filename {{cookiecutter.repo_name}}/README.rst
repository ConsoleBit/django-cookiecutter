===============================
{{ cookiecutter.project_name }}
===============================


{{ cookiecutter.description }}

* Free software: BSD license

Requirements
------------

* Django 2.1+
* Python 3.6


Installation
----------------------------

#. Clone the git repository.
#. Create a production.py file in {{ cookiecutter.repo_name }}/{{ cookiecutter.project_name }}/{{ cookiecutter.project_name }}/settings by copying what's in the example_production.py
    * Fill database details in the file you just created
    * Add the site admins in the ADMINS variable
    * Add server host in ALLOWED_HOSTS

#. Install all third party packages by running::

    $ pip install -r requirements/development.txt

#. Apply migrations::

    $ python manage.py migrate

