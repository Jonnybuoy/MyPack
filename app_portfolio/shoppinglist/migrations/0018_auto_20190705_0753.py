# Generated by Django 2.2.1 on 2019-07-05 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0017_auto_20190705_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 7, 53, 29, 329231, tzinfo=utc)),
        ),
    ]
