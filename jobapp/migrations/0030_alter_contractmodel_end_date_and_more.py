# Generated by Django 4.0.5 on 2023-07-10 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0029_alter_contractmodel_end_date_alter_jobmodel_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 9, 9, 58, 34, 703100, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='directcontract',
            name='city',
            field=models.CharField(choices=[('kileleshwa', 'Kileleshwa'), ('dandora', 'Dandora'), ('westlands', 'Westlands'), ('parklands', 'Parklands'), ('langata', "Lang'ata"), ('karen', 'Karen'), ('lavington', 'Lavington'), ('kilimani', 'Kilimani'), ('runda', 'Runda'), ('roysambu', 'Roysambu'), ('eastleigh', 'Eastleigh'), ('buruburu', 'Buruburu'), ('south_c', 'South C'), ('south_b', 'South B'), ('kasarani', 'Kasarani'), ('embakasi', 'Embakasi'), ('kawangware', 'Kawangware'), ('madaraka', 'Madaraka'), ('hurlingham', 'Hurlingham'), ('ngong_road', 'Ngong Road'), ('airport_west', 'Airport West'), ('banana_hill', 'Banana Hill'), ('gigiri', 'Gigiri'), ('industrial_area', 'Industrial Area'), ('juja', 'Juja'), ('kibera', 'Kibera'), ('limuru', 'Limuru'), ('lower_kabete', 'Lower Kabete'), ('muthaiga', 'Muthaiga')], max_length=100),
        ),
    ]
