
# Accounting system

### Требования
* Python 3.8.5


### Пример установки и запуска:

    D:\>py -m venv env
    
    D:\>cd env
    
    D:\env>Scripts\activate.bat
    
    (env) D:\env>git clone https://github.com/VovaGul/Accounting_system.git
    Cloning into 'Accounting_system'...
    remote: Enumerating objects: 39, done.
    remote: Counting objects: 100% (39/39), done.
    remote: Compressing objects: 100% (32/32), done.
    remote: Total 39 (delta 6), reused 35 (delta 4), pack-reused 0
    Receiving objects: 100% (39/39), 8.00 KiB | 629.00 KiB/s, done.
    Resolving deltas: 100% (6/6), done.
    
    (env) D:\env>cd Accounting_system
    
    (env) D:\env\Accounting_system>pip install -r requirements.txt
    Collecting asgiref==3.2.7 (from -r requirements.txt (line 1))
      Using cached https://files.pythonhosted.org/packages/68/00/25013f7310a56d17e1a
    b6fd885d5c1f216b7123b550d295c93f8e29d372a/asgiref-3.2.7-py2.py3-none-any.whl
    Collecting Django==3.0.4 (from -r requirements.txt (line 2))
      Using cached https://files.pythonhosted.org/packages/12/68/8c125da33aaf0942add
    5095a7a2a8e064b3812d598e9fb5aca9957872d71/Django-3.0.4-py3-none-any.whl
    Collecting django-crispy-forms==1.9.0 (from -r requirements.txt (line 3))
      Using cached https://files.pythonhosted.org/packages/c5/1e/166304128017b1dc45c
    6b79af753af93f6a0939c7ecca4258ca573aed8cd/django_crispy_forms-1.9.0-py2.py3-none
    -any.whl
    Collecting PyMySQL==0.9.3 (from -r requirements.txt (line 4))
      Using cached https://files.pythonhosted.org/packages/ed/39/15045ae46f2a123019a
    a968dfcba0396c161c20f855f11dea6796bcaae95/PyMySQL-0.9.3-py2.py3-none-any.whl
    Collecting pytz==2019.3 (from -r requirements.txt (line 5))
      Using cached https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf
    481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl
    Collecting sqlparse==0.3.1 (from -r requirements.txt (line 6))
      Using cached https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76
    be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl
    Installing collected packages: asgiref, sqlparse, pytz, Django, django-crispy-fo
    rms, PyMySQL
    Successfully installed Django-3.0.4 PyMySQL-0.9.3 asgiref-3.2.7 django-crispy-fo
    rms-1.9.0 pytz-2019.3 sqlparse-0.3.1
    
    (env) D:\env\Accounting_system>python manage.py makemigrations
    Migrations for 'accounts':
      accounts\migrations\0001_initial.py
        - Create model Profile
    
    (env) D:\env\Accounting_system>python manage.py migrate
    Operations to perform:
      Apply all migrations: accounts, admin, auth, contenttypes, sessions
    Running migrations:
      Applying accounts.0001_initial... OK
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying sessions.0001_initial... OK
    
    (env) D:\env\Accounting_system>py manage.py createsuperuser
    Username: admin
    Email address: admin@admin.ru
    Password:
    Password (again):
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    
    (env) D:\env\Accounting_system>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    April 03, 2020 - 21:49:58
    Django version 3.0.4, using settings 'demoproject.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    [03/Apr/2020 21:50:12] "GET /accounts/login/ HTTP/1.1" 200 1576
    [03/Apr/2020 21:50:15] "POST /accounts/login/ HTTP/1.1" 302 0
    [03/Apr/2020 21:50:15] "GET /accounts/profile/ HTTP/1.1" 200 1976
    [03/Apr/2020 21:50:17] "GET /accounts/logout/ HTTP/1.1" 200 677
    [03/Apr/2020 21:50:18] "GET / HTTP/1.1" 200 1576
