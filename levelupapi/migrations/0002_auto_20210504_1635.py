# Generated by Django 3.2 on 2021-05-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='gamer',
            new_name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.AttendingGamer', to='levelupapi.Gamer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
    ]
