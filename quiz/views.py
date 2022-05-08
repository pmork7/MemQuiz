from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .filefunctions import add_questions_from_file
from .forms import UploadFileForm, SelectorUploadFileForm
from .models import Question, Answer, Topic

def index(request):
    if request.method == "POST":
        print(request.POST)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            add_questions_from_file(request.POST['topic'], request.FILES['file'])
            return HttpResponseRedirect(reverse('quiz:congrats'))
    else:
        written_form = UploadFileForm()
        def get_queryset():
            return Topic.objects.all()

        topic_list = get_queryset();
        template = loader.get_template('quiz/index.html')
        context = {
            'topic_list':topic_list,
        }
    return render(request, 'quiz/index.html', context)

def detail(request, topic_id):
    def get_queryset():
        return Topic.objects.get(pk = topic_id).question_set.all()

    try:
        topic_questions = get_queryset()
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist.")
    return render(request, 'quiz/detail.html', {"topic_questions": topic_questions})


def congrats(request):
    return render(request, 'quiz/congrats.html')

def newupload(request):
    written_form = UploadFileForm()
    context = {'written_form': written_form}
    return render(request, 'quiz/newupload.html', context)

def oldupload(request):
    selector_form = SelectorUploadFileForm()
    context = {'selector_form': selector_form}
    return render(request, 'quiz/oldupload.html', context)
