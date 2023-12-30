from django.urls import path
from .views import BookDetailView,BorrowBook

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('borrow_book/<int:id>/',BorrowBook,name='borrow_book'),
    
]