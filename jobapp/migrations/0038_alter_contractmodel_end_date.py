# Generated by Django 4.2.6 on 2023-10-27 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0037_alter_contractmodel_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 26, 6, 29, 58, 191062, tzinfo=datetime.timezone.utc)),
        ),
    ]
