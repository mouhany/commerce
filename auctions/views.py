from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Auction, Category, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(active=True),
        "headline": "Active Listings:"
    })


def all(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all(),
        "headline": "All Listings:"
    })


def closed(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(active=False),
        "headline": "Closed Listings:"
    })


def listing(request, id):
    return render(request, "auctions/listing.html", {
        "auction": Auction.objects.get(pk=id),
        "comments": Comment.objects.filter(listing=id)
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })


def listing_category(request, category_name):
    category = Category.objects.get(category=category_name)
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(category=category, active=True),
        "headline": f"Category: {category_name}"
    })


@login_required(login_url='login')
def create(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            "categories" : Category.objects.all()
        })
    else:
        title = request.POST['title']
        description = request.POST['description']
        start_bid = request.POST['start_bid']
        image = request.POST['image']
        try:
            category = Category.objects.get(category=request.POST['category'])
        except:
            category = request.POST['category']
            new_category = Category(category=category)
            new_category.save()
            category = Category.objects.get(category)
        new_listing = Auction(
            title = title, 
            description = description, 
            start_bid = start_bid, 
            image = image, 
            category = category, 
            lister = request.user)
        new_listing.save()
        return redirect("index")


@login_required(login_url='login')
def comment(request, id):
    listing = Auction.objects.get(pk=id)
    comment = request.POST['comment']
    new_comment = Comment(listing=listing, user=request.user, comment=comment)
    new_comment.save()
    return redirect ("listing", id=id)


@login_required(login_url='login')
def bid(request, id):
    auction = Auction.objects.get(pk=id)
    amount = float(request.POST['bid'])
    if auction.current_bid() > amount and auction.lister != request.user and auction.active == True:
        return render(request, "auctions/listing.html", {
            "auction": auction,
            "message": "Amount should be higher than the current bid!"})
    elif auction.lister == request.user:
        return render(request, "auctions/listing.html", {
            "auction": auction,
            "message": "Can't bid on your own listing!"
        })
    elif auction.active == False:
        return render(request, "auctions/listing.html", {
            "auction": auction, 
            "message": "Can't bid on closed listing!"
        })
    else:
        bid = Bid(listing=auction, new_bid=amount, user=request.user)
        bid.save()
        return redirect ("listing", id=id)


@login_required(login_url='login')
def close(request, id):
    auction = Auction.objects.get(pk=id)
    auction.active = False
    auction.save()
    return redirect("listing", id=id)


@login_required(login_url='login')
def activate(request, id):
    auction = Auction.objects.get(pk=id)
    auction.active = True
    auction.save()
    return render(request, "auctions/listing.html", {
        "auction": auction,
        "message": "Listing active!"
    })


@login_required(login_url='login')
def watchlist(request, id):
    # User clicks "add to watchlist" from listing
    if request.method == "POST":
        auction = Auction.objects.get(pk=id)
        new_watchlist = User(watchlist=auction)
        new_watchlist.save()
        return render(request, "auctions/listing.html", {
            "auction": auction,
            "message": "Added to Watchlist!"
        })
        
@login_required(login_url='login')
def watchlists(request):
    # User clicks "watchlist" on navbar
    watchlist = request.user.watchlist.all()
    return render(request, "auctions/index.html", {
        "auctions": watchlist,
        "headline": "Watchlist:"
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
