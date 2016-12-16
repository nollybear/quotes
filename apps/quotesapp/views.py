from django.shortcuts import render, redirect
from .models import User, Quote, Favorite
from django.contrib import messages
from itertools import count




def index(request):
    return render(request, "quotesapp/index.html")

def register(request):
    result = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm'], request.POST['birthday'])
    if result == True:
        email = request.POST['email']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        return redirect('/quotes')
    else:
        request.session['errors'] = result[1]
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST['email'], request.POST['password'])
    if result == True:
        email = request.POST['email']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        return redirect('/quotes')
    else:
        request.session['errors'] = result[1]
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id=request.session['user_id'])[0]
    favorites = Favorite.objects.filter(user = user)
    quotes = Quote.objects.filter().exclude(id__in=favorites)
    context = {
        "user":user,
        "quotes":quotes,
        "favorites":favorites
    }
    return render(request, "quotesapp/quotes.html", context)

def addquote(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id = request.session['user_id'])[0]
    result = Quote.objects.addquote(user = user, quote = request.POST['quote'], author = request.POST['author'])
    if result == True:
        return redirect('/quotes')
    else:
        request.session['quote_errors'] = result[1]
        return redirect('/quotes')


def addfavorite(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    quote = Quote.objects.filter(id = id)[0]
    user = User.objects.filter(id = request.session['user_id'])[0]
    result = Favorite.objects.addfavorite(user = user, quote = quote)
    if result == True:
        return redirect('/quotes')


def user(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id = id)[0]
    quotes = Quote.objects.filter(user = user)
    counter = 0
    for quote in quotes:
        counter = counter + 1
    context = {
        "user":user,
        "quotes":quotes,
        "counter":counter
    }
    return render(request, "quotesapp/user.html", context)




def undefined(request):
    return render(request, "quotesapp/404.html")
