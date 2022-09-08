# Generated by Django 4.1 on 2022-09-08 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0019_remove_answerplayer_quiz_answerplayer_question"),
    ]

    operations = [
        migrations.RemoveField(model_name="question", name="answer",),
        migrations.AddField(
            model_name="answerquestion",
            name="question",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="kahoot.question",
            ),
            preserve_default=False,
        ),
    ]
