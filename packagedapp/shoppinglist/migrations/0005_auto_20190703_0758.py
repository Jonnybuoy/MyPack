# Generated by Django 2.2.1 on 2019-07-03 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0004_shoppinglist_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='price',
        ),
    ]