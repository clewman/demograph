# Generated by Django 2.1.2 on 2018-11-08 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0010_data_parameters'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Data_Parameters',
            new_name='Data_Parameter',
        ),
    ]
