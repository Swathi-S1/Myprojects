from django.contrib import admin
from attendancebook.models import StudentClass,ClassDivision,Teacher,Student,StudentAttendance

admin.site.register(StudentClass)
admin.site.register(ClassDivision)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentAttendance)
