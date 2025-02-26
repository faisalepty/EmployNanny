# Generated by Django 4.0.5 on 2023-06-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0023_alter_contractmodel_end_date'),
        ('payment', '0006_advancepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancepayment',
            name='direct_contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobapp.directcontract'),
        ),
        migrations.AlterField(
            model_name='advancepayment',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobapp.contractmodel'),
        ),
    ]
