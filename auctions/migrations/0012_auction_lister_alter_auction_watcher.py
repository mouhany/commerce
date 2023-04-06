# Generated by Django 4.1.7 on 2023-04-05 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auction_active_auction_watcher_comment_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='lister',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lister', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='watcher',
            field=models.ManyToManyField(blank=True, null=True, related_name='watcher', to=settings.AUTH_USER_MODEL),
        ),
    ]