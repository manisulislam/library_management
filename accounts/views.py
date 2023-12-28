from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
import sweetify


class UserRegisterView(View):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'You Registered Successfully', icon='success')
            return redirect('home')
        return render(request, self.template_name, {'form': form})