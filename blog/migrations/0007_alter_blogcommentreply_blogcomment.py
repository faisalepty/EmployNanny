# Generated by Django 4.2.6 on 2023-10-27 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_blogcomment_blogcommentreply_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcommentreply',
            name='blogcomment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]
