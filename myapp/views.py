from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    result = Products.objects.raw('SELECT *, price AS price FROM myapp_products ORDER BY RANDOM() LIMIT 1')[0]
    name = "%s" % (result.name)
    price = "%s" % (result.price)
    ratings = "%s" % (result.ratings)
    category = "%s" % (result.category)
    url = "%s" % (result.url)
    imageSrc = "%s" % (result.imageSrc)
    return render(request, "myapp/home.html", context={"result": result, "name": name, "price": price, "ratings": ratings, "category": category, "url": url, "imageSrc": imageSrc})
