from catalog.models import Category
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("SELECT setval(pg_get_serial_sequence('catalog_category', 'id'), 1, false);")

        Category.objects.all().delete()

        category_list = [
            {'name': 'fruits', 'created_at': ''},
            {'name': 'Sweets', 'created_at': ''},
            {'name': 'Meat', 'created_at': ''},
            {'name': 'Drinks', 'created_at': ''},
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)