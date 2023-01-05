from datetime import datetime
from django.shortcuts import render
from django.db.models import Count
from .models import Meal, MealClick


def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'cafe_core_app/menu.html', {'meal_categories': meal_categories})


def meal_category(request, meal_category):
    meal_choice = list(filter(lambda el: meal_category in el, Meal.MealType.choices))[0][0]
    meals_by_category = Meal.objects.filter(meal_type=meal_choice)
    return render(request, 'cafe_core_app/meals.html', {'meals': meals_by_category, 'meal_category': meal_choice})


def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    click = MealClick()
    click.meal_id = meal_id
    click.user_id = request.user.id
    click.click_date = datetime.utcnow().replace(minute=0,second=0,microsecond=0)
    click.save()
    return render(request, 'cafe_core_app/meal.html', {'meal': meal})
