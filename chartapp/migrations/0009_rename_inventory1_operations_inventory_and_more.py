# Generated by Django 4.2.5 on 2023-09-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0008_realtimecommunicationmessage_alter_goals_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operations',
            old_name='inventory1',
            new_name='inventory',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='inventory2',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='nos',
        ),
        migrations.AddField(
            model_name='operations',
            name='nos1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='operations',
            name='nos2',
            field=models.IntegerField(null=True),
        ),
    ]
