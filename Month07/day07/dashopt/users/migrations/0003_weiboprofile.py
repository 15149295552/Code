# Generated by Django 3.2.13 on 2023-02-02 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiBoProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wuid', models.CharField(db_index=True, max_length=10, unique=True)),
                ('access_token', models.CharField(max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'db_table': 'users_weibo_profile',
            },
        ),
    ]
