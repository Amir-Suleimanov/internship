from django.db import models
from autoslug import AutoSlugField

# Create your models here.




class CoffeeHouse(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')    
    slug = AutoSlugField(populate_from='name', verbose_name='URL', unique=True)
    schedule = models.CharField(max_length=200, verbose_name='График работы')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Кофейня'
        verbose_name_plural = 'Кофейни'
        
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = AutoSlugField(populate_from='name', verbose_name='URL', unique=True)
    coffee_house = models.ForeignKey(
        'CoffeeHouse',
        on_delete=models.CASCADE,
        verbose_name='Кофейня'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    UNITS = (
        ('ml', 'мл'),
        ('l', 'л'),
        ('g', 'гр'),
        ('kg', 'кг'),
    )

    name = models.CharField(max_length=200, verbose_name='Название')    
    slug = AutoSlugField(populate_from='name', verbose_name='URL', unique=True)

    quantity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Объем/Количество')
    unit = models.CharField(max_length=2, choices=UNITS, verbose_name='Единица измерения')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Меню')
    photo = models.ImageField(upload_to='static/menu_items/', blank=True, null=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name


