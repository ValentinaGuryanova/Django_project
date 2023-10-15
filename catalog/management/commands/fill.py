from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'яблоко', 'description': 'свежее зеленое яблоко', 'image': '', 'category': 'фрукт', 'price': '80', 'data_create': '', 'data_last_change': ''},
            {'name': 'апельсин', 'description': 'сочный мароко', 'image': '', 'category': 'фрукт', 'price': '70', 'data_create': '', 'data_last_change': ''},
            {'name': 'торт', 'description': 'бисквитный с фруктовой начинкой', 'image': '', 'category': 'сладости', 'price': '300', 'data_create': '', 'data_last_change': ''},
            {'name': 'конфеты', 'description': 'птичье молоко', 'image': '', 'category': 'сладости', 'price': '50', 'data_create': '', 'data_last_change': ''},
            {'name': 'молоко', 'description': 'топленое молоко 3.5', 'image': '', 'category': 'молочные продукты', 'price': '100', 'data_create': '', 'data_last_change': ''},
            {'name': 'йогурт', 'description': 'с клубничным вкусом', 'image': '', 'category': 'молочные продукты', 'price': '70', 'data_create': '', 'data_last_change': ''},
        ]

        category_list = [
            {'name': 'сладости', 'description': 'Торты, пирожные, конфеты, печенье.', 'created_at': ''},
            {'name': 'молочные продукты', 'description': 'Молоко, йогурт, кефир, сыр', 'created_at': ''},
            {'name': 'фрукты', 'description': '', 'created_at': ''},
            {'name': 'мясные продукты', 'description': 'Мясо, колбаса, нарезки', 'created_at': ''},
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