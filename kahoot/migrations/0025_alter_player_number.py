# Generated by Django 4.1 on 2022-09-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0024_alter_player_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="number",
            field=models.PositiveIntegerField(max_length=13),
        ),
    ]
