
- Python 3.8.2
- Django (3, 0, 4, 'final', 0)

**Дополнительные библиотеки:**

* django-crispy-forms  
* Bootstrap 4

[**Туториал, по которому создавал виртуальную среду для запуска проекта:** ](https://django.fun/tutorials/autentifikaciya-v-django-polnyj-primer-vhoda-vyhoda-i-smeny-parolya/ "Заголовок ссылки")


**Отсутствует регистрация, так что для входа сначала нужно создать суперпользовователя:** 

    py manage.py createsuperuser


**Работающие ссылки:**
* [главная страница](http://127.0.0.1:8000/ "Заголовок ссылки")
* [для входа](http://127.0.0.1:8000/accounts/login/ "Заголовок ссылки")
* [для выхода](http://127.0.0.1:8000/accounts/logout/ "Заголовок ссылки")
* [профиль](http://127.0.0.1:8000/accounts/profile/)

**Пример запуска:**

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
**Вывод Консоли:**
    
    (env) D:\envv\Accounting_system>python manage.py makemigrations
    Migrations for 'accounts':
      accounts\migrations\0001_initial.py
       - Create model Profile

    (env) D:\envv\Accounting_system>python manage.py migrate
    Operations to perform:
    Apply all migrations: accounts, admin, auth, contenttypes, sessions
    Running migrations:
      Applying accounts.0001_initial... OK

    (env) D:\envv\Accounting_system>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    April 03, 2020 - 15:10:59
    Django version 3.0.4, using settings 'demoproject.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.