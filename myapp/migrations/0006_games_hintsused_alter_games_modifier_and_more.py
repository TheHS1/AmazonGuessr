# Generated by Django 4.0.6 on 2022-09-25 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_totalscore_games_totalscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='hintsUsed',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='games',
            name='modifier',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='games',
            name='roundNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='games',
            name='totalScore',
            field=models.IntegerField(default=0),
        ),
    ]
