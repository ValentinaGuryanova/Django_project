# Generated by Django 4.2.6 on 2023-11-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_activ',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]