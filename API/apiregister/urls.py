from django.urls import path
from apiregister import views

urlpatterns = [
    path('', views.TeacherRegisterView.as_view(), name='teacher_register_view'),
]