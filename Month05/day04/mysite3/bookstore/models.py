from django.db import models


class Book(models.Model):
    """
    1. title - CharField 书名,非空,唯一
    2. pub - CharField 出版社,字符串,非空
    3. price - DecimalField 图书定价 总长6位/小数点2位
    4. market_price - 图书零售价 总长6位/小数点2位
    """
    title = models.CharField("书名", max_length=20, null=False, unique=True)
    pub = models.CharField("出版社", max_length=50, null=False)
    price = models.DecimalField("价格", max_digits=6, decimal_places=2)
    market_price = models.DecimalField("零售价", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"<{self.title}:{self.pub}:{self.price}>"


class Author(models.Model):
    name = models.CharField("姓名", max_length=20, null=False)
    age = models.IntegerField("年龄", null=False, default=1)
    email = models.EmailField("邮箱", null=True)

    def __str__(self):
        return f"{self.name}:{self.age}:{self.email}"