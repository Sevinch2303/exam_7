from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import *


def index(request):
    all_nft = NFT.objects.all().order_by('-id')

    context = {
        "all_nft": all_nft
    }
    return render(request, 'index.html', context)


def explore(request):
    return render(request, 'explore.html')


def author(request):
    return render(request, 'author.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        username = request.POST.get('username')
        price = request.POST.get('price')
        royalties = request.POST.get('royalties')
        file = request.FILES.get('file')
        category = request.POST.get('category')

        nft = NFT(title=title, description=description, username=username, price=price, royalties=royalties, file=file,
                  category=category)
        nft.save()
        return redirect('index')
    return render(request, 'create.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password1)
                user.save()
                messages.success(request, 'You have successfully registered.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'registration/registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')
