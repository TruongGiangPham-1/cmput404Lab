from django.urls import path
from . import views

urlpatterns = [
    # defined a path '' cuz view.py is in the root
    # import view and index function we wrote
  path('', views.index, name='index'),  #  let django know how to guide it to poll app
]