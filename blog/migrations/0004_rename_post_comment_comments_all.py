# Generated by Django 4.1.13 on 2024-01-13 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='comments_all',
        ),
    ]
