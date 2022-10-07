from django.urls import path
from . import views




app_name = 'polls'  # define a namespace url for this app. for all path 
# in this app(poll) we gotta use polls:urlname like polls:detail

urlpatterns = [
    # defines how to handle GET url request
    # defined a path '' cuz view.py is in the root
    # import view and index function we wrote
    # ex: /polls/
    #path('', views.index, name='index'),  #  let django know how to guide it to poll app
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),

    # USE GENETIC VIEW INSTEAD OF OUR functions FOR INDEX, DETAIL, AND RESULT
    # VOTE LOGIC IS OUR OWN
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]