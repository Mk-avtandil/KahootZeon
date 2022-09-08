from rest_framework import serializers
from .models import *


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerGroup
        fields = '__all__'


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionASerializers(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = '__all__'


class PlayerASerializers(serializers.ModelSerializer):
    class Meta:
        model = AnswerPlayer
        fields = '__all__'


class LeaderBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = '__all__'
