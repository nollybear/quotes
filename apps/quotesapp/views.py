from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
from itertools import count




def index(request):
    return render(request, "quotesapp/index.html")

def register(request):
    result =  User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm'])
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
    quotes = Quote.objects.filter().order_by('-id')[:3]
    context = {
        "user":user,
    }
    return render(request, "quotesapp/quotes.html", context)

def addquote(request):
    if 'user_id' not in request.session:
        return redirect('/')
    result = Quote.objects.addquote(request.POST['title'], request.POST['author'])
    if result[0] == True:
        title = request.POST['title']
        id = quote.id
        user = User.objects.filter(id = request.session['user_id'])[0]
        quote = Review.objects.create(user = user, book = book, review = request.POST['review'], rating = request.POST['rating'])
        return redirect('/book/{}'.format(book.id))
    else:
        request.session['errors'] = result[1]
        return redirect('/quotes')

def undefined(request):
    return render(request, "quotesapp/404.html")
