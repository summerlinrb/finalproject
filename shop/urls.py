from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shop'

urlpatterns = [
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)