# Generated by Django 2.0.13 on 2019-12-30 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendancebook', '0005_auto_20191226_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classdivision',
            name='student_class',
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.StudentClass'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.StudentClass'),
        ),
    ]
