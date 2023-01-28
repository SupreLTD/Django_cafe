from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from cafe_api.permissions import IsAdminOrReadOnly
from cafe_api.serializers import MealSerializer, MealTypeSerializer, TopMealsSerializer, TopUserClickSerializer, \
    ChartsSerializer
from cafe_core_app.models import Meal, MealType, MealClick


class MealListViewSet(viewsets.ModelViewSet):
    """Meals list views"""
    queryset = Meal.objects.all().select_related('meal_type').prefetch_related('images')
    serializer_class = MealSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # django-filter
    filterset_fields = ['size', 'price']
    search_fields = '__all__'
    ordering_fields = ['meal_type', 'price']

    @action(methods=['get'], detail=False)
    def mealtypes(self, request):
        types = MealType.objects.all()
        serializer = MealTypeSerializer(types, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def mealtype(self, request, pk=None):
        meals = Meal.objects.filter(meal_type=pk).select_related('meal_type').prefetch_related('images')
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)


class TopViewSet(viewsets.ReadOnlyModelViewSet):
    """Top Meals"""
    serializer_class = TopMealsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Meal.objects.annotate(count=Count('mealclick')).order_by('-count')[:3]

        return Meal.objects.annotate(count=Count('mealclick')).filter(pk=pk)


class TopUsersListView(generics.ListAPIView):
    """Top Users click on meals"""
    serializer_class = TopUserClickSerializer
    pagination_class = None
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return MealClick.objects.values('meal__name', 'user__username').annotate(cnt=Count('user')) \
                   .filter(meal_id=self.kwargs.get('pk')).order_by('-cnt')[:5]


class ChartsView(generics.ListAPIView):
    """Charts view"""
    serializer_class = ChartsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return MealClick.objects.values('click_date', 'meal__name').annotate(count=Count('click_date')).filter(
            meal_id=self.kwargs.get('pk')).order_by('click_date')
