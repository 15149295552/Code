# Generated by Django 3.2.13 on 2022-11-02 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='出版社')),
            ],
            options={
                'db_table': 'otm_pub',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='书名')),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otm.pub')),
            ],
            options={
                'db_table': 'otm_book',
            },
        ),
    ]
