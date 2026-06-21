from django.urls import reverse_lazy
from .models import Product
from django.views import generic
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"


class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "data": self.request.POST,
                "files": self.request.FILES,
            }
        )
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreateAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
