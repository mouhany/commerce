from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/all", views.all, name="all"),
    path("listing/closed", views.closed, name='closed'),
    path("category", views.category, name="category"),
    path("category/<str:category>", views.listing_category, name="listing_category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
