# Generated by Django 4.0.5 on 2023-07-05 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0027_alter_contractmodel_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 12, 58, 30, 461356, tzinfo=utc)),
        ),
    ]
