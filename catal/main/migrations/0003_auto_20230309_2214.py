# Generated by Django 3.2.14 on 2023-03-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230309_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': 'статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(help_text='Максимум 350 символов', max_length=350, verbose_name='Description'),
        ),
    ]
