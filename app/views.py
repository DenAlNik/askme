from typing import List, Dict

from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}',
            'tags': ['HTML5', 'Python', 'C++']
        }for i in range(1, 2000)
    ]
ANSWERS = [
        {
            'id': i,
            'title': f'Answer {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(1, 100)
    ]

# def paginate(objects, page, per_page=20):
#     paginator = Paginator(objects, per_page)
#     return paginator.page(page)


def index(request):
    paginator = Paginator(QUESTIONS, 20)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='index.html', context={'questions': page, 'page': page,'paginator': paginator})

def hot(request):
    paginator = Paginator(QUESTIONS, 20)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='hot.html', context={'questions': page, 'page': page, 'paginator': paginator})

def question(request, question_id):
    paginator = Paginator(ANSWERS, 30)
    item = QUESTIONS[question_id - 1]
    page = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='question.html', context={'question': item, 'answers': page, 'page': page, 'paginator': paginator})

def tag(request, tag_name):
    paginator = Paginator(QUESTIONS, 20)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='tag.html', context={'tag_name': tag_name, 'questions': page, 'page': page, 'paginator': paginator})

def ask(request):
    return render(request, template_name='ask.html')

def signup(request):
    return render(request, template_name='signup.html')

def login(request):
    return render(request, template_name='login.html')

def settings(request):
    return render(request, template_name='settings.html')