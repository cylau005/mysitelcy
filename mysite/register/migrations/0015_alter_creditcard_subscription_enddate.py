# Generated by Django 4.0.2 on 2022-03-19 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_alter_creditcard_subscription_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='subscription_enddate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 20, 55, 26, 874050)),
        ),
    ]
