# Generated by Django 3.2.5 on 2022-07-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='my post', max_length=225),
        ),
    ]
