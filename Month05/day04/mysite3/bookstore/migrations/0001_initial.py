# Generated by Django 3.2.13 on 2022-11-01 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='书名')),
                ('pub', models.CharField(max_length=50, verbose_name='出版社')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='价格')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='零售价')),
            ],
        ),
    ]
