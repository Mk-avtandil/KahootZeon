# Generated by Django 4.1 on 2022-09-08 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0023_alter_answerquestion_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="number",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(13),
                    django.core.validators.MinValueValidator(9),
                ]
            ),
        ),
    ]
