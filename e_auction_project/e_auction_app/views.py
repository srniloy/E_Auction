from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializer import UserEmailsSerializer
from rest_framework.response import Response

from .models import *


# Create your views here.


def redirect_view(request):
    response = redirect('signup')
    return response


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        current_email = request.POST.get('user_email')
        stored_emails = UserEmail.objects.all()
        for store_email in stored_emails:
            if store_email.user_email == current_email:
                return render(request, 'home.html', {"user_email": current_email})
        login_error = {
            "problem_text": "Entered wrong email or you haven't sign up yet, ",
            "signup_text": "click here to sign up"
        }
        return render(request, 'login.html', login_error)

    else:
        return render(request, 'login.html')


@csrf_exempt
def signup(request):
    print("data : ", request.POST.get("user_email"))
    if request.method == 'POST':
        user_email = request.POST.get("user_email")
        data = UserEmail(user_email=user_email)
        data.save()
        return redirect('home')

    else:
        return render(request, 'signup.html')


def home(req):
    return render(req, 'home.html', {"range": range(7)})


# def product(req):
#     return HttpResponse("products")
#
#
# def gallery(req):
#     return render(req, 'auction_gallery.html', {'content': 'auction_gallery.html'})
#
#
# def my_posts(req):
#     return render(req, 'home.html', {'content': 'my_post.html'})
