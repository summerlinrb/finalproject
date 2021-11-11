from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('store/', views.store, name='store'),
]