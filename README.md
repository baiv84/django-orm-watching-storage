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

This command install `django` framework and `psycopg2` library into the `venv` virtual environment.

# Run program 

    (venv) django-orm-watching-storage $ python main.py

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
