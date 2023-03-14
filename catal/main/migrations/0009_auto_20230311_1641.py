# Generated by Django 3.2.14 on 2023-03-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20230310_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockmaterialpagehome',
            options={'verbose_name': 'материал', 'verbose_name_plural': 'Главная - материалы'},
        ),
        migrations.RemoveField(
            model_name='blockguaranteespagehome',
            name='guarantees_h2',
        ),
        migrations.RemoveField(
            model_name='blockmaterialpagehome',
            name='material_h2',
        ),
        migrations.AddField(
            model_name='pagehome',
            name='guarantees_h2',
            field=models.CharField(blank=True, help_text='Максимум 300 символов', max_length=300, verbose_name='Заголовок блока - Гарантии'),
        ),
        migrations.AddField(
            model_name='pagehome',
            name='material_h2',
            field=models.CharField(blank=True, help_text='Максимум 300 символов', max_length=300, verbose_name='Заголовок блока - Принимаемые катализаторы'),
        ),
    ]
