# How to start project on your laptop

To start this project on your laptop, you need to install the following programs:
 - Python
 - Git
 - virtualenv

Open cmd.exe and type the following command to check if you have a python installed: `python -V`

```
Microsoft Windows [Version 10.0.17763.805]
(c) 2018 Microsoft Corporation. Alle Rechte vorbehalten.

C:\Users\vmadmin> python -V
Python 3.7.5
```
If you don't see a result similar to `python 3.7.5`, it means you have to install a python on your laptop. Click on the following link and download the python and install it: https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe

Note: if you have a smaller `Python` version than `3.6`, you need to install a python larger than 3.6 and use this python.

---
Open cmd.exe and check if you have installed virtualenv: `virtualenv --version`
```
C:\Users\vmadmin>virtualenv --version
15.1.0
```
If you don't see the similar output as the above, you need to install virtualenv.
You can do that using python pip manager:
```
C:\Users\vmadmin>pip install virtualenv
```

---
Open cmd.exe and check if you have installed git: `git --version`
```
C:\Users\vmadmin>git --version
git version 2.23.0.windows.1
```
If you don't see the similar output as the above, you need to install git.
You can download it from here: https://git-scm.com/

---
Then open cmd.exe and create a folder in the `C:` directory:
```
C:\Users\vmadmin>mkdir c:\Dev
```
Then go to this directory:
```
C:\Users\vmadmin>cd c:\Dev
```
From here you can download the gibbface project using git:
```
c:\Dev>git clone https://github.com/khashashin/gibbface
Cloning into 'gibbface'...
remote: Enumerating objects: 176, done.
remote: Counting objects: 100% (176/176), done.
remote: Compressing objects: 100% (151/151), done.

Receiving objects: 100% (176/176), 3.94 MiB | 3.02 MiB/s, done.
Resolving deltas: 100% (13/13), done.
```
Then go to the `gibbface` folder:
```
c:\Dev>cd gibbface/
```
Now you can create a virtual python environment by typing the following command:
```
c:\Dev\gibbface>virtualenv env
```
Then you can activate this virtual environment by entering the following: `env\Scripts\activate`:
```
c:\Dev\gibbface>env\Scripts\activate
```
Now you can see that your virtual environment is activated with the prefix `(env) c:\Dev>`
And don't forget to create temporarily environment variable

---
Install all required libraries:
```
(env) c:\Dev\gibbface>pip install -r requirements.txt
(env) c:\Dev\gibbface>$Env:ENV = "dev"
```
Now that all libraries have been installed, we can start migrating the database by typing the following command:
```
(env) c:\Dev\gibbface>python manage.py migrate
```
Now you can start the website:
```
(env) c:\Dev\gibbface>python manage.py runserver
```