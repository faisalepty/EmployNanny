# Generated by Django 4.0.5 on 2023-06-14 18:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_alter_contractmodel_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 14, 18, 4, 31, 963363, tzinfo=utc)),
        ),
    ]
