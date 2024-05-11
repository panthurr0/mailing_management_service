from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView, FormView

from users.services import send_email, verification_key, generate_password, send_password
from users.forms import UserRegisterForm, UserProfileForm, UserChangePWForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        host = self.request.get_host()
        token = verification_key()
        user.token = token
        user.save()
        send_email(user, host, token)
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ChangePWView(FormView):
    template_name = 'users/change_password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        email = form.cleaned_data['email']
        user = User.objects.get(email=email)

        passwrd = generate_password()
        hashed_passwrd = make_password(passwrd, salt=None, hasher="default")

        user.set_password(hashed_passwrd)
        user.save()
        send_password(user, hashed_passwrd)

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

# def change_password(request, pk):
#     user_item = get_object_or_404(User, pk=pk)
#
#     host = request.get_host()
#     passwrd = generate_password()
#     hashed_passwrd = make_password(passwrd, salt=None, hasher="default")
#     user_item.password = hashed_passwrd
#     user_item.save()
#     send_email(user_item, host, passwrd)
#
#     return redirect('users:login')
