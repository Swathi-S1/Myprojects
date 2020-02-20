from django.urls import path
from attendancebook import views

urlpatterns = [
    path('', views.TeacherRegisterView.as_view(), name='teacher_register_view'),
    path('login_view/', views.TeacherLogin.as_view(), name='login_view'),
    path('logout_view/',views.LogoutView.as_view(),name='logout_view'),
    # path('home/', views.ClassListView.as_view(), name='home'),
    path('division/<int:id>/',views.ClassDetailView.as_view(),name='class_division'),
    path('student_list/<int:id>/',views.StudentDetailView.as_view(),name='student_list'),
    path('mark_attendance/',views.MarkAttendance.as_view(),name='mark_attendance'),

]   