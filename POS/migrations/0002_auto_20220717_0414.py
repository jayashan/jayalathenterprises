# Generated by Django 3.2.5 on 2022-07-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='traffic',
            field=models.IntegerField(default=0),
        ),
    ]