# Generated by Django 2.2.1 on 2019-07-08 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0024_auto_20190707_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 9, 23, 17, 123271, tzinfo=utc)),
        ),
    ]
