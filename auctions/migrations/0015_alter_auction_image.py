# Generated by Django 4.1.7 on 2023-04-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.URLField(default='https://i.imgur.com/vLDtrNC.jpg'),
        ),
    ]
