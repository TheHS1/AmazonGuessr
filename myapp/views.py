from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
import math
from .models import *
from json import dumps
from json import loads
import random

# Create your views here.
def index(request):
    leaderboard = Games.objects.filter(finished=True).order_by('-totalScore')[:10]
    return render(request, "myapp/home.html", context={"leaderboard": leaderboard})

def processGame(request):
    if request.method =='POST':
        data = loads(request.body.decode('utf-8'))
        game = None
        user = None
        roundScore = 0

        if 'id' not in data:
            user = User()
            user.save()
        else:
            user = User.objects.get(id=data['id'])
            game = Games.objects.filter(player=user.id, finished=False).first()

        if game is None:
            prod = Products.objects.order_by('?').first()
            game = Games(player=user, product=prod)
            game.save()


        print(data)
        if 'guess' in data and len(data['guess']) > 0:

            rawScore = 1000*math.e**(-0.5 * (float(game.product.price[1:]) - float(data['guess']))**2/200)  * game.modifier 
            roundScore = 50 * round(float(rawScore/50))
            game.totalScore += roundScore
            oldProd = game.product
            game.product = Products.objects.order_by('?').first()
            game.hintsUsed = 0
            if(game.roundNumber == 5):
                game.finished=True
                newGame = Games(player=user, product=game.product)
                newGame.save()
                game.save()
                return JsonResponse({ 'id': newGame.player.id, 'round': newGame.roundNumber, 'score': game.totalScore, 'roundScore': roundScore, 'modifier': game.modifier, 'price': oldProd.price, 'img':newGame.product.imageSrc, 'finished': game.finished}, status=200)
            else:
                game.roundNumber += 1
            game.save()
            return JsonResponse({ 'id': game.player.id, 'round': game.roundNumber, 'score': game.totalScore, 'roundScore': roundScore, 'modifier': game.modifier, 'price': oldProd.price, 'img':game.product.imageSrc, 'finished': game.finished}, status=200)

        return JsonResponse({ 'id': game.player.id, 'round': game.roundNumber, 'score': game.totalScore, 'roundScore': roundScore, 'img':game.product.imageSrc, 'finished': game.finished}, status=200)

    else:
        return HttpResponseBadRequest()

def getHint(request):
    if request.method =='POST':
        data = loads(request.body.decode('utf-8'))
        game = Games.objects.get(player=data['id'],finished=0)
        if(game.hintsUsed < 3):
            game.hintsUsed += 1
            returnHint = None

            if (game.hintsUsed == 1):
                returnHint = game.product.ratings
                game.modifier = 0.95
            elif (game.hintsUsed == 2):
                returnHint = game.product.name
                game.modifier = 0.85
            elif (game.hintsUsed == 3):
                returnHint = "$" + str(round(random.uniform(0, float(game.product.price[1:])) * 0.75,2)) + " to $" + str(round(random.uniform(float(game.product.price[1:]), float(game.product.price[1:]) * 1.25), 2))
                game.modifier = 0.65

        game.save()

        return JsonResponse({ 'hintNum': game.hintsUsed, 'hint': returnHint}, status=200)
    else:
        return HttpResponseNotFound('<h1>Invalid Request Type</h1>')


def updateLeaderboard(request):
    if request.method =='POST':
        name = request.POST.get('name','guest')
        idVal = request.COOKIES.get('id')
        user = User.objects.get(id=idVal)
        user.username = name
        user.save()
        return redirect("/")
    else:
        return HttpResponseNotFound('<h1>Invalid Request Type</h1>')
