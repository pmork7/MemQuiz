import os
from .models import Question, Answer, Topic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

def handle_uploaded_file(f):
    cwd = os.getcwd()
    fd = f'{cwd}\\'
    try:
        with open('quiz\\textfiles\\recent_file.txt','wb+') as fhandle:
            for chunk in f.chunks():
                fhandle.write(chunk)
    except FileNotFoundError:
        print('The "textfiles" directory does not exist.')

def add_questions_from_file(topic_string, f):
    for chunk in f.chunks():
        decoded = chunk.decode("utf-8")
        lines = decoded.split("\n")
        for line in lines:
            line.rstrip()
            pieces = line.split(" - ")
            question = pieces[0].rstrip()
            answer = pieces[1].rstrip()
            t = Topic()
            try:
                t = Topic.objects.get(topic_name=topic_string)
            except ObjectDoesNotExist:
                t = Topic.objects.create(topic_name=topic_string)
            q = Question.objects.create(topic=t, question_text=question, pub_date=timezone.now())
            Answer.objects.create(question=q, answer_text=answer)

'''def check_if_question_exists(question, answer):
    if (Question.objects.filter(question_text=question)):
        q = Question.objects.filter(question_text=question)
        if (Answer.objects.filter(answer_text=answer)):
            a = Answer.objects.filter(answer_text=answer)
            if (a.question=q):
                return True
    return False'''
