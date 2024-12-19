from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, ProfileViewSet
from product.views import ProductViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')  # User CRUD
router.register('profiles', ProfileViewSet, basename='profile')  # Profile CRUD
router.register('products', ProductViewSet, basename='product')  # Product CRUD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]