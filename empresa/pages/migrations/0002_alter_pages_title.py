# Generated by Django 5.1.3 on 2024-11-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.TextField(max_length=100, unique=True, verbose_name='Titulo'),
        ),
    ]