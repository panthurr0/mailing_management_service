import random
import string
from random import randint

from django.conf import settings
from django.core.mail import send_mail

from users.models import User


def verification_key() -> int:
    return randint(999, 9998)


def send_email(user: User, host, token: int | str):
    url = f'http://{host}/email-confirm/{token}/'
    send_mail(
        'Ссылка для регистрации',
        f'Ссылка: {url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )


def generate_password(length: int = 5) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def send_password(user_email, password):
    subject = 'Ваш пароль'
    message = f'Вот ваш новый пароль: {password}'
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, sender_email, recipient_list)
