from django.contrib import admin
from .models import *


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname', 'number']
    list_display = ['name', 'surname', 'group', 'number', 'login', 'rating', 'point']
    list_filter = ['group']
    ordering = ['-rating']


class LeaderBoardAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname', 'number']
    list_display = ['name', 'surname', 'group', 'number', 'login', 'rating', 'point', 'correct_answers']
    list_filter = ['group']
    ordering = ['-rating']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'count_of_questions', 'count_correct_ans']

    def count_of_questions(self, obj):
        return obj.question.count()


class AnswerQuestionInlineAdmin(admin.TabularInline):
    model = AnswerQuestion
    max_num = 4
    min_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerQuestionInlineAdmin]

    class Meta:
        model = Question


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGroup)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(AnswerQuestion)
admin.site.register(AnswerPlayer)
admin.site.register(Question, QuestionAdmin)
admin.site.register(LeaderBoard, LeaderBoardAdmin)
