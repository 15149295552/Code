from django.contrib import admin
from bookstore.models import Book, Author


class BookManager(admin.ModelAdmin):
    list_display = ["id", "title", "price", "market_price"]
    list_display_links = ["title"]
    list_filter = ("title",)
    search_files = ["price"]
    list_editable = ["market_price"]


class AuthorManager(admin.ModelAdmin):
    list_display = ["id", "name", "age"]


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
