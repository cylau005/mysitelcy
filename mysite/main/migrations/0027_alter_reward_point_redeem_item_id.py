# Generated by Django 4.0.2 on 2022-03-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_reward_point_redeem_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward_point',
            name='redeem_item_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]