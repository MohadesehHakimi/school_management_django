from rest_framework import serializers

from .models import Student, Teacher, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'student_uid']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'teacher_uid', 'experience']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['subject', 'course_uid', 'teacher']
