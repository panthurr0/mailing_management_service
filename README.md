# Сервис управления рассылками

Чтобы удержать текущих клиентов, часто используют вспомогательные, или «прогревающие», рассылки для информирования и
привлечения клиентов. В проекте реализован сервис управления рассылками, администрирования и получения статистики, а
также раздел блога, для развития популярности сервиса в интернете.

## Стэк:

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" alt="python" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="django" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" alt="psql" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original-wordmark.svg" alt="bootstrap" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original-wordmark.svg" alt="html" width="40" height="40"/>
</div>

В проекте реализованы CRUD-механизмы для продуктов и блога, а также написан HTML для них.\
При регистрации, генерируется рандомный токен, а затем отправляется ссылка пользователю на почту, по которой он должен
перейти для верификации аккаунта
При сбросе пароля, генерируется новый рандомный пароль, применяется для конкретного пользователя в БД и затем
отправляется по почте\
[Механизм регистрации пользователя описан в RegisterView](users/views.py)\
[Механизм сброса пароля описан в ChangePWView](users/views.py)\
[Продукты кешируются с помощью cache_page](catalog/urls.py)\
[Получения данных по категориям из кеша](catalog/services.py)\
[Описание форм-классов](catalog/forms.py)

## Getting started:

1. Устанавливаем poetry зависимости:\
   `pip install poetry
   poetry install
   poetry shell`
2. Создать файл "/.env" и описать в нем все значения из "/.env-sample"
3. Применяем миграции:\
   `python3 manage.py migrate`
4. Создание пользователей и групп: # логи и права описаны ниже\
   `
   python manage.py createsu && \
   python manage.py clear_permissions && \
   python manage.py loaddata json_data/auth.json && \
   python manage.py loaddata json_data/users.json
   `
5. Устанавливаем фикстуры:\
   `python manage.py fill`
6. Запуск приложения:\
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