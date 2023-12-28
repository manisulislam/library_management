from django.contrib import admin
from category.models import BookCategoryModel
# Register your models here.


class BookCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=('name','slug')

admin.site.register(BookCategoryModel,BookCategoryAdmin)