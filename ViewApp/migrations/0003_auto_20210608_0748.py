# Generated by Django 2.2 on 2021-06-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ViewApp', '0002_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='pwd',
        ),
    ]
