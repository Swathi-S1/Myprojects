# Generated by Django 2.0.13 on 2019-12-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancebook', '0002_auto_20191223_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='student_classname',
            field=models.CharField(choices=[('LKG', 'LKG'), ('UKG', 'UKG'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X')], max_length=100),
        ),
    ]
