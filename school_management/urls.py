from django.urls import path

from . import views

urlpatterns = [
    path('students', views.StudentApiView.as_view(), name='students'),
    path('students/<str:student_uid>', views.StudentDetailApiView.as_view(), name='student_detail'),
    path('teachers', views.TeacherApiView.as_view(), name='teachers'),
    path('teachers/<str:teacher_uid>', views.TeacherDetailApiView.as_view(), name='teacher_detail'),
    path('find-user-type/<str:uid>', views.FindUserTypeByUid.as_view(), name='find_user_type'),
]
