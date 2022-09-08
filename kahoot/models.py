from django.db import models
import hashlib


class Player(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    group = models.ForeignKey('PlayerGroup', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        result = hashlib.sha256(self.password.encode())
        self.password = result.hexdigest()
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PlayerGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class AnswerQuestion(models.Model):
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    question = models.ManyToManyField(Question)
    group = models.ForeignKey(PlayerGroup, on_delete=models.CASCADE)
    count_of_question = models.IntegerField(default=0)
    count_correct_ans = models.IntegerField(default=0)
    time = models.IntegerField(default=20)
    point = models.IntegerField(default=100)

    def __str__(self):
        return self.title


class AnswerPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    player_answer = models.CharField(max_length=100)
    fact_time = models.IntegerField()

    def __str__(self):
        return self.player_answer


class LeaderBoard(Player, models.Model):
    class Meta:
        proxy = True


