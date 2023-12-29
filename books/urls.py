from django.urls import path
from .views import BookDetailView,BuyBook

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('buy_book/<int:id>',BuyBook,name='buy_book'),
]