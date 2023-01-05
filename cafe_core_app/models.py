from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.db import models


class Meal(models.Model):

    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Стоимость блюда')
    size = models.IntegerField('Размер блюда')

    class MealType(models.TextChoices):
        HOT_MEALS = 'Горячие блюда', _('hot_meals')
        DESSERTS = 'Десерты', _('deserts')
        DRINKS = 'Напитки', _('drinks')
        NO_TYPE = 'NO_TYPE', _('no_type')

    meal_type = models.CharField(
        max_length=30,
        choices=MealType.choices,
        default=MealType.NO_TYPE
    )

    def __str__(self):
        return self.name


class MealClick(models.Model):

    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING,verbose_name='meal')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='user')
    click_date = models.DateTimeField('Дата клика')



