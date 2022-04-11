

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import *
from .database import *


# Create your views here.


def redirect_view(request):
    response = redirect('login')
    return response


def index(request):
    return render(request, 'index.html')


info = UserInformation()


def login(request):
    if request.method == "POST":
        current_email = request.POST.get('user_email')
        if verify_user_email(current_email):
            info.email = current_email
            return redirect('home')
        else:
            login_error = {
                "problem_text": "Entered wrong email or you haven't sign up yet, "
            }
            return render(request, 'login.html', login_error)

    else:
        return render(request, 'login.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        user_email = request.POST.get("user_email")
        if not verify_user_email(user_email):
            store_user_info(user_email)
            info.email = user_email
            return redirect('home')
        else:
            return render(request, 'signup.html', {"error": " You have already created an account. "})

    else:
        return render(request, 'signup.html')


def home(request):
    context = {
        "range": range(7),
        "user_email": info.email,
        "all_product": get_all_product()
    }
    return render(request, 'home.html', context)


def product(req):
    return HttpResponse("products")


def gallery(req):
    arg = {
        'user_email': info.email
    }
    return render(req, 'auction_gallery.html', arg)


def my_posts(req):
    arg = {
        'user_email': info.email,
        "range": range(7),
        "all_product": get_all_product_by_email(info.email)
    }
    return render(req, 'my_post.html', arg)


product_info = ProductDetails()


def form(req):
    if req.method == "POST":
        print(info.email)
        name = req.POST.get('product_name')
        detail = req.POST.get('product_detail')
        price = req.POST.get('min_bid_price')
        dtime = req.POST.get('end_date_time')
        data = {
            "user_email": info.email,
            "name": name,
            "detail": detail,
            "price": price,
            "dtime": dtime
        }
        store_product_info(data)
        product_info.set_value(data["user_email"], data["name"], data["detail"], data["price"], data["dtime"])
        return redirect('home')
    else:
        return render(req, 'form.html')
