# Generated by Django 4.0.2 on 2022-05-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_rename_cfview_list_interact_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward_point',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]