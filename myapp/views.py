from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import *
from json import dumps
from json import loads
import random

# Create your views here.
def index(request):
    result = Products.objects.raw('SELECT * FROM myapp_products ORDER BY RANDOM() LIMIT 1')[0]
    leaderboard = Games.objects.filter(finished=True).order_by('-totalScore')[:10]
    id = dumps("%s" % (result.id))
    name = dumps("%s" % (result.name))
    price = dumps("%s" % (result.price[1:]))
    ratings = dumps("%s" % (result.ratings))
    category = dumps("%s" % (result.category))
    url = dumps("%s" % (result.url))
    imageSrc = "%s" % (result.imageSrc)

    return render(request, "myapp/home.html", context={"id": id, "result": result, "name": name, "price": price, "ratings": ratings, "category": category, "url": url, "imageSrc": imageSrc, "leaderboard": leaderboard})

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

def processGame(request):
    data = loads(request.body.decode('utf-8'))
    id = -1 
    round = -1
    game = None
    user = None

    if 'id' not in data:
        user = User()
        user.save()
    else:
        user = User.objects.get(id=data['id'])
        game = Games.objects.filter(player=user.id, finished=False).first()

    if game is None:
        game = Games(player=user)

    if data['guess'] and 'prodID' in data:
        product = Products.objects.get(id=data['prodID'])
        game.roundNumber += 1
        game.totalScore += abs(float(product.price[1:]) - float(data['guess']) * game.modifier * 500.0)
        if(game.roundNumber == 5):
            game.finished=True

    game.hintsUsed = 0
    game.save()

    return JsonResponse({ 'id': game.player.id, 'round': game.roundNumber, 'score': game.totalScore}, status=200)

def getHint(request):
    data = loads(request.body.decode('utf-8'))
    game = Games.objects.get(player=data['id'],finished=0)
    if(game.hintsUsed < 3):
        product = Products.objects.get(id=data['prodID'])
        game.hintsUsed += 1
        returnHint = None

        if (game.hintsUsed == 1):
            returnHint = product.ratings
            game.modifier = 0.95
        elif (game.hintsUsed == 2):
            returnHint = product.name
            game.modifier = 0.85
        elif (game.hintsUsed == 3):
            returnHint = "$" + str(random.uniform(0, float(product.price[1:]) * 0.25)) + " to $" + str(random.uniform(float(product.price[1:]), float(product.price[1:]) * 1.25))
            game.modifier = 0.65

    game.save()

    return JsonResponse({ 'hintNum': game.hintsUsed, 'hint': returnHint}, status=200)
