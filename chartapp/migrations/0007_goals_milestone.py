# Generated by Django 4.2.5 on 2023-09-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0006_goals1_goals2_remove_goals_month_remove_goals_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='milestone',
            field=models.IntegerField(null=True),
        ),
    ]