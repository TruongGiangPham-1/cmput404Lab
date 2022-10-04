from django.urls import path
from . import views




app_name = 'polls'  # define a namespace url for this app

urlpatterns = [
    # defines how to handle GET url request
    # defined a path '' cuz view.py is in the root
    # import view and index function we wrote
    # ex: /polls/
    path('', views.index, name='index'),  #  let django know how to guide it to poll app
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]