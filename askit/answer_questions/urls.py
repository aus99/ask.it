from django.urls import path
from . import views

app_name = 'answer_questions'
urlpatterns = [
    path('<int:question_id>/', views.view_question, name='view_question'),
    path('<int:question_id>/submit_answer/', views.submit_answer, name='submit_answer'),
    path('<int:question_id>/answer/<int:answer_id>/delete_answer/', views.delete_answer, name='delete_answer'),
    path('<int:question_id>/submit_comment/', views.submit_comment, name='submit_comment'),
    path('<int:question_id>/comment/<int:com_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:question_id>/upvote/', views.upvote_question, name='upvote'),
    path('<int:question_id>/downvote/', views.downvote_question, name='downvote'),
    path('<int:question_id>/answer/<int:answer_id>/upvote/', views.upvote_answer, name='upvote_answer'),
    path('<int:question_id>/answer/<int:answer_id>/downvote/', views.downvote_answer, name='downvote_answer'),
    path('<int:question_id>/delete/',views.delete_question, name='delete_question'),
    path('<int:question_id>/accept_answer/<int:answer_id>/', views.accept_answer, name='accept_answer'),
    path('RESET/', views.set_up_test_database, name='set_up_test_database'),
]