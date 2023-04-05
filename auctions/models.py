from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # watchlist


class Category(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.category}"


# class Bid(models.Model):
#     current_bid = models.FloatField()

#     def __str__(self):
#         return f"{self.current_bid}"
    
    
class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.FloatField()
    # current_bid = models.ForeignKey(Bid, on_delete=models.PROTECT, related_name="price")
    image = models.URLField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name = "group")
    
    def __str__(self):
        return f"ID: {self.id} | Title: {self.title} | Description: {self.description} | Start Bid: {self.start_bid} | Image URL:{self.image}"

# class Comment(models.Model):
#     comment = models.TextField()
#     date = models.DateTimeField(auto_now=True)