from django.urls import path
from .views import ProductFormView
from .views import list_products

urlpatterns = [
    path('add/', ProductFormView.as_view(), name = "add_product"),
    path('list/', list_products, name="list_products")
]
