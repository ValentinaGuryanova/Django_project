import random
from random import randint

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        verified_password = ''
        for i in range(8):
            i = randint(0, 9)
            verified_password += str(i)

            form.verified_password = verified_password
            user = form.save()
            user.verified_password = verified_password
        # new_user = form.save()
            send_mail(
                subject='Поздравляем с регистрацией!',
                message=f'Подтвердите вашу регистрацию в SuperMarket, нажмите на ссылку: http://127.0.0.1:8000/users/verifying?code={user.verified_password}\n ',
            # message='Вы зарегистрировались на нашей платформе, добро пожаловать!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return super().form_valid(form)


def verify_view(request):
    code = int(request.GET.get('code'))
    user = User.objects.get(verified_password=code)
    user.verified = True
    user.save()
    return render(request, 'users/verifying.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0,9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:product'))