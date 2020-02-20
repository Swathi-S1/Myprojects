# Generated by Django 2.0.13 on 2019-12-30 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendancebook', '0006_auto_20191230_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.ClassDivision'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='class_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.ClassDivision'),
        ),
    ]
