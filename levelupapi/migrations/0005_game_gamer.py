# Generated by Django 3.2 on 2021-05-27 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_game_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
    ]
