# Generated by Django 4.0.2 on 2022-03-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_reward_point_redeem_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward_point',
            name='redeem_item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prizelist'),
        ),
    ]
