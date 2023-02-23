# Description

`django-orm-watching-storage` is the mini-site which brings the features to monitor peoples visits into the bank storage. It is possible to control employees within the storage perimeter.  
 

# Prerequisites

Firstly, you have to install package `python3-venv` to work with python virtual environment.

Update packages on your system `!(it depends on your operating system)`

in this document I use Ubuntu as my operating system. 

So run update:
```console
$ sudo apt update
```

and run command:
```console
$ sudo apt install -y python3-venv
```

Then jump to project folder:
```console
$ cd django-orm-watching-storage
```

and create new python environment to run the code:
```console
$ python3 -m venv venv
```

Activate new virtual environment:
```console
$ source venv/bin/activate
```

As a result, you will see command line prompt like this:
```console
(venv) django-orm-watching-storage $ 
```

# Install dependencies

In the virtual environment run command:

```console
(venv) django-orm-watching-storage $  pip install -r requirements.txt
```

This command installs `django` framework, `psycopg2` and `environs` libraries into the `venv` virtual environment.

# Setup environment variables

To redefine program behavior, in project folder create `.env` file. 

Possible options to setup are:

* `DB_ENGINE` - define database backend engine. 

Possible values are: 
```
    django.db.backends.postgresql

    django.db.backends.mysql
    
    django.db.backends.sqlite3
    
    django.db.backends.oracle
```

By default, we use PostgreSQL server engine - `django.db.backends.postgresql`

* `DB_HOST` - define database server hostname.

By default, we use `localhost` name for server connection.

* `DB_PORT` - define database server listening port.

By default, we use PostgreSQL server default port - `5432`

* `DB_NAME` - define database name to work with.

This parameter has no default value - it has to be explicitly defined.

* `DB_USER` - define database user to connect.

This parameter has no default value - it has to be explicitly defined.

* `DB_PASSWORD` - define database password to connect.

This parameter has no default value - it has to be explicitly defined.

* `SECRET_KEY` - this is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

By default, we use secret key value - `apollo84`

* `ALLOWED_HOSTS` - list of strings representing the host/domain names that this Django site can serve.

By default, we allow only localhost connections to communicate with our site - `'.localhost', '127.0.0.1'`

* `DEBUG` - option to define debug mode. `True` - enable debug output, `False` - disable debug output.

By default, we use `False` option value to disable debugging output.

---
Minimal set of variables in `.env` file to work with Postgresql server:

```
DB_HOST=xxxx
DB_PORT=xxxx
DB_NAME=xxxx
DB_USER=xxxx
DB_PASSWORD=xxxx
```

Before running site, fill these variables by your personal values.


# Run program 

To run site locally, execute command:

    $ python manage.py runserver localhost:8000

or:

    $ python manage.py runserver 127.0.0.1:8000


# Control results

If program running successfully, you will see the results like these:

![Alt text](img/1.png?raw=true "Active passcards")

![Alt text](img/2.png?raw=true "Employees inside storage")

![Alt text](img/3.png?raw=true "Visits per one employee")


# Final steps

Deactivate virtual environment:

```console
(venv) django-orm-watching-storage $ deactivate
```

Close console:
```console
$ exit
```
