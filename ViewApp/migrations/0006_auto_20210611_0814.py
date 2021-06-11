# Generated by Django 2.2 on 2021-06-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewApp', '0005_auto_20210609_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='liked_comments', to='ViewApp.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
