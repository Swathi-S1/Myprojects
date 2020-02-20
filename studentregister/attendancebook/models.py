from django.db import models
from django.contrib.auth.models import User

class_choices = (
    
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV'),
    ('V','V'),
    ('VI','VI'),
    ('VII','VII'),
    ('VIII','VIII'),
    ('IX','IX'),
    ('X','X'),
    
)
class_division = (
    
    ('A', 'A'),
    ('B', 'B'),
    ('C','C'),
    ('D','D'),    
)

class StudentClass(models.Model):
    student_classname = models.CharField(max_length=100, choices=class_choices)
    def __str__(self):
        return self.student_classname

    
class ClassDivision(models.Model):
    student_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE,null=True)
    division_name = models.CharField(max_length=5,choices=class_division)
    class Meta:
        unique_together = ("student_class", "division_name")

    def __str__(self):
        return str(self.student_class)+'-'+ self.division_name
        


class Teacher(models.Model):
    class_division = models.ForeignKey(ClassDivision,on_delete=models.CASCADE,null=True)
    user           = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)


class Student(models.Model):
    student_roll_no = models.CharField(max_length=100,unique=True)
    student_name    = models.CharField(max_length=100)
    class_division = models.ForeignKey(ClassDivision,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.student_name


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date    = models.DateTimeField(auto_now=True)
    mark_attendance = models.BooleanField(default=False)
    def __str__(self):  
        return str(self.student)+'-'+str(self.mark_attendance)

