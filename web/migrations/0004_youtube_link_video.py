# Generated by Django 5.1.1 on 2024-11-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_fotos_legenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='youtube_link_video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=300)),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
    ]
