from django.urls import path
from . import views

app_name = 'ask_questions'
urlpatterns = [

    # path('<int:question_id>/', views.display_questions, name='displayQuestions'),
    path('summary/', views.summry_api, name='summaryApi'),
    path('tagging/', views.tag_api, name='tagApi'),
    path('module/<str:mod>/', views.submit_question, name='submitQuestions'),
]