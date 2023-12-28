from django.shortcuts import render, redirect
from django.views import View
from category.models import BookCategoryModel
from books.models import BookModel

def Home(request, category_slug=None):
    data=BookModel.objects.all()
    if category_slug is not None:
        category=BookCategoryModel.objects.get(slug=category_slug)
        data=BookModel.objects.filter(book_category=category)
    categories=BookCategoryModel.objects.all()
    return render(request, 'home.html', {'data':data, 'category':categories})