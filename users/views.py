import random

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.management.commands.services import generate_verified_code
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            verified_password = ''
            for i in range(8):
                verified_password += random.choice('0123456789')

            form.verified_password = verified_password
            user = form.save()
            user.verified_password = verified_password
            send_mail(
                subject='Поздравляем с регистрацией!',
                message=f'Подтвердите вашу регистрацию в SuperMarket, нажмите на ссылку: http://127.0.0.1:8000/users/verifying?code={user.verified_password}\n ',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return super().form_valid(form)


def verify_view(request):
    code = int(request.GET.get('code'))
    user = User.objects.get(verified_password=code)
    user.verified = True
    user.save()
    if user.verified != code:
        print('Код неверный')
    return render(request, 'users/verifying.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


