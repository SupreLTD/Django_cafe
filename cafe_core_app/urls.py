from django.urls import path
from . import views

app_name = 'cafe_core_app'

urlpatterns = [

    path('', views.main, name='menu'),
    path('menu', views.menu, name='menu'),
    path('menu/<str:meal_category>', views.meal_category, name='meal_category'),
    path('menu/<int:meal_id>/meal', views.meal, name='meal'),
    path('about', views.about, name='about'),
]
