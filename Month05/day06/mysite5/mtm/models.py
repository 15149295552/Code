from django.db import models


class Author(models.Model):
    name = models.CharField("作者", max_length=20)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField("书名", max_length=20)
    # 外键:无须指定级联动作
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

# # 1.一夜暴富这本书的作者都有谁？
# b1 = Book.objects.get(name="一夜暴富")
# b1.author.all()
#
# # 2.吕泽都写过那些书？
# a1 = Author.objects.get(name="吕泽")
# Book.objects.filter(author=a1)
