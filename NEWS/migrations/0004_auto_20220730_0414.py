# Generated by Django 3.2.5 on 2022-07-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWS', '0003_post_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='not_categorize', max_length=225),
        ),
    ]
