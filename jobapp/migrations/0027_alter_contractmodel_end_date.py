# Generated by Django 4.0.5 on 2023-07-04 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0026_alter_contractmodel_end_date_alter_jobmodel_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 11, 17, 51, 60238, tzinfo=utc)),
        ),
    ]
