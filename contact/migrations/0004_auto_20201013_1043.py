# Generated by Django 3.1.1 on 2020-10-13 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_newsletter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newsletter',
            new_name='newsMail',
        ),
    ]
