# Generated by Django 4.0.6 on 2022-09-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_games_hintsused_alter_games_modifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='hintsUsed',
            field=models.IntegerField(default=0),
        ),
    ]
