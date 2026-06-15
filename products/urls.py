from django.urls import path
from .views import ProductListView, ProductFormView, ProductListAPI

urlpatterns = [
    path('list/', ProductListView.as_view(), name="list_products"),
    path('api/', ProductListAPI.as_view(), name="list_product_api"),
    path('add/', ProductFormView.as_view(), name="add_product"),
]

