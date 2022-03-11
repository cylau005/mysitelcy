# Generated by Django 4.0.2 on 2022-03-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_movielist_date_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='movie_image_url',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='overall_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
