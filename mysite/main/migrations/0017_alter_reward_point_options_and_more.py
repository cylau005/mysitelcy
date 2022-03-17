# Generated by Django 4.0.2 on 2022-03-17 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_reward_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reward_point',
            options={'ordering': ['user_id']},
        ),
        migrations.AddField(
            model_name='reward_point',
            name='redeem_item_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.prizelist'),
        ),
    ]