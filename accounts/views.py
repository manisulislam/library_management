from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
import sweetify
from django.contrib.auth.views import LoginView,LogoutView
from books.models import BuyBookModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
            sweetify.success(request, 'You Registered Successfully. Please log in first.', icon='success')
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)
    
    def get_success_url(self) :
        sweetify.success(self.request, 'You Logged In Successfully', icon='success')
        
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):   
    
    def get_success_url(self) :
        sweetify.success(self.request, 'You Logged Out Successfully', icon='success')
        
        return reverse_lazy('home')

class UserProfileView(LoginRequiredMixin,View):
    template_name = 'accounts/profile.html'
    
    def get(self, request):
        reports=BuyBookModel.objects.filter(user=request.user)
        return render(request, self.template_name,{'reports':reports})
    
@login_required()
def ReturnBook(request,id):
    current_book=BuyBookModel.objects.get(id=id)
    current_book.user.account.balance+=current_book.book.book_price
    current_book.user.account.save(update_fields=['balance'])
    current_book.delete()
    sweetify.success(request, 'Book Returned Successfully', icon='success')
    return redirect('profile')

