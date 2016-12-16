from django.shortcuts import render

def index(request):
    return render(request, "quotesapp/index.html")

# def register(request):
#     result =  User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm'])
#     if result == True:
#         email = request.POST['email']
#         user = User.objects.filter(email=email)[0]
#         request.session['user_id'] = user.id
#         return redirect('/books')
#     else:
#         request.session['errors'] = result[1]
#         return redirect('/')
#
# def login(request):
#     # result = User.objects.login(request.POST['email'], request.POST['password'])
#     # if result == True:
#     #     email = request.POST['email']
#     #     user = User.objects.filter(email=email)[0]
#     #     request.session['user_id'] = user.id
#     #     return redirect('/books')
#     # else:
#     #     request.session['errors'] = result[1]
#     #     return redirect('/')
