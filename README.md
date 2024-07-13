








## Getting started
1. Устанавливаем poetry зависимости:\
   `pip install poetry
   poetry install
   poetry shell`
2. Создать файл "/.env" и описать в нем все значения из "/.env-sample"
3. Применяем миграции:\
   `python3 manage.py migrate`
4. Создание пользователей и групп: # логи и права описаны ниже\
   `python manage.py createsu
   python manage.py clear_permissions
   python manage.py loaddata json_data/auth.json
   python manage.py loaddata json_data/users.json`
4. Устанавливаем фикстуры:\
   `python manage.py fill`
5. Запуск приложения:\
   `python manage.py runserver`

logins:

    log: bla@mail.ru
    pw: 123
    perms: su

    log: tester@sky.pro
    pw: 123
    perms: default user w/o perms
    
    log: olapopaola@mail.ru
    pw: 0|=gR%]c
    perms: moder

    log: cm@con.man
    pw : 0|=gR%]c
    perms: content manager