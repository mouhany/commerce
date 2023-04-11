from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/all", views.all, name="all"),
    path("listing/closed", views.closed, name='closed'),
    path("listing/<int:id>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_name>", views.listing_category, name="listing_category"),
    path("create", views.create, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
