# Generated by Django 4.2.5 on 2023-09-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elearn", "0027_learner_learner_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="learner",
            name="learner_username",
            field=models.CharField(default="aditya", max_length=100),
        ),
    ]
