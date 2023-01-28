from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cafe_core_app/', include('cafe_core_app.urls')),
    path('analytics/', include('analytics.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('cafe_api.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
urlpatterns += doc_urls

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
