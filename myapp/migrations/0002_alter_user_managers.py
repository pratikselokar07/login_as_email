# Generated by Django 4.1.7 on 2023-03-03 10:25

from django.db import migrations
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', myapp.models.UserManager()),
            ],
        ),
    ]