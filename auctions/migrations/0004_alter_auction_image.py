# Generated by Django 4.1.7 on 2023-04-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_descriptions_auction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.URLField(),
        ),
    ]
