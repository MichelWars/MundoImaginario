# Generated by Django 5.1.1 on 2024-11-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_youtube_link_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube_link_video',
            name='link',
            field=models.URLField(),
        ),
    ]
