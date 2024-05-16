1. python3 manage.py migrate
2. python3 manage.py createsu to create superuser
3. python3 manage.py clear_permissions
4. python3 manage.py loaddata json_data/auth.json
5. python3 manage.py loaddata json_data/users.json to apply users(perms and logs below)
6. python3 manage.py fill to apply fixtures
7. change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in config/settings.py to use mail verification

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