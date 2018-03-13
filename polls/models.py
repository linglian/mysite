# coding=utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('发布内容', max_length=200)
    pub_date = models.DateTimeField('发布日期')
    def __str__(self):
        return self.question_text
    def say_something(self):
        return 'What?!!!'
    say_something.admin_order_field = 'pub_date'
    say_something.short_description = '你说什么'

class Choice(models.Model):
    question = models.ForeignKey(Question,
        on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text