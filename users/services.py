from random import randint

from django.conf import settings
from django.core.mail import send_mail

from users.models import User


def verification_key():
    return randint(999, 9998)


def send_email(user: User, host, token):
    url = f'http://{host}/email-confirm/{token}/'
    send_mail(
        'Ссылка для регистрации',
        f'Ссылка: {url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )
