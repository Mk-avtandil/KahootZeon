from rest_framework import generics
from rest_framework import filters
from .serializers import *
from .services import calc_points


# *****************Players***************** #
class KahootListView(generics.ListAPIView):
    queryset = Player.objects.all().order_by('-rating')
    serializer_class = PlayerSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'surname', 'number', 'group__title']


class KahootCreateView(generics.CreateAPIView):
    serializer_class = PlayerSerializers


class KahootUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializers
    queryset = Player.objects.all()


# *****************PlayerGroup***************** #
class KahootGroupListView(generics.ListAPIView):
    queryset = PlayerGroup.objects.all()
    serializer_class = PlayerGroupSerializers


class KahootGroupCreateView(generics.CreateAPIView):
    serializer_class = PlayerGroupSerializers


class KahootGroupUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerGroupSerializers
    queryset = PlayerGroup.objects.all()


# *******************Question******************* #
class KahootQuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers


class KahootQuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializers


class KahootQuestionUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializers
    queryset = Question.objects.all()


# *******************AnswerQuestion******************* #
class KahootQuestionAListView(generics.ListAPIView):
    queryset = AnswerQuestion.objects.all()
    serializer_class = QuestionASerializers


class KahootQuestionACreateView(generics.CreateAPIView):
    serializer_class = QuestionASerializers


class KahootQuestionAUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionASerializers
    queryset = AnswerQuestion.objects.all()


# *******************PlayerAnswer***************** #
class KahootPlayerAListView(generics.ListAPIView):
    queryset = AnswerPlayer.objects.all()
    serializer_class = PlayerASerializers


class KahootPlayerACreateView(generics.CreateAPIView):
    serializer_class = PlayerASerializers

    def post(self, request):
        return self.create(calc_points(self, request))


class KahootPlayerAUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerASerializers
    queryset = AnswerPlayer.objects.all()


class LeaderBoardListView(generics.ListAPIView):
    queryset = LeaderBoard.objects.all()
    serializer_class = LeaderBoardSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'surname', 'number', 'group__title']
