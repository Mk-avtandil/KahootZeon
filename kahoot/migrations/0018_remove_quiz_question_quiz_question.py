# Generated by Django 4.1 on 2022-09-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0017_rename_answer1_answerquestion_answer_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="quiz", name="question",),
        migrations.AddField(
            model_name="quiz",
            name="question",
            field=models.ManyToManyField(to="kahoot.question"),
        ),
    ]
