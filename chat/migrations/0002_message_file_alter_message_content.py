# Generated by Django 5.0.7 on 2024-09-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='chat_files/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
