# Generated by Django 2.2.1 on 2019-05-31 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0002_remove_shoppinglist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]