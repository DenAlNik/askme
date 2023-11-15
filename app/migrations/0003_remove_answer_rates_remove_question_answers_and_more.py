# Generated by Django 4.2.7 on 2023-11-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_avatar_alter_answer_author_alter_answer_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='rates',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='rates',
        ),
        migrations.AddField(
            model_name='answer',
            name='rates',
            field=models.ManyToManyField(blank=True, default=0, null=True, to='app.rate'),
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(blank=True, null=True, to='app.answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='rates',
            field=models.ManyToManyField(blank=True, null=True, to='app.rate'),
        ),
    ]