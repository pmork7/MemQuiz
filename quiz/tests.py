import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .models import Question
from .forms import UploadFileForm

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['question_list'], [])

    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() returns False for questions
        whose pub_date is in the future.
        '''

        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        '''
        was_published_recently() returns True for question_list
        who pub_date is within the last day.
        '''
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_future_question_and_past_question(self):
        '''
        Even if both past and future questions exist, only
        past questions are displayed.
        '''
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('quiz:index'))
        self.assertQuerySetEqual(
            response.context['question_list'],
            [question],
        )

    def test_two_past_questions(self):
        '''
        The quiz index displays multiple questions in the correct order
        '''
        question1 = create_question(question_text="Past question 1", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse('quiz:index'))
        self.assertQuerySetEqual(
            response.context['question_list'],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_questions(self):
        '''
        The detail view of a question with a pub_date in the future returns
        a response of 404 not found.
        '''
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('quiz:detail',args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_questions(self):
        past_question = create_question(question_text="Past question.", days=-5)
        url = reverse('quiz:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class UploadFileFormTests(TestCase):
    def test_file_upload(self):
        selenium = webdriver.Chrome('C:\\bin\\101\\chromedriver.exe')
        selenium.get('http://127.0.0.1:8000/quiz/newupload')
        print(selenium.page_source)
        file = selenium.find_element_by_id("id_file")
        topic_name = selenium.find_element_by_id("id_topic")
        submit_button = selenium.find_element_by_id("submit_button")

        topic_name.send_keys('COMPTIA')
        file.send_keys('C:\\Users\\paula\\CS\\COMPTIA Quiz\\QuestionBank.txt')
        submit_button.send_keys(Keys.RETURN)
        print(selenium.page_source)
