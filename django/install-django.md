`` create and browse a directory in command prompt and run below script to create a VM profile for django 
>> python -m venv <vm profile name>. press enter. it will create a new folder

python -m venv vmdev

`` now to activate the environment 
>> <env name>/Scripts/active

  vmdev/Scripts/active
  
'' Install Django and rest framework. before installing make sure you have crated the VM profile and activated it. 
  
pip install django
pip install djangorestframework
  
  -----Output------------
  C:\....\e2esa-git-repo>python -m venv vmdev

C:\....\e2esa-git-repo>cd django-angular

C:\....\e2esa-git-repo\django-angular>vmdev\Scripts\activate

(vmdev) C:\....\e2esa-git-repo\django-angular>pip install django
Collecting django
  Downloading Django-4.0-py3-none-any.whl (8.0 MB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting tzdata; sys_platform == "win32"
  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
Collecting backports.zoneinfo; python_version < "3.9"
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-win32.whl (36 kB)
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.4.1-py3-none-any.whl (25 kB)
Installing collected packages: sqlparse, tzdata, backports.zoneinfo, asgiref, django
Successfully installed asgiref-3.4.1 backports.zoneinfo-0.2.1 django-4.0 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 20.1.1; however, version 21.3.1 is available.
You should consider upgrading via the 'c:\users\..\appdata\local\programs\python\python38-32\python.exe -m pip install --upgrade pip' command.

(vmdev) C:\....\e2esa-git-repo\django-angular>pip install djangorestframework
Collecting djangorestframework
  Downloading djangorestframework-3.13.1-py3-none-any.whl (958 kB)
Requirement already satisfied: django>=2.2 in c:\users\..\appdata\local\programs\python\python38-32\lib\site-packages (from djangorestframework) (4.0)
Collecting pytz
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
Requirement already satisfied: backports.zoneinfo; python_version < "3.9" in c:\users\..\appdata\local\programs\python\python38-32\lib\site-packages (from django>=2.2->djangorestframework) (0.2.1)
Requirement already satisfied: tzdata; sys_platform == "win32" in c:\users\..\appdata\local\programs\python\python38-32\lib\site-packages (from django>=2.2->djangorestframework) (2021.5)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\..\appdata\local\programs\python\python38-32\lib\site-packages (from django>=2.2->djangorestframework) (0.4.2)
Requirement already satisfied: asgiref<4,>=3.4.1 in c:\users\..\appdata\local\programs\python\python38-32\lib\site-packages (from django>=2.2->djangorestframework) (3.4.1)
Installing collected packages: pytz, djangorestframework
Successfully installed djangorestframework-3.13.1 pytz-2021.3
WARNING: You are using pip version 20.1.1; however, version 21.3.1 is available.
You should consider upgrading via the 'c:\users\..\appdata\local\programs\python\python38-32\python.exe -m pip install --upgrade pip' command.

(vmdev) C:\....\e2esa-git-repo\django-angular>
  
  ----------------
