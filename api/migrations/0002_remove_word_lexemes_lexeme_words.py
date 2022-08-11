# Generated by Django 4.1 on 2022-08-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='lexemes',
        ),
        migrations.AddField(
            model_name='lexeme',
            name='words',
            field=models.ManyToManyField(related_name='lexemes', through='api.Link', to='api.word'),
        ),
    ]
