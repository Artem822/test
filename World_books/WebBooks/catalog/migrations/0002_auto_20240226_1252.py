# Generated by Django 3.0.9 on 2024-02-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text="Choose book's author", to='catalog.Author', verbose_name="Book's author"),
        ),
    ]
