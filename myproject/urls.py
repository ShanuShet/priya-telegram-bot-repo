from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicViewSet, ProtectedViewSet

router = DefaultRouter()
router.register(r'public', PublicViewSet, basename='public')
router.register(r'protected', ProtectedViewSet, basename='protected')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 