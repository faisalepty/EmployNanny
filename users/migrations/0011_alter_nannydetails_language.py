# Generated by Django 4.0.5 on 2023-07-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_employerprofile_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nannydetails',
            name='language',
            field=models.CharField(choices=[('Kamba', 'Kamba'), ('Kikuyu', 'Kikuyu'), ('Luhya', 'Luhya'), ('Kiswahili', 'Kiswahili'), ('English', 'English'), ('Luo', 'Luo'), ('Kalenjin', 'Kalenjin'), ('Meru', 'Meru'), ('Embu', 'Embu'), ('Maasai', 'Maasai'), ('Kisii', 'Kisii'), ('Turkana', 'Turkana'), ('Mijikenda', 'Mijikenda'), ('Somali', 'Somali'), ('Swahili', 'Swahili'), ('Rendille', 'Rendille'), ('Samburu', 'Samburu'), ('Orma', 'Orma'), ('Taita', 'Taita'), ('Giriama', 'Giriama'), ('Pokomo', 'Pokomo'), ('Dahalo', 'Dahalo'), ('Gusii', 'Gusii'), ('Ribe', 'Ribe'), ('Tharaka', 'Tharaka'), ('Bajuni', 'Bajuni'), ('Tesoo', 'Tesoo'), ('Kupsabiny', 'Kupsabiny'), ('Chonyi', 'Chonyi'), ('Wanga', 'Wanga'), ('Kuria', 'Kuria'), ('Kikamba', 'Kikamba'), ('Ogiek', 'Ogiek'), ('El Molo', 'El Molo'), ('Nandi', 'Nandi'), ('Segeju', 'Segeju')], max_length=200),
        ),
    ]
