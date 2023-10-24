from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'sweets', 'description': 'Cake, capcake, sweets, bisquits', 'created_at': ''},
            {'name': 'milk', 'description': 'milk, cheese, eggs, yogurt', 'created_at': ''},
            {'name': 'fruits', 'description': '', 'created_at': ''},
            {'name': 'meat', 'description': 'meat, chicken, fish', 'created_at': ''},
        ]

        product_list = [
            {'name': 'apples', 'description': 'red apples', 'image': '/products/apples.jpeg', 'category': Сategory.objects, 'price': '80', 'data_create': '', 'data_last_change': ''},
            {'name': 'oranges', 'description': 'marroko', 'image': '/products/oranges.jpg', 'category': Сategory, 'price': '70', 'data_create': '', 'data_last_change': ''},
            {'name': 'cake', 'description': 'bisquit with fruit', 'image': '/products/cake.jpg', 'category': Сategory, 'price': '300', 'data_create': '', 'data_last_change': ''},
            {'name': 'candies', 'description': 'bird milk', 'image': '/products/candy.jpg', 'category': Сategory, 'price': '50', 'data_create': '', 'data_last_change': ''},
            {'name': 'milk', 'description': 'yellow milk 3.5', 'image': '/products/milk.jpeg', 'category': Сategory, 'price': '100', 'data_create': '', 'data_last_change': ''},
            {'name': 'yogurt', 'description': 'with strawberry', 'image': '/products/jjogurt.jpg', 'category': Сategory, 'price': '70', 'data_create': '', 'data_last_change': ''},
        ]

        # for product_item in product_list:
        #     Product.objects.create(**product_item)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Product.objects.bulk_create(product_for_create)
        Category.objects.bulk_create(category_for_create)