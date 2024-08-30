# Generated by Django 5.0.7 on 2024-08-29 08:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_tag_options_rename_tag_text_tag_title_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='thumbs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbsdown',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbsup',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.BooleanField(default=None),
        ),
    ]
