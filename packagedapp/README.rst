=====
Shoppinglist
=====

Shoppinglist is a simple Django app designed to keep a record of shoppinglist
items for easy remembrance.


Quick start
-----------

1. Add "shoppinglist" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'shoppinglist',
    ]

2. Include the application's URLconf in your project urls.py like this::

    path('', include('shoppinglist.urls')),

3. Run `python manage.py migrate` to create the shoppinglist models.

4. Start the development server and visit http://127.0.0.1:8000/add/
   to add an item to your list.

5. Visit http://127.0.0.1:8000 to view your list.
