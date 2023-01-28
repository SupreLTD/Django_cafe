from datetime import datetime
from django.shortcuts import render
from django.db.models import Count
from .models import Meal, MealClick, MealType


def main(request):
    return render(request, 'cafe_core_app/main.html')


def menu(request):
    meal_categories = MealType.objects.all()
    return render(request, 'cafe_core_app/menu.html', {'meal_categories': meal_categories})


def about(request):
    return render(request, 'cafe_core_app/about.html')


def meal_category(request, meal_category):
    meals = Meal.objects.filter(meal_type__url=meal_category).order_by('id')
    title = MealType.objects.values('name').get(url=meal_category)
    return render(request, 'cafe_core_app/meals.html', {'meals': meals, 'title': title})


def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    click = MealClick()
    click.meal_id = meal_id
    click.user_id = request.user.id
    click.click_date = datetime.utcnow().replace(minute=30, second=0, microsecond=0)
    click.save()
    return render(request, 'cafe_core_app/meal.html', {'meal': meal})
