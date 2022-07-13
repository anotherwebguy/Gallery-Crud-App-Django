from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("new/", views.new, name='new'),
    path("show/:<id>", views.show, name='show'),
    path(":<id>/edit", views.edit, name='edit'),
    path("delete/:<id>", views.delete, name='delete'),
]