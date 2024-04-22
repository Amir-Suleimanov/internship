from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
from pytils.translit import slugify
# def custom_slugify(value):
#     return slugify(value, allow_unicode=False)



class CoffeeHouse(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')    
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name='URL', slugify=slugify)
    schedule = models.CharField(max_length=200, verbose_name='График работы')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Кофейня'
        verbose_name_plural = 'Кофейни'
        
    def __str__(self):
        return self.name
    


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users",
        blank=True
    )