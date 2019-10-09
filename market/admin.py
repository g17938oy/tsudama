from django.contrib import admin
from .models import Book
from .models import Lesson

admin.site.register(Book)
admin.site.register(Lesson)
