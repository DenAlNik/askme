from typing import List, Dict
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer, Rate, Profile, Tag, User
from .models import ManagerQuestion, ManagerAnswer

# Create your views here.
# QUESTIONS = [
#         {
#             'id': i,
#             'title': f'Question {i}',
#             'content': f'Long lorem ipsum {i}',
#             'tags': ['HTML5', 'Python', 'C++']
#         }for i in range(1, 2000)
#     ]
# ANSWERS = [
#         {
#             'id': i,
#             'title': f'Answer {i}',
#             'content': f'Long lorem ipsum {i}'
#         } for i in range(1, 100)
#     ]
# TAGS = [
#     {
#         'id': i,
#         'tag_name': f"Tag {i}"
#     } for i in range(1, 21)
# ]


MEMBERS = User.objects.all()[:10]
TAGS = Tag.objects.all()[:20]



def paginate(object, page, per_page=20):
    return Paginator(object, per_page).get_page(page)


def index(request):
    questions = Question.objects.new_sort()
    return render(request, template_name='index.html', context={'page': paginate(questions, request.GET.get('page')),
                                                                'members': MEMBERS, 'tags': TAGS})


def hot(request):
    questions = Question.objects.hot_sort()
    return render(request, template_name='hot.html', context={'page': paginate(questions, request.GET.get('page')),
                                                                'members': MEMBERS, 'tags': TAGS})


def question(request, question_id):
    item = Question.objects.get(pk=question_id)
    answers = item.answers.sort_answer()
    return render(request, template_name='question.html', context={'question': item, 'page': paginate(answers, request.GET.get('page'), 30),
                                                                'members': MEMBERS, 'tags': TAGS})


def tag(request, tag_name):
    questions = Question.objects.has_tag(tag_name)
    return render(request, template_name='tag.html', context={'tag_name': tag_name, 'page': paginate(questions, request.GET.get('page'), 20),
                                                                'members': MEMBERS, 'tags': TAGS, 'questions': questions})


def ask(request):
    return render(request, template_name='ask.html', context={'members': MEMBERS, 'tags': TAGS})


def signup(request):
    return render(request, template_name='signup.html', context={'members': MEMBERS, 'tags': TAGS})


def login(request):
    return render(request, template_name='login.html', context={'members': MEMBERS, 'tags': TAGS})


def settings(request):
    return render(request, template_name='settings.html', context={'members': MEMBERS, 'tags': TAGS})