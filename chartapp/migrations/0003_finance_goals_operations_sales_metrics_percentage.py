# Generated by Django 4.2.5 on 2023-09-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0002_metrics_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Overall', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('Month', models.IntegerField()),
                ('networth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team', models.CharField(max_length=30)),
                ('nos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('units', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='metrics',
            name='percentage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
