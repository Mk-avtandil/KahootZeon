from django.db.models import F
from random import randint
from .models import *


def calc_points(self, request):
    client_query = AnswerQuestion.objects.filter(question_id=request.data['question']).values()
    spend_time = int(request.data['fact_time'])
    player_answer = request.data['player_answer'].lower()
    question_answer = AnswerQuestion.objects.filter(
        question_id=client_query[0]['question_id'], is_correct=True).values('answer')[0]['answer']

    try:
        quiz_time = Quiz.objects.filter(question=client_query[0]['question_id']).values('time')[0]['time']
        quiz_point = Quiz.objects.filter(question=client_query[0]['question_id']).values('point')[0]['point']
    except IndexError:
        quiz_time = 20
        quiz_point = 100

    if player_answer == str(question_answer).lower():
        Quiz.objects.filter(question=client_query[0]['question_id']).update(
            count_correct_ans=F('count_correct_ans')+1)
        Player.objects.filter(pk=request.data['player']).update(
            correct_answers=F('correct_answers')+1, rating=F('rating')+1)

        if spend_time == 1:
            res = quiz_point - (quiz_point / quiz_time * spend_time + quiz_point / quiz_time)
            Player.objects.filter(pk=request.data['player']).update(point=F('point') + res)
        elif spend_time > 1:
            res = quiz_point - (quiz_point / quiz_time * spend_time)
            Player.objects.filter(pk=request.data['player']).update(point=F('point') + res)
    return request
