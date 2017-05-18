from django.views.generic.edit import View

from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Own modules
from .forms import RegisterForm


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
