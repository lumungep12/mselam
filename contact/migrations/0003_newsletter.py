# Generated by Django 3.1.1 on 2020-10-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201011_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=70)),
                ('mailPosted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]