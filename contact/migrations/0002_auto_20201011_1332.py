# Generated by Django 3.1.1 on 2020-10-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='company',
            field=models.CharField(default='nil.co', max_length=100),
        ),
        migrations.AddField(
            model_name='feeds',
            name='fullname',
            field=models.CharField(default='user', max_length=70),
        ),
    ]