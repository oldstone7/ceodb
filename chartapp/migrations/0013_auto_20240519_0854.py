# Generated by Django 3.2.4 on 2024-05-19 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0012_message_room_delete_realtimecommunicationmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='asset',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='liab',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='liquid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]