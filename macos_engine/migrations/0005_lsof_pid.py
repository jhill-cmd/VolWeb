# Generated by Django 3.2.18 on 2023-05-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macos_engine', '0004_auto_20230525_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='lsof',
            name='PID',
            field=models.BigIntegerField(null=True),
        ),
    ]