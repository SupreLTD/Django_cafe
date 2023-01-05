from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cafe_core_app/', include('cafe_core_app.urls')),
    path('analytics/', include('analytics.urls'))
]