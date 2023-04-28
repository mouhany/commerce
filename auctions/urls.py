from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/all", views.all, name="all"),
    path("listing/closed", views.closed, name='closed'),
    path("mylistings", views.my_listings, name="my_listings"),
    path("mybids", views.my_bids, name="my_bids"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("close/<int:id>", views.close, name="close"),
    path("activate/<int:id>", views.activate, name="activate"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_name>", views.listing_category, name="listing_category"),
    path("watchlist/<int:id>", views.watchlist, name="watchlist"),
    path("watchlist", views.watchlists, name="watchlists"),
    path("create", views.create, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
