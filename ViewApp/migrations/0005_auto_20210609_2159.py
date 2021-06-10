# Generated by Django 2.2 on 2021-06-10 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ViewApp', '0004_auto_20210608_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comicpage',
        ),
        migrations.AddField(
            model_name='comic',
            name='cover_art',
            field=models.FileField(null=True, upload_to='comic'),
        ),
        migrations.AddField(
            model_name='comic',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='commentRef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='ViewApp.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='ViewApp.User'),
        ),
        migrations.CreateModel(
            name='ComicPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_no', models.IntegerField()),
                ('comic_img', models.FileField(upload_to='comic')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('comicRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='ViewApp.Comic')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='pageRef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pcomment', to='ViewApp.ComicPage'),
        ),
    ]
