# Generated by Django 3.2.14 on 2023-03-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230309_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(help_text='Максимум 350 символов', max_length=250, verbose_name='Description'),
        ),
    ]
