from django import forms
from quiz.models import Topic


class UploadFileForm(forms.Form):
    CHOICES = [('-','-'),('|','|')]
    topic = forms.CharField(max_length = 100)
    file = forms.FileField()
    selector = forms.ChoiceField(label='Delimiter',choices=CHOICES)

class SelectorUploadFileForm(forms.Form):
    topic_CHOICES = [(x.topic_name,x.topic_name) for x in Topic.objects.all()]
    delimiter_choices = [('-','-'),('|','|')]
    file = forms.FileField()
    topic_selector = forms.ChoiceField(label="Topic", choices=topic_CHOICES)
    delimiter_selector = forms.ChoiceField(label='Delimiter', choices=delimiter_choices)
