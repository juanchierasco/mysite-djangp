from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by("-date") # PARA ORDENAR DE MENOR A MAYOR

    context = {
        "questions" : questions
    }

    return render(request, "index.html", context)

def detail(request , question_id):
    return HttpResponse(f"This is questions number: {question_id}")
# Ó return HttpResponse("This is questions number: " + question_id)

    
