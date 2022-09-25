# Generated by Django 4.0.6 on 2022-09-23 20:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_description_products_price_products_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier', models.FloatField()),
                ('TotalScore', models.IntegerField()),
                ('roundNumber', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
