# How to start project on your laptop

To start this projekt on your laptop you need following programms istallieren:
 - Python
 - Git
 - virtualenv

Open cmd.exe and type following command to check if you have python installed: `python -V`

```
Microsoft Windows [Version 10.0.17763.805]
(c) 2018 Microsoft Corporation. Alle Rechte vorbehalten.

C:\Users\vmadmin> python -V
Python 3.7.5
```
If you dont see the output similar to `Python 3.7.5` that means you have to install python on your Laptop. Go to the following link and download the python and install it: https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe

Note: if you get `Python` version smaller than `3.6` you have to install python greater then 3.6 and use this python.

---
Open cmd.exe and check if you have git installed: `git --version`
```
C:\Users\vmadmin>git --version
git version 2.23.0.windows.1
```
If you dont see the output similar to the text above you need to install git.
You can download it from here: https://git-scm.com/

---
Next, open cmd and create folder under `C:` directory:
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
Then go to the directory `gibbface`:
```
c:\Dev>cd gibbface/
```
Now you can create python virtualenvironment, type following:
```
c:\Dev\gibbface>virtualenv env
```
Then you can activate this virtualenvironment, type this: `env\Scripts\activate`:
```
c:\Dev\gibbface>env\Scripts\activate
```
Now you can see that your virtuaenv is activated with prefix of `(env) c:\Dev>`

---
Install all requirement libraries:
```
(env) c:\Dev\gibbface>pip install -r requirements.txt
```
Now since all libraries installed we can start database migration, type following:
```
(env) c:\Dev\gibbface>python manage.py migrate
```
Now you can start the website:
```
(env) c:\Dev\gibbface>python manage.py runserver
```