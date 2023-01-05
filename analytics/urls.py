from django.urls import path
from . import views

app_name = 'analytics'
urlpatterns = [
    path('top_meals/', views.top_meals, name='top_meals'),
    path('charts/', views.chart, name='charts'),
    path('<int:meal_id>/chart', views.get_chart, name='chart'),
]
