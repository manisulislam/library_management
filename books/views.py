from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import BookModel,BuyBookModel
from django.shortcuts import get_object_or_404
import sweetify

# Create your views here.
class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    def get(self, request, *args, **kwargs):
        book=get_object_or_404(BookModel, pk=kwargs['pk'])
        context={
            'book':book
        }
        return render(request, self.template_name, context)


def BuyBook(request,id):
    book=get_object_or_404(BookModel, pk=id)
    book_price=book.book_price
    print(book_price)
    user_balance=request.user.account.balance
    print(user_balance)
    if user_balance>=book_price:
        request.user.account.balance-=book_price
        request.user.account.save(update_fields=['balance'])
        BuyBookModel.objects.create(user=request.user,book=book)
        sweetify.success(request, 'Book Purchased Successfully', icon='success')
        return redirect('home')
    