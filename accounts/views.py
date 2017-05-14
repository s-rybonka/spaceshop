from django.views.generic.edit import FormView, View

from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.http import is_safe_url

from .forms import RegisterForm
from .forms import LoginForm
from spaceshop import settings


class RegisterView(View):
    template = "registration/register.html"
    form = RegisterForm

    def get(self, request, **kwargs):
        response = TemplateResponse(request, self.template, {'form': self.form(request=request)})

        return response

    def post(self, request, **kwargs):
        form = self.form(data=request.POST, request=request)
        if form.is_valid():

            form.save()

            if not form.errors:
                return redirect(reverse('login'))

        return render(request, self.template, {'form': form})

# To do: Need add decoratosrs here
class LoginView(FormView):
    form_class = LoginForm

    success_url = reverse_lazy('home')

    template_name = "registration/login.html"

    def post(self, request, redirect_field_name=REDIRECT_FIELD_NAME, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user:

            login(request, user)

            redirect_to = self.request.POST.get('next', '')

            if not is_safe_url(url=redirect_to, host=self.request.get_host()):
                redirect_to = str(settings.LOGIN_REDIRECT_URL)

            response = HttpResponseRedirect(redirect_to=redirect_to)

            return response
        else:
            return redirect(reverse('login'))
