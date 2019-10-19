# Dyna-Socket
*** A Full Fledged Python Chat Engine ****

## Requirements:

  Python 2.7

## Python package requirements:

1. os
2. sys
3. socket
4. threading
5. glob


### Steps to run the bot

* Run the client side code
```console
code@user:~$ python testclient.py
```
* Run the server side code
```console
code@user:~$ python testserver.py
```

### What to do if your system has python3 as default?
Create a virtual environment with Python 2.7. Steps mentioned below

#### Create virtualenv:
* Install virtualenv:
```console
code@user:~$ pip install virtualenv
```
* Create a virtual environment:
```console
code@user:~$ virtualenv dyna-sock --python=/usr/bin/python2.7
```
* Activate virtual environment:
```console
code@user:~$ source dyna-sock/bin/activate
```

#### Create conda environment (This can be done only if anaconda is installed):
Note:- In case anaconda is not installed, you can find the steps to do so here -> [Install anaconda](https://docs.anaconda.com/anaconda/user-guide/faq/#anaconda-faq-35)

* Create conda environment:
```console
code@user:~$ conda create -n dyna-sock python=2.7
```
* Start conda environment:
```console
code@user:~$ source activate dyna-sock
```
