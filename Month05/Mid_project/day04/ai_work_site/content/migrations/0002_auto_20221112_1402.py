# Generated by Django 3.2.13 on 2022-11-12 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-recommend', '-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelTable(
            name='topic',
            table='topic',
        ),
    ]
