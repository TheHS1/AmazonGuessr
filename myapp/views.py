from django.shortcuts import render
from .models import *
from json import dumps

# Create your views here.
def index(request):
    result = Products.objects.raw('SELECT *, price AS price FROM myapp_products ORDER BY RANDOM() LIMIT 1')[0]
    name = dumps("%s" % (result.name))
    price = dumps("%s" % (result.price[1:]))
    ratings = dumps("%s" % (result.ratings))
    category = dumps("%s" % (result.category))
    url = dumps("%s" % (result.url))
    imageSrc = "%s" % (result.imageSrc)

    return render(request, "myapp/home.html", context={"result": result, "name": name, "price": price, "ratings": ratings, "category": category, "url": url, "imageSrc": imageSrc})
