# Generated by Django 2.0.13 on 2019-12-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendancebook', '0008_studentclass_availabile_divisions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentclass',
            name='availabile_divisions',
        ),
        migrations.AddField(
            model_name='studentclass',
            name='available_divisions',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.ClassDivision'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.StudentClass'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='class_division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.ClassDivision'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.StudentClass'),
        ),
    ]