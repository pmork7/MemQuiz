from django.urls import path
from . import views


app_name = "quiz"
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:topic_id>/', views.detail, name='detail'),
  path('congrats', views.congrats, name='congrats'),
  path('newupload', views.newupload, name='newupload'),
  path('oldupload', views.oldupload, name='oldupload'),
]
