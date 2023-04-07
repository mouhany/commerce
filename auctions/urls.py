from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category", views.category, name="category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("listing/all", views.all, name="all"),
    path("listing/closed", views.closed, name='closed'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
