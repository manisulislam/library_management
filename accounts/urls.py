from django.urls import path
from .views import UserRegisterView,UserLoginView,UserLogoutView,UserProfileView,ReturnBook

urlpatterns=[
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('return_book/<int:id>/', ReturnBook, name='return_book'),
]