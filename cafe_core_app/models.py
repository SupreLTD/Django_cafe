from django.contrib.auth.models import User

from django.db import models


class MealType(models.Model):
    name = models.CharField('Категория', max_length=30)
    image = models.ImageField('Изображение', upload_to='meal_types/')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Meal(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Стоимость блюда')
    size = models.IntegerField('Размер блюда')
    meal_type = models.ForeignKey(MealType, on_delete=models.DO_NOTHING, verbose_name='Категория',
                                  related_name='meal_type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING, related_name='mealclick')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    click_date = models.DateTimeField('Дата клика')


class ImageMeal(models.Model):
    image = models.ImageField('Изображение', upload_to='meal_images/')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
