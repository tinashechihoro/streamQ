import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from wx.py.tests.test_introspect import Q


class Question(models.Model):
    """
    Question Model
    """
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    user = models.ForeignKey(User)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Comment(models.Model):
    """
    Comment Model
    """

    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
class Disqus(models.Model):
    """
    Disqus Model
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=35, null=True)
    body = models.TextField()
    entry = models.ForeignKey(Question)

    class meta:
        ordering = ['-created']

    def __str__(self):
        return "{0}s: {1}".format(self.entry, self.body[:60])