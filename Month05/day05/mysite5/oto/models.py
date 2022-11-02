"""
作家表:妻子表  --->  1..1
"""
from django.db import models


class Author(models.Model):
    """作家模型类"""
    name = models.CharField("作家", max_length=50)

    class Meta:
        db_table = "oto_author"


class Wife(models.Model):
    name = models.CharField("妻子", max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "oto_wife"



