from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import BookModel,BuyBookModel
from django.shortcuts import get_object_or_404
import sweetify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views import View


# Create your views here.

class BookDetailView(LoginRequiredMixin,DetailView):
    template_name = 'books/book_detail.html'
    model=BookModel
    def get(self, request, *args, **kwargs):
        book=get_object_or_404(BookModel, pk=kwargs['pk'])
        context={
            'book':book,
            
        }
        return render(request, self.template_name, context)
    
    
   
@login_required
def BorrowBook(request, id):
    book = get_object_or_404(BookModel, pk=id)
    book_price = book.book_price

    user_balance = request.user.account.balance

    if user_balance >= book_price:
        request.user.account.balance -= book_price
        request.user.account.save(update_fields=['balance'])
        BuyBookModel.objects.create(user=request.user, book=book)
        sweetify.success(request, 'Book Borrowed Successfully.Check your email.', icon='success')
        
        mail_subject = 'Borrow Book Successfully message'
        message = render_to_string('books/borrow_book_mail.html', {
                    'user': request.user,
                    'price': book_price,
                    'book': book
                })
        to_email = request.user.email
        send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()
        return redirect('profile')

    
