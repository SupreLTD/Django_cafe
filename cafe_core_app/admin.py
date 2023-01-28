from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Meal, ImageMeal, MealType, MealClick


class ImageInLine(admin.TabularInline):  # StackedInline
    model = ImageMeal
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120">')

    get_image.short_description = 'Изображение'


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'meal_type')
    inlines = [ImageInLine]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60" height="50"')

    get_image.short_description = 'Изображение'


@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MealClick)
class MealClickAdmin(admin.ModelAdmin):
    list_display = ('meal','user')
