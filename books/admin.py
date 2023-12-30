from django.contrib import admin
from .models import BookModel,BuyBookModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(BuyBookModel)
