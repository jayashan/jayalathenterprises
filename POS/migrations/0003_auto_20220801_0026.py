# Generated by Django 3.2.5 on 2022-08-01 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0002_category_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]