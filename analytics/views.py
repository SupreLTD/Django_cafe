from django.db.models import Count
from django.shortcuts import render

from cafe_core_app.models import Meal, MealClick


def top_meals(request):
    meals = Meal.objects.annotate(cnt=Count('mealclick')).order_by('-cnt')[:3]
    return render(request, 'analytics/top_meals.html', {'meals': meals})


def chart(request):
    meals = Meal.objects.all().order_by('meal_type')
    return render(request, 'analytics/charts.html', {'meals': meals})


def get_chart(request, meal_id):
    data = MealClick.objects.values('click_date', 'meal__name').annotate(cnt=Count('click_date')).filter(
        meal_id=meal_id).order_by('click_date')

    chart_data = [[(i['click_date'].replace(minute=0, second=0, microsecond=0).timestamp() + 10800) * 1000,
                   i['cnt']] for i in data]
    meal = data[0]['meal__name']

    user_clicks = MealClick.objects.values('meal', 'user__username').annotate(cnt=Count('user')) \
                      .filter(meal_id=meal_id).order_by('-cnt')[:5]

    return render(request, 'analytics/chart.html', {'data': chart_data, 'meal': meal, 'userclicks': user_clicks})
