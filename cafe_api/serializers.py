from django.db.models import Count
from rest_framework import serializers
from cafe_core_app.models import Meal, MealType, ImageMeal, MealClick


class ImageMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageMeal
        fields = ('id', 'image')


class MealSerializer(serializers.ModelSerializer):
    images = ImageMealSerializer(read_only=True, many=True)
    meal_type = serializers.CharField(read_only=True)

    class Meta:
        model = Meal
        fields = ("id", 'name', 'description', 'price', 'size', 'meal_type', 'images')


class TopMealsSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Meal
        fields = ('name', 'count')


class MealTypeSerializer(serializers.ModelSerializer):
    meals = MealSerializer(read_only=True)

    class Meta:
        model = MealType
        fields = ('id', 'name', 'image', 'url', 'meals')


class TopUserClickSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='cnt', read_only=True)
    user = serializers.CharField(source='user__username', read_only=True)
    meal = serializers.CharField(source='meal__name', read_only=True)

    class Meta:
        model = MealClick
        fields = ('user', 'count', 'meal')


class ChartsSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = MealClick
        fields = ('click_date', 'count')
