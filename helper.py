# 1.
# python3 -m venv venv - создание виртуального окружения

# source venv/bin/activate - активировать виртуальное окружение
# pip freeze - список установленных библиотек
# deactivate - выйти из виртуального окружения

###########################################################


# 2. 
# requirements.txt:
    # django
    # djangorestframework


# 3. 
# pip install -r requirements.txt

# 4.
# django-admin startproject name_project . - создаем главное приложение нашего проекта

# 5.
# django-admin startapp name_app - создаем определенное приложение

# 6.
# ./manage.py runserver

# 7.
# ./manage.py createsuperuser - создает суперюзера
# ./manage.py makemigrations создает миграцию
# ./manage.py migrate - применяет ее