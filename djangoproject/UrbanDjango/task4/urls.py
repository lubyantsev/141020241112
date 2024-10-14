from django.contrib import admin
from django.urls import path
from . import views  # Импортируем из нового приложения task4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
]