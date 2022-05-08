import datetime

from django.db import models
from django.utils import timezone

class Topic(models.Model):
    topic_name = models.CharField(max_length = 200)

    def __repr__(self):
        return f'Topic(topic_name={self.topic_name})'

    def __str__(self):
        return f'{self.topic_name}'

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    def __repr__(self):
        return f'Question(topic={self.topic},question_text={self.question_text},pub_date={self.pub_date})'

    def __str__(self):
        return f'{self.topic},{self.question_text},{self.pub_date}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length = 200)

    def __repr__(self):
        return f'Answer(question={self.question},answer={self.answer_text})'

    def __str__(self):
        return f'{self.question},{self.answer_text}'
