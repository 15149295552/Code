from django.db import models


class Pub(models.Model):
    name = models.CharField("出版社", max_length=50, unique=True, null=False)

    class Meta:
        db_table = "otm_pub"

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE)
    name = models.CharField("书名", max_length=50)

    class Meta:
        db_table = "otm_book"

    def __str__(self):
        return f"{self.name}"

# 正向: 西游记这本书的出版社是哪个？
# b1 = Book.objects.get(name="西游记")
# b1.pub.name

# 1.北京大学出版社出版过哪些图书
# p1 = Pub.objects.get(name="北京大学出版社")
# books = Book.objects.filter(pub=p1)

# 2.Python这本书是由哪个出版社出版的？
# b1 = Book.objects.get(name="Python")
# b1.pub.name







