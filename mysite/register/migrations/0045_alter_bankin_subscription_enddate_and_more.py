# Generated by Django 4.0.2 on 2022-04-28 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0044_alter_bankin_subscription_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankin',
            name='subscription_enddate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 13, 16, 6, 680778, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='subscription_enddate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 13, 16, 6, 679772, tzinfo=utc)),
        ),
    ]
