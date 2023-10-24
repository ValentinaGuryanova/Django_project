# Generated by Django 4.2.6 on 2023-10-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_category_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение')),
                ('data_create', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_publish', models.BooleanField(verbose_name='Признак публикации')),
                ('count_view', models.IntegerField(verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]