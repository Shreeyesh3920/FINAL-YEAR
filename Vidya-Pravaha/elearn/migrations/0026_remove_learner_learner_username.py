# Generated by Django 4.2.5 on 2023-09-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("elearn", "0025_learner_learner_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="learner",
            name="learner_username",
        ),
    ]