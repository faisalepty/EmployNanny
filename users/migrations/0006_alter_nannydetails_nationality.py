# Generated by Django 4.0.5 on 2023-06-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_nannydetails_id_back_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nannydetails',
            name='nationality',
            field=models.CharField(choices=[('kenyan', 'Kenyan'), ('nigerian', 'Nigerian'), ('south_african', 'South African'), ('ethiopian', 'Ethiopian'), ('egyptian', 'Egyptian')], max_length=100),
        ),
    ]
