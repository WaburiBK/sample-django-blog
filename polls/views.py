#from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
# with render, no longer need to import loader
# HttpResponse retained as I still have the detail, results & vote methods

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

# render() function takes three arguments i.e request object, template
# name and dictionary as optional third argument
# it returns a HttpResonse object of given template rendered within given
# context

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
