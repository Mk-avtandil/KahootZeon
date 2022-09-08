from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/kahoot_player/read/', KahootListView.as_view(), name='player_read'),
    path('api/v1/kahoot_player/create/', KahootCreateView.as_view()),
    path('api/v1/kahoot_player/upd/del/<int:pk>/', KahootUpdateDestroyView.as_view()),

    path('api/v1/kahoot_group/read/', KahootGroupListView.as_view(), name='group_read'),
    path('api/v1/kahoot_group/create/', KahootGroupCreateView.as_view()),
    path('api/v1/kahoot_group/upd/del/<int:pk>/', KahootGroupUpdateDestroyView.as_view()),

    path('api/v1/kahoot_question/read/', KahootQuestionListView.as_view(), name='test_read'),
    path('api/v1/kahoot_question/create/', KahootQuestionCreateView.as_view()),
    path('api/v1/kahoot_question/upd/del/<int:pk>/', KahootQuestionUpdateDestroyView.as_view()),

    path('api/v1/kahoot_question_answer/read/', KahootQuestionAListView.as_view()),
    path('api/v1/kahoot_question_answer/create/', KahootQuestionACreateView.as_view()),
    path('api/v1/kahoot_question_answer/upd/del/<int:pk>/', KahootQuestionAUpdateDestroyView.as_view()),

    path('api/v1/kahoot_player_answer/read/', KahootPlayerAListView.as_view()),
    path('api/v1/kahoot_player_answer/create/', KahootPlayerACreateView.as_view()),
    path('api/v1/kahoot_player_answer/upd/del/<int:pk>/', KahootPlayerAUpdateDestroyView.as_view()),

    path('api/v1/kahoot_leader_board/', LeaderBoardListView.as_view()),
]
