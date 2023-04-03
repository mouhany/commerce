from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # watchlist


class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.FloatField()
    image = models.TextField()
    # category = models.Choices
    
    def __str__(self):
        return f"ID: {self.id} | Title: {self.title} | Description: {self.description} | Start Bid: {self.start_bid} | Image URL:{self.image}"
    


# class Bid(models.Model):
#     # current_price = 
#     # bid_price = 
#     pass


# class Comment(models.Model):
#     auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_comments")
#     comment = models.TextField()
#     date = models.DateTimeField(auto_now=True)