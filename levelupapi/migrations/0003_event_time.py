# Generated by Django 3.2 on 2021-05-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20210504_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='09:30'),
            preserve_default=False,
        ),
    ]
