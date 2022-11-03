from django.contrib import admin
from otm.models import Pub, Book


class PubManager(admin.ModelAdmin):
    list_display = ["id", "name"]


class BookManager(admin.ModelAdmin):
    list_display = ["id", "name", "pub_id"]


admin.site.register(Pub, PubManager)
admin.site.register(Book, BookManager)