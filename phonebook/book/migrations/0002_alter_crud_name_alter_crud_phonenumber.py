# Generated by Django 5.1.6 on 2025-02-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='crud',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
    ]
