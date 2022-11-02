from django.contrib import admin
from mtm.models import Author, Book


class AuthorManager(admin.ModelAdmin):
    list_display = ["id", "name"]


class BookManager(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)



