from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import *
from json import dumps
from json import loads

# Create your views here.
def index(request):
    result = Products.objects.raw('SELECT * FROM myapp_products ORDER BY RANDOM() LIMIT 1')[0]
    id = dumps("%s" % (result.id))
    name = dumps("%s" % (result.name))
    price = dumps("%s" % (result.price[1:]))
    ratings = dumps("%s" % (result.ratings))
    category = dumps("%s" % (result.category))
    url = dumps("%s" % (result.url))
    imageSrc = "%s" % (result.imageSrc)

    return render(request, "myapp/home.html", context={"id": id, "result": result, "name": name, "price": price, "ratings": ratings, "category": category, "url": url, "imageSrc": imageSrc})



def getDBData(request):
    # Use request id to get relevant data from db
    id = loads(request.body.decode('utf-8'))['id']
    result = Products.objects.raw('SELECT * FROM myapp_products WHERE id=%s', [id])[0]
    name = dumps("%s" % (result.name))
    price = dumps("%s" % (result.price[1:]))
    ratings = dumps("%s" % (result.ratings))
    category = dumps("%s" % (result.category))
    url = dumps("%s" % (result.url))

    # send a json response 
    return JsonResponse({ 'name':name, 'price':price, 'ratings':ratings, 'category':category, 'url': url }, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
