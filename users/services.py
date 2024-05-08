from random import randint

from django.conf import settings
from django.core.mail import send_mail

from users.models import User


def verification_key():
    return randint(1000, 9998)


def send_email(user: User):
    key = verification_key()
    send_mail(
        'Ваш пароль для регистрации',
        f'Пароль: {key}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    return key
