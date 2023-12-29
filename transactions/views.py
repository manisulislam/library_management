from django.shortcuts import render,redirect
from django.views import View
import sweetify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transaction
from .forms import TransactionForm
from .constants import DEPOSIT
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class DepositMoneyView(LoginRequiredMixin,View):
    form_class = TransactionForm
    template_name = 'transactions/deposit_form.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form=TransactionForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            user=request.user
            user.account.balance+=amount
            print(user.account.balance)
            user.account.save(
                update_fields=['balance',]
            )
            sweetify.success(request, 'Deposit Successful', icon='success')
            
            
            # deposit successful mail
            mail_subject='Deposit Successfully message'
            message=render_to_string('transactions/deposit_mail.html',{
                'user': self.request.user,
                'amount': amount
            })
            to_email=self.request.user.email
            send_email=EmailMultiAlternatives(mail_subject,'',to=[to_email])
            send_email.attach_alternative(message,'text/html')
            send_email.send()
            
            return redirect('home')





   