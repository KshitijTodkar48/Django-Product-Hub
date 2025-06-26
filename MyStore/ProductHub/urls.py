from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:product_id>/', views.product_details, name="product_details"),
    path('sellers/', views.product_sellers, name="product_sellers")
]