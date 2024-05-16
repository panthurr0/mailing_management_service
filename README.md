1. run python3 manage.py createsu to create superuser
2. run python3 manage.py clear_permissions
3. run python3 manage.py loaddata json_data/auth.json
4. run python3 manage.py loaddata json_data/users.json to apply users(perms and logs below)
5. run python3 manage.py fill to apply fixtures
6. change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in config/settings.py to use mail verification


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