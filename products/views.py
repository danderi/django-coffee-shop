from django.urls import reverse_lazy
from .models import Product
from django.views import generic
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'

class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.request.POST,
            'files': self.request.FILES,
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
