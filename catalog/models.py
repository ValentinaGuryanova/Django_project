from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание', **NULLABLE)

    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    data_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    data_last_change = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    is_activ = models.BooleanField(default=False, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price} {self.description[0:100]}'

    @property
    def active_version(self):
        return Version.objects.filter(is_active=True, product_id=self.id).first()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Version(models.Model):
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    version_number = models.IntegerField(verbose_name='номер версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.version_name} {self.version_number} {self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('is_active',)
