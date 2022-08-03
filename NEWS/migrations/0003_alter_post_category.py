# Generated by Django 3.2.5 on 2022-08-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWS', '0002_remove_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('LOCAL', 'LOCAL'), ('BUSINESS', 'BUSINESS'), ('TRADE', 'TRADE'), ('INTERNATIONAL', 'INTERNATIONAL')], default='not_categorize', max_length=225, null=True),
        ),
    ]