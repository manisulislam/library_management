from django.db import models
from category.models import BookCategoryModel
from django.contrib.auth.models import User


class BookModel(models.Model):
    book_title = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    book_image = models.ImageField(upload_to='books/media/uploads/')
    book_description = models.TextField()

    def __str__(self):
        return self.book_title
    
class BuyBookModel(models.Model):
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['created_on']
    def __str__(self):
        return self.book.book_title

class Comment(models.Model):
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name