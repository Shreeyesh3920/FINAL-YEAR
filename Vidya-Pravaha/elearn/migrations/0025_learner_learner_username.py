# Generated by Django 4.2.5 on 2023-09-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elearn", "0024_parent_learner_linked"),
    ]

    operations = [
        migrations.AddField(
            model_name="learner",
            name="learner_username",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
