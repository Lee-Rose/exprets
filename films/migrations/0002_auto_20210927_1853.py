# Generated by Django 3.2.7 on 2021-09-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='film',
        ),
        migrations.AddField(
            model_name='article',
            name='actors',
            field=models.ManyToManyField(to='films.Actor'),
        ),
        migrations.AddField(
            model_name='article',
            name='year_of_release',
            field=models.IntegerField(default=2000, max_length=4),
        ),
    ]
