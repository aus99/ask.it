# Generated by Django 4.1.7 on 2023-03-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]