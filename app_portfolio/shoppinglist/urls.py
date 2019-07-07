from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_index, name='list_index'),
    path("list_details/<int:pk>/", views.list_details, name='list_details'),
    path("add", views.list_add, name='list_add'),
    path("", views.list_delete, name='list_delete'),
]
