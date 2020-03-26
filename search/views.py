from django.shortcuts import render
from products.models import Product
from django.contrib.postgres.search import SearchVector
# Create your views here.
def do_search(request):
    """seraching for products by word
    """
    products =Product.objects.annotate(search=SearchVector('title', 'description'),).filter(search__icontains=request.GET['do_search'])
    return render(request, "products/product_list.html", {"products":products})



