from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category


class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.FloatField()
    image = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="")
    lister = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="lister")
    watcher = models.ManyToManyField(User, blank=True, null=True, related_name="watcher")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by {self.lister}"
    
    def empty_image(self):
        return f""


class Bid(models.Model):
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE)
    new_bid = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} bids ${self.new_bid} on {self.listing}"


class Comment(models.Model):
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="deleted_user")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} commented on {self.listing}: {self.comment}"