# Generated by Django 2.2.1 on 2019-07-07 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0023_auto_20190705_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 11, 27, 36, 243754, tzinfo=utc)),
        ),
    ]
