from django.contrib import admin
from book_app import models
# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)