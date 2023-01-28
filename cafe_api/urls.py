from django.urls import path, include
from rest_framework import routers

from .views import MealListViewSet, TopViewSet, TopUsersListView, ChartsView

router_meals = routers.SimpleRouter()
router_meals.register(r'meals', MealListViewSet, )

router_top = routers.SimpleRouter()
router_top.register(r'top', TopViewSet, basename='top')

urlpatterns = [
    path("", include(router_meals.urls), name="meals"),
    path("", include(router_top.urls), name="top"),
    path("top_users/<int:pk>", TopUsersListView.as_view(), name="top_users"),
    path("charts/<int:pk>", ChartsView.as_view(), name="charts"),
]
