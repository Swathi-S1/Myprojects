from django.shortcuts import render,redirect
from django.views import View
from .forms import UserForm,ClassDivisionForm,StudentClassForm,LoginForm
from attendancebook.models import StudentClass,ClassDivision,Teacher,Student,StudentAttendance
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import generic
import datetime
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
class TeacherRegisterView(View):

    def get(self,request):
        user_register_form = UserForm()
        student_class=StudentClassForm()
        student_division = ClassDivisionForm()
        return render(request,"attendancebook/teacherregistration.html",
                            {'user_register_form':user_register_form,
                                'student_class':student_class, 
                                    'student_division':student_division})

    def post(self,request):
        user_register_form = UserForm(request.POST)
        student_division = ClassDivisionForm(request.POST)
        student_class = StudentClassForm(request.POST)
        print(user_register_form.errors)
        if user_register_form.is_valid() and student_division.is_valid() and student_class.is_valid():    
            user = user_register_form.save(commit=False)
            username = user_register_form.cleaned_data['username']
            password1 = user_register_form.cleaned_data['password1']
            user.set_password(password1)
            user.save()
            classname = request.POST.get('student_classname')
            division=request.POST.get('division_name')
            try:
                teacher_class = ClassDivision.objects.get(student_class__student_classname=classname,division_name=division)
            except:
                teacher_class = None
            if teacher_class:
                teacher=Teacher.objects.create(user=user,class_division=teacher_class)
                user_register_form.save()
                teacher.save()
                return redirect("login_view/")
            else:
                messages.add_message(request, messages.INFO,'Invalid Class Division')
                return render(request,"attendancebook/teacherregistration.html",
                    {'user_register_form':user_register_form,
                                'student_class':student_class, 
                                    'student_division':student_division}) 

        else:
            messages.add_message(request, messages.INFO,'form information are not valid')
            return render(request,"attendancebook/teacherregistration.html",
                    {'user_register_form':user_register_form,
                                'student_class':student_class, 
                                    'student_division':student_division})


class TeacherLogin(View):
    def get(self,request):
        teacher_login = LoginForm()
        return render(request,'attendancebook/teacherlogin.html',{'teacher_login':teacher_login})
    def post(self,request):
        teacher_login = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('class_division',id=request.user.teacher.class_division.id)
        else:
            messages.add_message(request,messages.INFO,'Invalid User Details...')
            return redirect('login_view')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('teacher_register_view')


# class ClassListView(LoginRequiredMixin,generic.ListView):
#     login_url = '/login_view/'
#     model = StudentClass
#     template_name = "attendancebook/studentclass-list.html"

    
# class ClassDetailView(LoginRequiredMixin,generic.DetailView):
#     login_url = '/login_view/'
#     model = ClassDivision

#     def get(self,request, *args, **kwargs):
        
#         division_list = ClassDivision.objects.filter(student_class=self.kwargs['id'])
#         return render(request,'attendancebook/division_list.html',{'division_list':division_list})
class ClassDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/login_view/'
    model = Teacher

    def get(self,request, *args, **kwargs):
        
        division_list = Teacher.objects.filter(class_division=self.kwargs['id'])
        print(self.kwargs['id'])
        return render(request,'attendancebook/division_list.html',{'division_list':division_list})


class StudentDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/login_view/'
    model = Student

    def get(self,request,*args,**kwargs):
        students_list = Student.objects.filter(class_division=self.kwargs['id'])
        print(self.kwargs['id'])
        return render(request,'attendancebook/student_list.html',{'students_list':students_list}) 


class MarkAttendance(LoginRequiredMixin,View):
    login_url = '/login_view/'

    def post(self,request):
        stud_id = request.POST.get('stud_id')
        attendance = request.POST.get('mark_attendance')
        student = Student.objects.get(id=stud_id)
        try:
            if (attendance == 'true'):
                attendance_list = StudentAttendance.objects.create(student=student,mark_attendance=True)
            else:
                attendance_list = StudentAttendance.objects.create(student=student,mark_attendance=False)

            data={'status':'success'}

        except:
            data={'status':'fail'}

        return JsonResponse(data) 



# class AttendanceListView(LoginRequiredMixin,View):
#     login_url = '/login_view/'
#     def get(self,request):
#         attendance_list = StudentAttendance.objects.filter(date=date)    
    
      
        