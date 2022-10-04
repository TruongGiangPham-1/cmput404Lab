from django.shortcuts import get_object_or_404 ,render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}  # make it a dictionary
    # feed index.html the list of questions []
    return render(request, 'polls/index.html', context)  # render the output with index.html template

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # this is django method
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # question_id is from /polls/question_id, ex /polls/38
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)