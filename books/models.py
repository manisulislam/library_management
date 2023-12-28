from django.db import models
from category.models import BookCategoryModel
# Create your models here.

class BookModel(models.Model):
    book_title = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    book_image = models.ImageField(upload_to='books/media/uploads/')
    book_description = models.TextField()

    def __str__(self):
        return self.book_title