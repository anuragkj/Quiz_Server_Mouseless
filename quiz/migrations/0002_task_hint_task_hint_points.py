# Generated by Django 4.0 on 2022-08-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='hint',
            field=models.CharField(default='No hint!!', max_length=256),
        ),
        migrations.AddField(
            model_name='task',
            name='hint_points',
            field=models.IntegerField(default=0),
        ),
    ]
