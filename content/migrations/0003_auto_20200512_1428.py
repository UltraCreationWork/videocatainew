# Generated by Django 3.0.5 on 2020-05-12 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_comment_postview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reviewed',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]