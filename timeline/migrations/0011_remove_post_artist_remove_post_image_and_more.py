# Generated by Django 5.1.2 on 2024-10-27 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0010_post_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
