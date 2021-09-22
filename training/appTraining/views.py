from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from . models import Features

# Create your views here.
def index(request):
    # context = {
    #     'name' : 'Pranay',
    #     'bio' : 'is a hardcore programmer'
    # }
    
    # feature = Features()
    # feature.id = 0
    # feature.name = 'Pranay'
    # feature.bio = 'I like to build complicated projects (cause I don\'t like easy things), being inside the core of the software, coding, and bringing up a brand new side to the world.... '

    # feature1 = Features()
    # feature1.id = 1
    # feature1.name = 'Kumar'
    # feature1.bio = 'I like to build complicated projects (cause I don\'t like easy things), being inside the core of the software, coding, and bringing up a brand new side to the world.... '


    # feature2 = Features()
    # feature2.id = 2
    # feature2.name = 'Singh'
    # feature2.bio = 'I like to build complicated projects (cause I don\'t like easy things), being inside the core of the software, coding, and bringing up a brand new side to the world.... '


    # feature3 = Features()
    # feature3.id = 3
    # feature3.name = 'Anonymos'
    # feature3.bio = 'I like to build complicated projects (cause I don\'t like easy things), being inside the core of the software, coding, and bringing up a brand new side to the world.... '

    # features = [feature, feature1, feature2, feature3]

    features = Features.objects.all()

    return render(request, 'index.html', { "features": features })


def counter(request):
    # text = request.POST['text']
    # amount_of_words = len(text.split())
    return render(request, 'counter.html', { 'amount' : 22 })

def register(request):
    
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:

            if (User.objects.filter(email=email).exists()):
                messages.info(request, 'Email already in use!')
                return redirect('register')
            elif (User.objects.filter(username=name).exists()):
                messages.info(request, 'Name already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                return redirect('/')
        
        else:
            messages.info(request, 'Passwords are not same!')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Please provide valid credential!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request, p):
    return render(request, 'profile.html', {'p': p})

    