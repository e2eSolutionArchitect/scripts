'' make sure you have django installed and VM profile created. For the steps please check 'install-django' in this repo.

django-admin startproject <project name>
django-admin startproject DjangoAPI

Run server
python manage.py runserver

Check the local link at port 8000
http://localhost:8000/
  
--Output------------------
(vmdev) C:\....\e2esa-git-repo\django-angular>django-admin startproject DjangoAPI

(vmdev) C:\....\e2esa-git-repo\django-angular>cd DjangoAPI

(vmdev) C:\....\e2esa-git-repo\django-angular\DjangoAPI>code . [Optional: just opening the code in code editor]

(vmdev) C:\....\e2esa-git-repo\django-angular\DjangoAPI>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 25, 2021 - 13:33:01
Django version 4.0, using settings 'DjangoAPI.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[25/Dec/2021 13:33:13] "GET / HTTP/1.1" 200 10697
[25/Dec/2021 13:33:13] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[25/Dec/2021 13:33:13] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[25/Dec/2021 13:33:13] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[25/Dec/2021 13:33:13] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[25/Dec/2021 13:33:13] "GET /favicon.ico HTTP/1.1" 404 2113
--------------------
