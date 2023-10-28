# Generated by Django 4.2.6 on 2023-10-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_name', models.CharField(max_length=150, verbose_name='название версии')),
                ('version_number', models.IntegerField(verbose_name='номер версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
