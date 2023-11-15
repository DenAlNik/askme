from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class ManagerQuestion(models.Manager):
    def new_sort(self):
        return self.order_by('-date', '-rating')

    def hot_sort(self):
        return self.order_by('-rating', '-date')

    def has_tag(self, tag):
        return self.filter(tags__tag_name=tag)


class ManagerAnswer(models.Manager):
    def sort_answer(self):
        return self.order_by('-rating', '-date')


class Question(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField('Tag', related_name='questions')
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=User)
    answers = models.ManyToManyField('Answer', null=True, blank=True)
    rates = models.ManyToManyField('Rate', null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    objects = ManagerQuestion()

    def count_answers (self):
        return self.answers.all().count()

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Answer(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=User)
    rates = models.ManyToManyField('Rate', null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    correct_answer = models.BooleanField(default=False)
    objects = ManagerAnswer()

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.pk}. {self.tag_name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=256)
    avatar = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}. {self.user.username}'


class Rate(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=User)
    is_good = models.BooleanField(default=True)
    # meta
    def __str__(self):
        if (self.is_good):
            return f'{self.pk}. {self.author.username}\'s like'
        else:
            return f'{self.pk}. {self.author.username}\'s dislike'
