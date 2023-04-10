from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Category #, Bid, Comment


def index(request, active=True):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(active=active).order_by('title'),
        "headline": "Active Listings:"
    })
    
    
def all(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all().order_by('title'),
        "headline": "All Listings:"
    })


def closed(request, active=False):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(active=active).order_by('title'),
        "headline": "Closed Listings:"
    })


def listing(request, id):
    return render(request, "auctions/listing.html", {
        "auction": Auction.objects.get(pk=id)
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all().order_by('category')
    })


def listing_category(request, category_name):
    category = Category.objects.get(category=category_name)
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(category=category, active=True).order_by('title'),
        "headline": f"Category: {category_name}"
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
